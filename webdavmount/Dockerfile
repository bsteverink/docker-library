FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
        davfs2 \
        ca-certificates \
        python-pip \
        python-setuptools \
        #python-dev \
        #build-essential \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV WD_USER=webdav \
    WEBDAV_USER=user \
    WEBDAV_PASSWORD=pass \
    WEBDAV_URL=url

# Set up user and add to group
RUN useradd -m -u 1000 $WD_USER  && \
    usermod -aG davfs2 $WD_USER

# Add a dir for config
RUN mkdir /home/$WD_USER/stack && \
    mkdir /home/$WD_USER/.davfs2 && \
    cp /etc/davfs2/secrets /home/$WD_USER/.davfs2/secrets

# Make sure all permissions are correct
RUN chown $WD_USER:$WD_USER /home/$WD_USER/stack && \
    chown -R $WD_USER:$WD_USER /home/$WD_USER/.davfs2 && \
    chmod 600 /home/$WD_USER/.davfs2/secrets && \
    chgrp $WD_USER /etc/fstab && \
    chmod 770 /etc/fstab

# Allow mount to be executed by non-priveleged users
RUN chmod u+s /sbin/mount.davfs

# Make sure file locks are not used
#RUN perl -p -i -e "s/#\s*use_locks\s*1/use_locks 0/" /etc/davfs2/davfs2.conf

ADD ./requirements.txt /home/$WD_USER/
WORKDIR /home/$WD_USER

RUN pip install -U pip
RUN pip install -Ur requirements.txt

ADD ./server.py /home/$WD_USER/

ADD ./start.sh /home/$WD_USER/
RUN chown $WD_USER:$WD_USER /home/$WD_USER/start.sh && \
    chmod u+x /home/$WD_USER/start.sh

USER $WD_USER

CMD ["./start.sh"]

# docker run -it -p 5000:5000 --cap-add=SYS_ADMIN --device=/dev/fuse -v /Users/bartsteverink/Sites/docker-library/webdavmount:/home/webdav bsteverink/webdavmount /bin/bash