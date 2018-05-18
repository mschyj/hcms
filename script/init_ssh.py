#!/usr/bin/python

import sys
import os
import commands
import subprocess

import vm
import paramiko

vmname=sys.argv[1]
vm_ip=vm.get_vm_ip(vmname)
remote_user=vm.remote_user
remote_ssh_dir="/" + vm.remote_user +"/.ssh"
local_ssh_dir="/" + vm.local_user + "/.ssh"
ssh_files=vm.ssh_files
blank=" "

if not os.path.exists(local_ssh_dir):
  os.makedirs(local_ssh_dir)
  ssh_keygen_cmd="ssh-keygen -t rsa"
  output=subprocess.call(ssh_keygen_cmd,shell=True)

ssh_authorized_key="cat " + local_ssh_dir + "/id_rsa.pub >> " + local_ssh_dir + "/authorized_keys"
output=subprocess.call(ssh_authorized_key,shell=True) 

for file in ssh_files:
  if os.path.isfile(file):
    #cp_cmd="cp -fr " + file + blank + local_ssh_dir
    scp_cmd="scp -q " + file + blank + remote_user + "@" + vm_ip + ":" + remote_ssh_dir 
    #status,output=commands.getstatusoutput(cp_cmd)
    #status,output=commands.getstatusoutput(scp_cmd)
    #output=subprocess.call(cp_cmd,shell=True)
    subprocess.call(scp_cmd,shell=True)
  else:
    print file + " is not found"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(vm_ip, port=22,
            username=remote_user,
            allow_agent=True,
            key_filename=local_ssh_dir + "/id_rsa",
            timeout=60)
clustername=vmname[0:vmname.index("-")]
print "The master name is " + vmname
print "The cluster name is " + clustername
cmd_suspend = "sed -i 's/clustername/" + clustername + "/g' /etc/slurm/slurm.suspend.sh"
cmd_resume = "sed -i 's/clustername/" + clustername + "/g' /etc/slurm/slurm.resume.sh"
stdin, stdout, stderr = ssh.exec_command(cmd_suspend)
#print stdout.readlines()
stdin, stdout, stderr = ssh.exec_command(cmd_resume)
#print stdout.readlines()
ssh.close()
