#!/usr/bin/python

import sys
import os
import commands
import subprocess

import vm

vmname=sys.argv[1]
vm_ip=vm.get_vm_ip(vmname)
remote_user=vm.remote_user
remote_ssh_dir="/" + vm.remote_user +"/.ssh"
local_ssh_dir="/" + vm.local_user + "/.ssh"
ssh_files=vm.ssh_files
blank=" "

if not os.path.exists(local_ssh_dir):
  os.makedirs(local_ssh_dir)
for file in ssh_files:
  if os.path.isfile(file):
    cp_cmd="cp -fr " + file + blank + local_ssh_dir
    scp_cmd="scp " + file + blank + remote_user + "@" + vm_ip + ":" + remote_ssh_dir 
    #status,output=commands.getstatusoutput(cp_cmd)
    #status,output=commands.getstatusoutput(scp_cmd)
    #output=subprocess.call(cp_cmd,shell=True)
    output=subprocess.call(scp_cmd,shell=True)
  else:
    print file + " is not found"
