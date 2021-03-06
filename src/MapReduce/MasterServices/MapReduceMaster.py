#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def RegisterWorker(self, ip, listeningPort):
        """
        Parameters:
         - ip
         - listeningPort
        """
        pass

    def Reconnect(self):
        pass

    def FinishedMap(self):
        pass

    def RegisterResult(self, key, value):
        """
        Parameters:
         - key
         - value
        """
        pass

    def FinishedReduce(self):
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def RegisterWorker(self, ip, listeningPort):
        """
        Parameters:
         - ip
         - listeningPort
        """
        self.send_RegisterWorker(ip, listeningPort)
        return self.recv_RegisterWorker()

    def send_RegisterWorker(self, ip, listeningPort):
        self._oprot.writeMessageBegin('RegisterWorker', TMessageType.CALL, self._seqid)
        args = RegisterWorker_args()
        args.ip = ip
        args.listeningPort = listeningPort
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_RegisterWorker(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = RegisterWorker_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.invalidState is not None:
            raise result.invalidState
        raise TApplicationException(TApplicationException.MISSING_RESULT, "RegisterWorker failed: unknown result")

    def Reconnect(self):
        self.send_Reconnect()

    def send_Reconnect(self):
        self._oprot.writeMessageBegin('Reconnect', TMessageType.ONEWAY, self._seqid)
        args = Reconnect_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def FinishedMap(self):
        self.send_FinishedMap()
        self.recv_FinishedMap()

    def send_FinishedMap(self):
        self._oprot.writeMessageBegin('FinishedMap', TMessageType.CALL, self._seqid)
        args = FinishedMap_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_FinishedMap(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = FinishedMap_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.invalidState is not None:
            raise result.invalidState
        return

    def RegisterResult(self, key, value):
        """
        Parameters:
         - key
         - value
        """
        self.send_RegisterResult(key, value)
        self.recv_RegisterResult()

    def send_RegisterResult(self, key, value):
        self._oprot.writeMessageBegin('RegisterResult', TMessageType.CALL, self._seqid)
        args = RegisterResult_args()
        args.key = key
        args.value = value
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_RegisterResult(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = RegisterResult_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.invalidState is not None:
            raise result.invalidState
        return

    def FinishedReduce(self):
        self.send_FinishedReduce()
        self.recv_FinishedReduce()

    def send_FinishedReduce(self):
        self._oprot.writeMessageBegin('FinishedReduce', TMessageType.CALL, self._seqid)
        args = FinishedReduce_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_FinishedReduce(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = FinishedReduce_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.invalidState is not None:
            raise result.invalidState
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["RegisterWorker"] = Processor.process_RegisterWorker
        self._processMap["Reconnect"] = Processor.process_Reconnect
        self._processMap["FinishedMap"] = Processor.process_FinishedMap
        self._processMap["RegisterResult"] = Processor.process_RegisterResult
        self._processMap["FinishedReduce"] = Processor.process_FinishedReduce

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_RegisterWorker(self, seqid, iprot, oprot):
        args = RegisterWorker_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = RegisterWorker_result()
        try:
            result.success = self._handler.RegisterWorker(args.ip, args.listeningPort)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidState as invalidState:
            msg_type = TMessageType.REPLY
            result.invalidState = invalidState
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("RegisterWorker", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_Reconnect(self, seqid, iprot, oprot):
        args = Reconnect_args()
        args.read(iprot)
        iprot.readMessageEnd()
        try:
            self._handler.Reconnect()
        except TTransport.TTransportException:
            raise
        except Exception:
            logging.exception('Exception in oneway handler')

    def process_FinishedMap(self, seqid, iprot, oprot):
        args = FinishedMap_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = FinishedMap_result()
        try:
            self._handler.FinishedMap()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidState as invalidState:
            msg_type = TMessageType.REPLY
            result.invalidState = invalidState
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("FinishedMap", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_RegisterResult(self, seqid, iprot, oprot):
        args = RegisterResult_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = RegisterResult_result()
        try:
            self._handler.RegisterResult(args.key, args.value)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidState as invalidState:
            msg_type = TMessageType.REPLY
            result.invalidState = invalidState
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("RegisterResult", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_FinishedReduce(self, seqid, iprot, oprot):
        args = FinishedReduce_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = FinishedReduce_result()
        try:
            self._handler.FinishedReduce()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidState as invalidState:
            msg_type = TMessageType.REPLY
            result.invalidState = invalidState
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("FinishedReduce", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class RegisterWorker_args(object):
    """
    Attributes:
     - ip
     - listeningPort
    """


    def __init__(self, ip=None, listeningPort=None,):
        self.ip = ip
        self.listeningPort = listeningPort

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.ip = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.listeningPort = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RegisterWorker_args')
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.I32, 1)
            oprot.writeI32(self.ip)
            oprot.writeFieldEnd()
        if self.listeningPort is not None:
            oprot.writeFieldBegin('listeningPort', TType.I32, 2)
            oprot.writeI32(self.listeningPort)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(RegisterWorker_args)
RegisterWorker_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'ip', None, None, ),  # 1
    (2, TType.I32, 'listeningPort', None, None, ),  # 2
)


class RegisterWorker_result(object):
    """
    Attributes:
     - success
     - invalidState
    """


    def __init__(self, success=None, invalidState=None,):
        self.success = success
        self.invalidState = invalidState

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.invalidState = InvalidState()
                    self.invalidState.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RegisterWorker_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.invalidState is not None:
            oprot.writeFieldBegin('invalidState', TType.STRUCT, 1)
            self.invalidState.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(RegisterWorker_result)
RegisterWorker_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'invalidState', [InvalidState, None], None, ),  # 1
)


class Reconnect_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Reconnect_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Reconnect_args)
Reconnect_args.thrift_spec = (
)


class FinishedMap_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FinishedMap_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(FinishedMap_args)
FinishedMap_args.thrift_spec = (
)


class FinishedMap_result(object):
    """
    Attributes:
     - invalidState
    """


    def __init__(self, invalidState=None,):
        self.invalidState = invalidState

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.invalidState = InvalidState()
                    self.invalidState.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FinishedMap_result')
        if self.invalidState is not None:
            oprot.writeFieldBegin('invalidState', TType.STRUCT, 1)
            self.invalidState.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(FinishedMap_result)
FinishedMap_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'invalidState', [InvalidState, None], None, ),  # 1
)


