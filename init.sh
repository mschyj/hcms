#!/bin/bash
if [ -d $HOME/.hwcc ]
then
  mv $HOME/.hwcc $HOME/hwcc_bak
fi 
 
mkdir -p $HOME/.hwcc/storage
cp -fr ./examples/example.conf $HOME/.hwcc/config
cp -fr ./script $HOME/.hwcc/
