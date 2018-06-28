#!/bin/sh

export WEBDAV_USER
export WEBDAV_PASSWORD
export WEBDAV_URL

# print ENV variables
echo "User is $WEBDAV_USER"
echo "Password is ************"
echo "URL is $WEBDAV_URL"

mount "/home/$WD_USER/stack"

echo "Mounted stack, going into infinite sync loop now."

while true; do cp -a /home/$WD_USER/host/. /home/$WD_USER/stack; sleep 5; done