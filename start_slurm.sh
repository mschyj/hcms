elasticluster -vvv -c ~/.elasticluster/config -s ~/.elasticluster/storage start slurm -n slurm > output 2>&1 && python ~/hwcc-master/script/init_ssh.py slurm-master001 >> output &
