elasticluster -vvv -c /root/hwc/cfg/config -s /root/hwc/cfg/storage start slurm -n slurm > output 2>&1 && python /root/hwc/script/init_ssh.py slurm-frontend001 >> output &
