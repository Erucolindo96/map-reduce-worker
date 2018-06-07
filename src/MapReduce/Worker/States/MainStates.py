from src.MapReduce.Worker.States.State import InterruptableState, OneShotState, ChangingStateException
from src.MapReduce.Worker.ThriftClients import MasterRefuseConnection, RegisterWorkerException


class NotImplemented(Exception):
    pass


class WaitingForMasterState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(self, worker_ref)
        #uruchom watek sluchajacy na multicascie mastera

    def handleState(self):
        self.worker_ref.infoLog("Listening for Master")
        msg, sender = self.worker_ref.master_multicast.receive()
        self.worker_ref.infoLog("Receive from " + str(sender) + "message: " + str(msg))
        if msg.decode('utf8') == self.MASTER_JOIN_COM:
            #zapisz adres mastera
            sender_ip = sender[0]
            self.worker_ref.saveMasterIp(sender_ip)
            self.worker_ref.infoLog("Receive connection request for Master")
            self.worker_ref.infoLog("Master IP was saved")
            raise ChangingStateException("SET_CLIENT_THRIFT_WITH_MASTER")
        else:
            print ("Message from master multicast: " + str(msg))
            print ("Adress master: " + str(sender) )


class SetClientThriftWithMasterState(OneShotState):
    def __init__(self, worker_ref):
        OneShotState.__init__(self, worker_ref)

    def handleState(self):
        self.worker_ref.createClientConnectionWithMaster()
        self.worker_ref.infoLog("Client connection With Master active")

        self.worker_ref.createWorkerServer()
        self.worker_ref.startServer()
        self.worker_ref.infoLog("Worker thrift server created")

        try:
            self.worker_ref.registerWorker()
        except MasterRefuseConnection as e:
            self.worker_ref.warningLog("Registration on Master refused")
            return
        except RegisterWorkerException as e:
            self.worker_ref.fatalError("Unexpected exception while registration on Master occur. Close application")
            raise e
        raise ChangingStateException("WAIT_AS_THRIFT_SERVER_FOR_MASTER")


class WaitAsThriftServerForMasterState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(self, worker_ref)

    def handleState(self):
        self.worker_ref.infoLog("Wait as thrift Server for Master state")
        raise ChangingStateException("MASTER_CONNECTED")




class MasterConnectedState(OneShotState):
    def __init__(self, worker_ref):
        OneShotState.__init__(self, worker_ref)

    def handleState(self):
        self.worker_ref.infoLog("Waiting for work from master")
        raise ChangingStateException("WAIT_FOR_WORK")




class WaitForWorkState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(self, worker_ref)

    def handleState(self):
        if not self.isMasterLive():
            self.worker_ref.warningLog("Master is dead. Try to connect with another")
            raise NotImplemented("Wait for work")

        map_request = self.worker_ref.isMapRequested()
        if map_request :
            self.worker_ref.infoLog("Receive map request from Master")
            self.worker_ref.debugLog("Change state to Prepare and run Map()")
            raise ChangingStateException("PREPARE_AND_RUN_MAP")


class PrepareAndRunMap(OneShotState):
    def __init__(self, worker_ref):
        OneShotState.__init__(self, worker_ref)

    def handleState(self):
        self.worker_ref.runMapProcess(self.worker_ref.mapPath(), self.worker_ref.dataToMapPath(), self.worker_ref.afterMapDataPath() )
        self.worker_ref.infoLog("Run Map")
        self.worker_ref.runPairManager()
        self.worker_ref.infoLog("//Not implemented// Run after-map pair manager")

        raise ChangingStateException("MAP_STEP")


class MapStepState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(self, worker_ref)

    def handleState(self):
        if not self.isMasterLive():
            self.worker_ref.warningLog("Master is dead. Try to connect with another")
            raise NotImplemented("Wait for work")

        if self.worker_ref.isMapProcessEnd() and self.worker_ref.isPairManagerEnd():
            raise ChangingStateException("WAIT_FOR_REDUCE")

        #raise NotImplemented("Map Step State")

class WaitForReduceState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(worker_ref)

    def handleState(self):
        pass


class ReduceStepState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(self, worker_ref)

    def handleState(self):
        pass


class SendResultsToMasterState(InterruptableState):
    def __init__(self, worker_ref):
        InterruptableState.__init__(self, worker_ref)

    def handleState(self):
        pass

state_map = {
    "WAIT_FOR_MASTER": WaitingForMasterState,
    "SET_CLIENT_THRIFT_WITH_MASTER": SetClientThriftWithMasterState,
    "WAIT_AS_THRIFT_SERVER_FOR_MASTER": WaitAsThriftServerForMasterState,
    "MASTER_CONNECTED": MasterConnectedState,
    "WAIT_FOR_WORK": WaitForWorkState,
    "PREPARE_AND_RUN_MAP": PrepareAndRunMap,
    "MAP_STEP": MapStepState,
    "WAIT_FOR_REDUCE": WaitForReduceState,
    "REDUCE_STEP": ReduceStepState,
    "SEND_RESULTS_TO_MASTER": SendResultsToMasterState
}
