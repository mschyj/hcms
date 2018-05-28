echo "This script will initilize the slurm power saving script"
echo "You could check the machine name of the master node on the cloud by the Web Console"
echo "Please do not use ip address for the slurm master node"
read -p "Please input the machine name of the master node on the cloud(example:slurm-master001):" hostname
python $HOME/.hwcc/script/init_ssh.py $hostname 
echo "The initilization is done, please verify your power saving environment"
