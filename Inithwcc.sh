#!/bin/bash
echo "|======================================================================|"
echo " This script will initilize the HWCC environment "      
if test ! -d $HOME/.hwcc
then
  echo " $HOME/.hwcc is not existed, this script will create it"
  mkdir -p $HOME/.hwcc/storage
  echo " $HOME/.hwcc/storage is created"
  cp -fr ./examples/example.conf $HOME/.hwcc/config
  echo " $HOME/.hwcc/config is created"
  cp -fr ./script $HOME/.hwcc/ 
  echo " $HOME/.hwcc/script is created"
else
  test ! -d $HOME/.hwcc/storage && { mkdir -p $HOME/.hwcc/storage;echo " $HOME/.hwcc/storage is created"; } || echo " $HOME/.hwcc/storage is existed"
  test ! -f $HOME/.hwcc/config  && { cp -fr ./examples/example.conf $HOME/.hwcc/config;echo " $HOME/.hwcc/config is created"; } || echo " $HOME/.hwcc/config is existed"
  test ! -d $HOME/.hwcc/script  && { cp -fr ./script $HOME/.hwcc/;echo " $HOME/.hwcc/script is created"; } || echo " $HOME/.hwcc/script is existed"
fi 
echo " HWCC environment is initilized " 
echo "|======================================================================|"
