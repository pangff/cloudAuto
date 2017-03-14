__author__ = 'pangff'
import time
import json
import client;
from aliyunsdkecs.request.v20140526 import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import os

def destoryInstance(clt,instanceId):
    print "destoryInstance==start:"+instanceId
    request = DeleteInstanceRequest.DeleteInstanceRequest()

    request.set_accept_format('json')
    request.set_InstanceId(instanceId)
    result = clt.do_action(request)
    print "destoryInstance==end:("+instanceId+")"+result
    return json.loads(result);

def destoryInstanceWithRetry(clt,instanceId):
    destoryInfo = destoryInstance(clt,instanceId)
    times = 0;
    if 'Code' in destoryInfo and destoryInfo['Code']=='IncorrectInstanceStatus':
        time.sleep(2)
        times+=1;
        print "destoryInstanceWithRetry==times:"+str(times);
        destoryInstanceWithRetry(clt,instanceId)

def stopInstance(clt,instanceId):
    print "stopInstance==start:"+instanceId
    request = StopInstanceRequest.StopInstanceRequest()

    request.set_accept_format('json')
    request.set_InstanceId(instanceId)
    request.set_ForceStop('true')
    result = clt.do_action(request)
    print "stopInstance==end:("+instanceId+")"+result
    return result;

def readInstances():
    file = open("./config/instances.txt", "r")
    return file.readlines()

def main():
    millis = int(round(time.time() * 1000))
    clt = client.initClient();
    instanceList = readInstances();
    instanceCount = len(instanceList);
    for i in range(0, instanceCount):
        intanceId = instanceList[i].replace("\n","");
        if intanceId!='':
            stopInstance(clt,intanceId)
            destoryInstanceWithRetry(clt,intanceId);

    millisEnd = int(round(time.time() * 1000))
    timeUse = (millisEnd-millis)
    print "instance-release-used:"+str(timeUse)+"ms"
    if os.path.exists("./config/instances.txt"):
        os.remove("./config/instances.txt")

if __name__ == '__main__':
    main()

# print result
#
# request=DescribeRegionRequest.DescribeRegionRequest()