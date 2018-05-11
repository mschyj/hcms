#!/bin/bash
# this is config file
################################ cloud config ##################################

echo "Please config your cloud/openstack info"
read -p "Enter your provider [default openstack,pass p] :" provider
if [ "$provider" != p ]
    then
        if [ ! -z $provider ]
            then
                sed -i "/^provider/c provider = $provider" ~/.hwcc/config
            else
                sed -i "/^provider/c provider = openstack" ~/.hwcc/config
        fi
fi

read -p "Enter your identity_api_version[default 3, pass p]: " identify_api_version
default_api_version=3
if [ "$identify_api_version" != p ]
    then
        if [ "$identify_api_version" != "$default_api_version" ]
            then
               sed -i "/^identify_api_version/c identify_api_version = $identify_api_version" ~/.hwcc/config
            else
               identify_api_version=3
               sed -i "/^identify_api_version/c identify_api_version = 3" ~/.hwcc/config
        fi
    else
        identify_api_version=`grep identify_api_version ~/.hwcc/config | awk '{print $3}'`
fi


read -p "Enter your project name[pass p]: " project_name
if [ "$project_name" != p ]
    then
        sed -i "/^project_name/c project_name = $project_name" ~/.hwcc/config
fi

read -p "Enter your project id[pass p]: " project_id
if [ "$project_id" != p ]
    then
        sed -i "/^roject_id/c project_id = $project_id" ~/.hwcc/config
fi

read -p "Enter your region name[pass p]: " region_name
if [ "$region_name" != p ]
    then
        sed -i "/^region_name/c region_name = $region_name" ~/.hwcc/config
        sed -i "/^sfs_endpoint/c sfs_endpoint = sfs.$region_name.myhuawei.com" ~/.hwcc/config
    else
        region_name=`grep region_name ~/.hwcc/config | awk '{print $3}'`
        sed -i "/^sfs_endpoint/c sfs_endpoint = sfs.$region_name.myhuawei.com" ~/.hwcc/config
fi

sed -i "/^auth_url/c auth_url = https://iam.$region_name.myhwclouds.com/v$identify_api_version" ~/.hwcc/config
#readd -p "Enter your auth_url [default https://iam.cn-north-1.myhwclouds.com/v3,pass p]: "  auth_url
#
#if [ "$auth_url" != p ]
#    then
#        if [ ! -z $auth_url ]
#            then 
#                sed -i "/^auth_url/c auth_url = $auth_url" ~/.hwcc/config
#            else
#                sed -i "/^auth_url/c auth_url = https://iam.cn-north-1.myhwclouds.com/v3" ~/.hwcc/config
#        fi
#fi


read -p "Enter your username[pass p]: " username
if [ "$username" != p ] 
    then
        read -p "confirm your username[y/n] :" confirm_username
        if [ "$confirm_username" == "y" ]
            then 
                sed -i "/^username/c username = $username" ~/.hwcc/config
                sed -i "/^project_domain_name/c project_domain_name = $username" ~/.hwcc/config
                sed -i "/^user_domain_name/c user_domain_name = $username" ~/.hwcc/config
            else
                read -p "Enter your username again: " username 
                sed -i "/^username/c username = $username" ~/.hwcc/config
                sed -i "/^project_domain_name/c project_domain_name = $username" ~/.hwcc/config
                sed -i "/^user_domain_name/c user_domain_name = $username" ~/.hwcc/config
        fi
fi

read -p "Enter your password[pass p]: " password1
if [ "$password1" != p ]
    then 
        read -p "Enter your password again: " password2
        while [ "$password1" != "$password2" ]
        do
            echo "passwords entered twice are diffrent, please enter again!"
            read -p "Enter your password: " password1
            read -p "Enter your password again: " password2
        done
        sed -i "/^password/c password = $password1" ~/.hwcc/config
fi

#read -p "Enter if you need floating_ip[default n]": requset_floating_ip
#if [ "$request_floating_ip" == y ]
#    then
#        sed -i "/^request_floating_ip/c request_floating_ip = True" ~/.hwcc/config 
#fi
        

################################ sfs config ################################## 


read -p "Enter if you want to use sfs[y/n,default y, pass p]: " is_create_sfs

