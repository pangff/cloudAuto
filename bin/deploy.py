__author__ = 'pangff'
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# See http://www.cnblogs.com/ma6174/archive/2012/05/25/2508378.html

import paramiko
import threading
import yaml


def ssh_save_exec(ip, username,passwd,command):

	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,passwd,timeout=5)
		for m in command:
			stdin, stdout ,stderr = ssh.exec_command(m)
			stdin.write("Y")
			out = stdout.readlines()
			for o in out:
				print o
		print '%s\t OK \n' % (ip)
		ssh.close()
	except :
		print '%s\t Error \n' % (ip)




def main():

	f = open("./config/ips.yaml")
	config = yaml.load(f)

	cmd = config['execs']
	username = config['username']
	passwd = config['passwd']

	ips = config['ips']
	print "Beging Exec:%s on server ip: %s..." % (cmd,ips)
	for ip in ips:
		a = threading.Thread(target=ssh_save_exec ,args=(ip,username,passwd,cmd))
		a.start()
	print "Done!"


if __name__ == "__main__":
    main()