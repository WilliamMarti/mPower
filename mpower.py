#!/usr/bin/python

#Script to control mPower Pro units from Ubiquity
#William Marti

import paramiko
import sys
import argparse

#in this case im developing in vagrant, these will need to change
username =  "vagrant";
password =  "vagrant";


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='vagrant',
    password='vagrant')


stdin, stdout, stderr = ssh.exec_command(
    "uptime")


stdin.flush()


data = stdout.read().splitlines()
for line in data:
    print line


print "we got here"