if [ "$is_create_sfs" != p ]
    then
        if [ "$is_create_sfs" == "y" ] || [ -z $is_create_sfs ]
            then
                sed -i "/^is_create_sfs/c is_create_sfs = True" ~/.hwcc/config
                read -p "Enter if you want to use a exist one [y/n, default y,pass p]: " use_exist_one
                if [ "$use_exist_one" != p ]
                    then
                        if [ "$use_exist_one" == "y" ] || [ -z $use_exist_one ]
                            then
                                read -p "Enter your sfs name[default hwcc_sfs,pass p]: " sfs_name
                                if [ "$sfs_name" != p ]
                                    then
                                        if [ ! -z $sfs_name ]
                                            then
                                                sed -i "/^sfs_name/c sfs_name = $sfs_name" ~/.hwcc/config
                                            else
                                                sed -i "/^sfs_name/c sfs_name = hwcc_sfs" ~/.hwcc/config
                                        fi
                                fi
                            else
                                read -p "Enter your sfs name[default hwcc_sfs,pass p]: " sfs_name
                                if [ "$sfs_name" != p ]
                                    then
                                        if [ ! -z $sfs_name ]
                                            then
                                                sed -i "/^sfs_name/c sfs_name = $sfs_name" ~/.hwcc/config
                                            else
                                                sed -i "/^sfs_name/c sfs_name = hwcc_sfs" ~/.hwcc/config
                                        fi
                                fi
                                
                                read -p "Enter your sfs size[default 1000G,pass p]: " sfs_size
                                if [ "$sfs_size" != p ]
                                    then
                                        if [ ! -z $sfs_size ]
                                            then
                                                sed -i "/^sfs_size/c sfs_size = $sfs_size" ~/.hwcc/config
                                            else
                                                sed -i "/^sfs_size/c sfs_size = 1000" ~/.hwcc/config
                                        fi
                                fi

                                read -p "Enter your sfs network id[vpc id,pass p]: " sfs_network_id
                                if [ "$sfs_network_id" != p ]
                                    then
                                        if [ ! -z $sfs_network_id ]
                                            then
                                                sed -i "/^sfs_network_id/c sfs_network_id = $sfs_network_id" ~/.hwcc/config
                                        fi
                                fi

                               # read -p "Enter your sfs endpoint[default sfs.cn-north-1.myhuaweicloud.com ,pass p]: " sfs_endpoint       
                               # if [ "$sfs_endpoint" != p ]
                               #     then
                               #         if [ ! -z $sfs_endpoint ]
                               #             then
                               #                 sed -i "/^sfs_endpoint/c sfs_endpoint = $sfs_endpoint" ~/.hwcc/config          
                               #             else
                               #                 sed -i "/^sfs_endpoint/c sfs_endpoint = sfs.cn-north-1.myhuaweicloud.com" ~/.hwcc/config               
                               #         fi
                               # fi
                        fi
                fi
        else
            sed -i "/^is_create_sfs/c is_create_sfs = False" ~/.hwcc/config
        fi
fi

################################ squid config ##################################
echo "Please config your squid info"
read -p "Enter id you want to use squid[default y, pass p]: " is_use_squid
if [ "$is_use_squid" != p ]
    then
        if [ -z $is_use_squid ] || [ "$is_use_squid" == "y" ]
            then
                sed -i "/^is_use_squid/c is_use_squid = True" ~/.hwcc/config
                yum install squid -y
                read -p "Enter your squid ip[pass p]: " host_ip
                if [ "$host_ip" != p ]
                    then
                        sed -i "/^host_ip/c host_ip = $host_ip" ~/.hwcc/config
                fi
                read -p "Enter your squid port[default 3128,pass p]: " squid_port
                if [ "$squid_port" != p ]
                    then
                        if [ ! -z $squid_port ]
                            then
                                sed -i "/^http_port/c http_port $squid_port" /etc/squid/squid.conf
                            else
                                sed -i "/^http_port/c http_port 3128" /etc/squid/squid.conf
                        fi
                fi
        else
            sed -i "/^is_use_squid/c is_use_squid = False" ~/.hwcc/config
        fi
fi



################################# login config ################################## 
echo "Please config your login info"
read -p "Enter your image_user[default root, pass p]: " image_user
if [ "$image_user" != p ]
    then
        if [ ! -z $image_user ]
            then
                sed -i "/^image_user/c image_user = $image_user" ~/.hwcc/config
            else
                sed -i "/^image_user/c image_user = root" ~/.hwcc/config
        fi
fi

read -p "Enter your image_user_sudo[default root, pass p]: " image_user_sudo
if [ "$image_user_sudo" != p ]
    then
        if [ ! -z $image_user_sudo ]
            then
                sed -i "/^image_user_sudo/c image_user_sudo = $image_user_sudo" ~/.hwcc/config
            else
                sed -i "/^image_user_sudo/c image_user_sudo = root" ~/.hwcc/config
        fi
fi

read -p "Enter if you want sudo [default y, pass p]: " image_sudo
if [ "$image_sudo" != p ]
    then
        if [ ! -z $image_sudo ]
            then
                sed -i "/^image_sudo/c image_sudo = False" ~/.hwcc/config
            else
                sed -i "/^image_sudo/c image_sudo = " ~/.hwcc/config
        fi
fi

read -p "Enter your key name[default hwcluster, pass p]: " user_key_name
if [ "$user_key_name" != p ]
    then
        if [ ! -z $user_key_name ]
            then
                sed -i "/^user_key_name/c user_key_name = $user_key_name" ~/.hwcc/config
            else
                sed -i "/^user_key_name/c user_key_name = hwcluster" ~/.hwcc/config
        fi
