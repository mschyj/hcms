ps -ef | grep SimpleHTTPServer | awk '{print $2}' | xargs kill -9
cd /sfs/appstore
python -m SimpleHTTPServer 80 &>/dev/null &
ps -ef | grep SimpleHTTPServer | grep -v grep
