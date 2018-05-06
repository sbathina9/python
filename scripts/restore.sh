#!/bin/bash -x
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/home/bitnami/log.out 2>&1

cd /home/bitnami/BACKUP
myfile=`ls -1tr | tail -n 1`
if [ -z ${myfile} ]; then echo "myfile is unset"; exit; else echo echo "myfile is set"; fi
#if [ ! -n ${myfile} ]; then echo "myfile is zero"; exit; else echo echo "myfile is nonzero"; fi
sudo rm -rf /tmp/bitnami-backup
sudo /opt/bitnami/ctlscript.sh stop
sudo mv /opt/bitnami /tmp/bitnami-backup
sudo tar -pxzvf $myfile -C /
sudo /opt/bitnami/ctlscript.sh start

#ls -1tr | head -n -5 | xargs -d '\n' rm -f --
rm -f /home/bitnami/BACKUP/*

