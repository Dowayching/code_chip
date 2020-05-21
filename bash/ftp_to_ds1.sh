#!/bin/bash

#
# @Purpose
#   send single file to DS1 server
#
# @Usage
#   bash ftp_to_ds1.sh file do_tar user password
#   -file: sent file or file path name
#   -do_tar: yes to do tar, no or else do nothing
#   -user: DS1 login ID
#   -password: DS1 login password
#
# @Remark:
#   if you don't want to key ID & password everytime, 
#   just only replace the following $2/$3, but need to 
#   concern the security issue
#

# FTP configuration
HOST=192.168.200.3  #DS1
SENT_TARGET=$1
TO_TAR=$2
USER=$3
PASSWD=$4
SENT_FILE=$SENT_TARGET

# tar file if necessary
if [ $TO_TAR == "yes" ]; then
    SENT_FILE=$SENT_TARGET.tar
    tar -czvf $SENT_FILE $SENT_TARGET
fi

# FTP command
ftp -n -p $HOST << END_SCRIPT
quote USER $USER
quote PASS $PASSWD
cd ~/Downloads
put $SENT_FILE
quit
END_SCRIPT

echo "send $SENT_TARGET to DS1 ok!"

# remove temp tar file
if [ $TO_TAR == "yes" ]; then
    rm $SENT_FILE
fi

