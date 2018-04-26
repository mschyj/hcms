#!/bin/bash
getFrontIP(){
  echo "Get the private ip address of frontend machine"
}
CLUSTER_HOME=/root/hwc
TARGET_HOME=/root
TARGET_USER=root
SSH_FILES="$CLUSTER_HOME/id_rsa $CLUSTER_HOME/id_rsa.pub $CLUSTER_HOME/authorized_keys"
getFrontIP
for file in $SSH_FILES
do 
  echo "copy $file to $HOME/.ssh"
  cp -fr $file $HOME/.ssh/
  scp $file $TARGET_USER@192.168.0.217:$TARGET_HOME/.ssh/
done