class RegisterResult_args(object):
    """
    Attributes:
     - key
     - value
    """


    def __init__(self, key=None, value=None,):
        self.key = key
        self.value = value

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.key = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.value = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RegisterResult_args')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 1)
            oprot.writeString(self.key.encode('utf-8') if sys.version_info[0] == 2 else self.key)
            oprot.writeFieldEnd()
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.STRING, 2)
            oprot.writeString(self.value.encode('utf-8') if sys.version_info[0] == 2 else self.value)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(RegisterResult_args)
RegisterResult_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'key', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'value', 'UTF8', None, ),  # 2
)


class RegisterResult_result(object):
    """
    Attributes:
     - invalidState
    """


    def __init__(self, invalidState=None,):
        self.invalidState = invalidState

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.invalidState = InvalidState()
                    self.invalidState.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RegisterResult_result')
        if self.invalidState is not None:
            oprot.writeFieldBegin('invalidState', TType.STRUCT, 1)
            self.invalidState.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(RegisterResult_result)
RegisterResult_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'invalidState', [InvalidState, None], None, ),  # 1
)


class FinishedReduce_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FinishedReduce_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(FinishedReduce_args)
FinishedReduce_args.thrift_spec = (
)


class FinishedReduce_result(object):
    """
    Attributes:
     - invalidState
    """


    def __init__(self, invalidState=None,):
        self.invalidState = invalidState

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.invalidState = InvalidState()
                    self.invalidState.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FinishedReduce_result')
        if self.invalidState is not None:
            oprot.writeFieldBegin('invalidState', TType.STRUCT, 1)
            self.invalidState.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(FinishedReduce_result)
FinishedReduce_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'invalidState', [InvalidState, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

