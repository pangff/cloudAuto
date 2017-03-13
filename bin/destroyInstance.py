__author__ = 'pangff'
import time

import client;
from aliyunsdkecs.request.v20140526 import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest


def destoryInstance(clt,instanceId):
    print "destoryInstance==start:"+instanceId
    request = DeleteInstanceRequest.DeleteInstanceRequest()

    request.set_accept_format('json')
    request.set_InstanceId(instanceId)
    result = clt.do_action(request)
    print "destoryInstance==end:("+instanceId+")"+result
    return result;

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
    clt = client.initClient();
    instanceList = readInstances();
    instanceCount = len(instanceList);
    for i in range(0, instanceCount):
        intanceId = instanceList[i].replace("\n","");
        stopInstance(clt,intanceId)

    print "wait 1 minute (instance stop)..:";
    time.sleep(60)

    for i in range(0, instanceCount):
        intanceId = instanceList[i].replace("\n","");
        destoryInstance(clt,intanceId);

if __name__ == '__main__':
    main()

# print result
#
# request=DescribeRegionRequest.DescribeRegionRequest()