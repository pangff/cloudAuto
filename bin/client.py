__author__ = 'pangff'
from aliyunsdkcore import client
import yaml

def initClient():
   f = open("config/accesskey.yaml")
   accesskey = yaml.load(f)
   clt = client.AcsClient(accesskey['accessKeyID'], accesskey['accessKeySecret'], accesskey['regionId'])
   return clt