fi

read -p "Enter your public key path to save[default ~/.ssh/id_rsa.pub, pass p]: " user_key_public
if [ "$user_key_public" != p ]
    then
        if [ ! -z $user_key_public ]
            then
                sed -i "/^user_key_public/c user_key_public = $user_key_public" ~/.hwcc/config
            else
                sed -i "/^user_key_public/c user_key_public = ~/.ssh/id_rsa.pub" ~/.hwcc/config
        fi
fi

read -p "Enter your private key path to save[default ~/.ssh/id_rsa, pass p]: " user_key_private
if [ "$user_key_private" != p ]
    then
        if [ ! -z $user_key_private ] 
            then
                sed -i "/^user_key_private/c user_key_private = $user_key_private" ~/.hwcc/config
            else
                sed -i "/^user_key_private/c user_key_private = ~/.ssh/id_rsa" ~/.hwcc/config
        fi 
fi 


       
################################ setup slurm config ##################################
echo "In slurm/pbs/sge config, you cannot type 'p'"

start_line_num=`grep -n "user_key_private" ~/.hwcc/config | awk -F ":" '{print $1}'`
sed -i "$(expr $start_line_num + 1),\$d" ~/.hwcc/config 

install=0
read -p "Do you want to intall slurm:[y/n default y] " install_slurm

if [ -z $install_slurm ] || [ "$install_slurm" == "y" ]
    then
        echo -e "\n[setup/ansible_slurm]" >> ~/.hwcc/config
        echo "provider = ansible" >> ~/.hwcc/config
        read -p "Enter your slurm master name[default master]: " slurm_master
        if [ ! -z $slurm_master ]
            then
                echo "master_groups = slurm_$slurm_master" >> ~/.hwcc/config
        else
            slurm_master=master
            echo "master_groups = slurm_master" >>~/.hwcc/config
        fi

        read -p "Enter your slurm worker name[default worker]: " slurm_worker
        if [ ! -z $slurm_worker ]
            then
                echo "worker_groups = slurm_$slurm_worker" >> ~/.hwcc/config
        else
            slurm_worker=worker
            echo "worker_groups = slurm_worker" >>~/.hwcc/config
        fi  

        ######################### setup slurm config ##################################
        echo -e "\n[cluster/slurm]" >> ~/.hwcc/config
        echo "cloud = catalyst" >> ~/.hwcc/config
        read -p "Enter user name to login slurm [default root]: " login
        if [ ! -z $login ]
            then
                echo "login = $login" >> ~/.hwcc/config
            else
                echo "login = root" >>~/.hwcc/config
        fi
        echo "setup = ansible-slurm" >> ~/.hwcc/config        
        read -p "Enter your security group name of slurm[default sg-cluster]: " security_group
        if [ ! -z $security_group ]
            then
                echo "security_group = $security_group" >> ~/.hwcc/config
            else
                echo "security_group = sg-cluster" >>~/.hwcc/config
        fi

        read -p "Enter your network id of slurm[subnet id]: " network_ids
        if [ ! -z $network_ids ]
            then
                echo "network_ids = $network_ids" >> ~/.hwcc/config
        fi

        read -p "Enter your image id of slurm: " image_id
        if [ ! -z $image_id ]
            then
                echo "image_id = $image_id" >> image_id
        fi
        
        read -p "Enter your number of slurm master: " master_nodes
        if [ $master_nodes -lt 1 ] || [ -z $master_nodes ]
            then
                read -p "Enter valid number :" master_nodes
                echo "master_nodes = $master_nodes" >> ~/.hwcc/config
            else
                echo "master_nodes = $master_nodes" >> ~/.hwcc/config            
        fi
        read -p "Enter your number of slurm worker: " worker_nodes
        
        if [ $worker_nodes -lt 1 ] || [ -z $worker_nodes ]
            then
                read -p "Enter valid number :" worker_nodes
                echo "worker_nodes = $worker_nodes" >> ~/.hwcc/config
            else
                echo "worker_nodes = $worker_nodes" >> ~/.hwcc/config
        fi

        echo -e "\n[cluster/slurm/$slurm_master]" >> ~/.hwcc/config 
        read -p "Enter your flavor of slurm master: " master_flavor
        if [ ! -z $master_flavor ]
            then
                echo "flavor = $master_flavor" >> ~/.hwcc/config
        fi
        echo -e "\n[cluster/slurm/$slurm_worker]" >> ~/.hwcc/config
        read -p "Enter your flavor of slurm worker: " slurm_flavor
        if [ ! -z $slurm_flavor ]
            then
                echo -e "flavor = $slurm_flavor" >> ~/.hwcc/config
        fi
 fi      
