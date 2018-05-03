hwcc -vvv -c ~/.hwcc/config -s ~/.hwcc/storage start slurm -n slurm > output 2>&1 && python $HOME/.hwcc/script/init_ssh.py slurm-master001 >> output &
