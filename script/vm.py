#!/usr/bin/env python

import getpass
import sys
import os
import ConfigParser

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client

home=os.environ['HOME']
config=ConfigParser.ConfigParser()
config.read(home + "/.elasticluster/config")
username=config.get("cloud/catalyst","username")
password=config.get("cloud/catalyst","password")
auth_url=config.get("cloud/catalyst","auth_url")
user_domain_name=config.get("cloud/catalyst","user_domain_name")
project_domain_name=config.get("cloud/catalyst","project_domain_name")
project_name=config.get("cloud/catalyst","project_name")

local_user=getpass.getuser()
remote_user=config.get("login/centos","image_user")
ssh_files=[home+"/.ssh/id_rsa",home+"/.ssh/id_rsa.pub",home + "/.ssh/authorized_keys"]

auth = v3.Password(
       username=username,
       password=password,
       auth_url=auth_url,
       user_domain_name=user_domain_name,
       project_domain_name=project_domain_name,
       project_name=project_name
    )
		
def start_vm(vmname):
  found=False
  sess = session.Session(auth=auth, verify=True)
  #print sess.get_endpoint(service_type='compute',interface='public')
  novacli = client.Client("2.1", session=sess)
  instances=novacli.servers.list()
  #print instances
  if vmname == 'all':
    for vm in instances:
      if vm.status == 'SHUTOFF':
        print vm.name + " is starting"
        print vm.status
        novacli.servers.start(vm)
        found = True
  else:
    for vm in instances:
      if vm.name == vmname:
        print vm.name + " is starting"
        novacli.servers.start(vm)
        found = True
  if(not found):
    print vmname + " is not found"

def stop_vm(vmname):
  found=False
  sess = session.Session(auth=auth, verify=True)
  #print sess.get_endpoint(service_type='compute',interface='public')
  novacli = client.Client("2.1", session=sess)
  instances=novacli.servers.list()
  #print instances
  for vm in instances:
    if vm.name == vmname:
      print vm.name + " is stopping"
      novacli.servers.stop(vm)
      found = True
  if(not found):
    print vmname + " is not found"
	
def get_vm_ip(vmname):
  found=False
  frontip=0
  sess = session.Session(auth=auth, verify=True)
  novacli = client.Client("2.1", session=sess)
  instances=novacli.servers.list()
  for vm in instances:
    if vm.name == vmname:
      IPs = sum(vm.networks.values(),[])
      frontip=IPs[0]
      found = True
  if(not found):
    print vmname + " is not found"
  return frontip

def find_vm(vmname):
  sess = session.Session(auth=auth, verify=True)
  novacli = client.Client("2.1", session=sess)
  try:
    vm = novacli.servers.find(name=vmname)
    print vm
  except AttributeError:
    print "Attribute Error"
  except client.exceptions.NotFound:
    print "Not Found"

def init_ssh():
  print "init ssh"

if __name__ == "__main__":
  print ('This is main of module "vm.py"')
  #get_vm_ip("slurm-frontend001")
  #start_vm('all')
  #find_vm("slurm-frontend004")
