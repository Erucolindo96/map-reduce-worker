﻿namespace java MapReduce.Thrift

exception InvalidState {
    1: string message;
}

service MapReduceMaster {
    bool RegisterWorker(1:i32 ip, 2:i32 listeningPort) throws(1:InvalidState invalidState),
	oneway void Reconnect(),
    void FinishedMap() throws(1:InvalidState invalidState),
	void RegisterResult(1:string key, 2:string value) throws(1:InvalidState invalidState),
	void FinishedReduce() throws(1:InvalidState invalidState),
}