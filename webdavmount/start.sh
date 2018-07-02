#!/bin/sh

export WEBDAV_USER
export WEBDAV_PASSWORD
export WEBDAV_URL

# print ENV variables
echo "User is $WEBDAV_USER"
echo "Password is ************"
echo "URL is $WEBDAV_URL"

echo "${WEBDAV_URL} ${WEBDAV_USER} ${WEBDAV_PASSWORD}" > /home/$WD_USER/.davfs2/secrets && \
echo "${WEBDAV_URL} /home/${WD_USER}/stack davfs user,rw,noauto 0 0" >> /etc/fstab

mount "/home/$WD_USER/stack"

# Starting server

export FLASK_APP=server.py
flask run --host=0.0.0.0