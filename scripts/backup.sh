#!/bin/bash -x
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/home/bitnami/log.out 2>&1

cd /home/bitnami/BACKUP
sudo /opt/bitnami/ctlscript.sh stop
sudo tar -pczvf application-backup.tar.gz /opt/bitnami
sudo /opt/bitnami/ctlscript.sh start
mv application-backup.tar.gz application-backup-$(date +%Y%m%d%H%M%S).tar.gz
myfile=`ls -1tr | tail -n 1`
scp -i /home/bitnami/LightsailDefaultPrivateKey-us-east-2.pem $myfile ubuntu@18.221.14.210:~/BACKUP/
#ls -1tr | head -n -5 | xargs -d '\n' rm -f --
rm -f /home/bitnami/BACKUP/*
