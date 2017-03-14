# cloudAuto
通过阿里云python sdk实现阿里云平台实例自动创建、释放脚本。

* 实例创建：在脚本例子中实现了通过一个有node环境、pm2可以自启动的restify镜像创建按量付费的ECS实例，并在启动ECS后测试自启动restify服务的连接情况
当连接成功后通过日志纪录整个过程所用时间，同时将创建实例id纪录在config/instances.txt中。
* 实例释放：脚本例子中通过读取config/instances.txt中实例id，进行批量释放操作，并通过日志答应整个操作所用时间

## 环境要求

    * python 2.7
    * 该项目中提供了一个简单的simple-restify服务项目，可以将其放到已有ECS中，添加pm2自启动，生成镜像

## 配置方法

* clone项目到本地 git clone https://github.com/pangff/cloudAuto.git
* pip安装相关依赖（包括阿里云的python sdk）(pip install xxxx)
* 修改config/accesskey.yaml.template。重命名为accesskey.yaml。并添加自己阿里云的accessKeyID、accessKeySecret、regionId(地区)信息
* 修改config/createconf.yaml中信息，根据自己需要做相关配置
* 创建实例:cd到cloudAuto目录，运行python bin/createInstance.py.(注意：如果有了自启动服务的镜像，那么需要修改createInstance.py中checkServiceStatus方法的服务url，如果没有可以注释 serverInfo = checkServiceStatus(ipInfo['IpAddress']);部分)
* 释放实例:cd到cloudAuto目录，运行python bin/destroyInstance.py.


