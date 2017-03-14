__author__ = 'pangff'
import json
import client;
import urllib2;
import time
from aliyunsdkecs.request.v20140526 import CreateInstanceRequest
from aliyunsdkecs.request.v20140526 import StartInstanceRequest
from aliyunsdkecs.request.v20140526 import AllocatePublicIpAddressRequest
import yaml
import threading

# {"InstanceId":"i-wz9csdigjpkey122lmlg","RequestId":"2D3AB98D-6F3B-4296-9B3D-74709C979D57"}
def createInstance(clt):
    request = CreateInstanceRequest.CreateInstanceRequest()
    f = open("./config/createconf.yaml")
    config = yaml.load(f)
    request.set_ImageId(config['ImageId'])
    request.set_SecurityGroupId(config['SecurityGroupId'])
    request.set_HostName(config['HostName'])
    request.set_Password(config['Password'])
    request.set_InstanceType(config['InstanceType'])
    request.set_InternetMaxBandwidthOut(config['InternetMaxBandwidthOut'])
    request.set_accept_format('json')
    result = clt.do_action(request)
    print "createInstance=="+result

    return json.loads(result);

# {"RequestId":"486E5410-7BAF-438B-8B7F-2C1193634ACA"}
def startInstance(clt,instanceId):
    request = StartInstanceRequest.StartInstanceRequest()

    request.set_accept_format('json')
    request.set_InstanceId(instanceId)
    result = clt.do_action(request)
    print "startInstance=="+result
    return result;

# {"RequestId":"DD1C4650-2C47-429E-96DB-BC913EF56175","IpAddress":"xxx.25.154.89"}
def allocatePublicIpAddress(clt,instanceId):
    request = AllocatePublicIpAddressRequest.AllocatePublicIpAddressRequest()

    request.set_accept_format('json')
    request.set_InstanceId(instanceId)
    result = clt.do_action(request)
    print "allocatePublicIpAddress=="+result
    return  json.loads(result);


def writeToFile(instanceId):
    f = open('./config/instances.txt', 'a')
    f.write(instanceId+'\n')  # python will convert \n to os.linesep
    f.close()

def clearFile():
    f = open('./config/instances.txt', 'w')
    f.write("")  # python will convert \n to os.linesep
    f.close()


def checkServiceStatus(ip):
    print 'checkServiceStatus-start...';
    attempts = 0
    while attempts<999999:
        try:
            result = urllib2.urlopen("http://"+ip+":3100/hello/123",timeout=60).read();
            print 'checkServiceStatus='+result;
            return result;
        except Exception, e:
            attempts += 1;
            time.sleep(2)
            print e
            print 'service not started...retry'+str(attempts)+"tiems";

def main():
    clearFile();
    millis = int(round(time.time() * 1000))
    clt = client.initClient();
    instanceInfo = createInstance(clt);
    if instanceInfo['InstanceId']!="":
        writeToFile(instanceInfo['InstanceId']);
        ipInfo = allocatePublicIpAddress(clt,instanceInfo['InstanceId'])
        startInstance(clt,instanceInfo['InstanceId']);
        serverInfo = checkServiceStatus(ipInfo['IpAddress']);
        millisEnd = int(round(time.time() * 1000))
        timeUse = (millisEnd-millis)
        print "service-start-use:"+str(timeUse)+"ms"
        print serverInfo;
    else:
        print "error to create instance"


if __name__ == '__main__':
    main()

# print result
#
# request=DescribeRegionRequest.DescribeRegionRequest()