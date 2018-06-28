FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
        davfs2 \
        ca-certificates \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV WD_USER=webdav \
    WEBDAV_USER=user \
    WEBDAV_PASSWORD=pass \
    WEBDAV_URL="url"


# Set up user and add to group
RUN useradd -m -u 1000 $WD_USER  && \
    usermod -aG davfs2 $WD_USER

# Add a dir for config
RUN mkdir /home/$WD_USER/stack && \
    mkdir /home/$WD_USER/.davfs2 && \
    cp /etc/davfs2/secrets /home/$WD_USER/.davfs2/secrets

RUN chown $WD_USER:$WD_USER /home/$WD_USER/stack && \
    chown -R $WD_USER:$WD_USER /home/$WD_USER/.davfs2 && \
    chmod 600 /home/$WD_USER/.davfs2/secrets

# Allow mount to be executed by non-priveleged users
RUN chmod u+s /sbin/mount.davfs

RUN echo "${WEBDAV_URL} ${WEBDAV_USER} ${WEBDAV_PASSWORD}" > /home/$WD_USER/.davfs2/secrets && \
    echo "${WEBDAV_URL} /home/${WD_USER}/stack davfs user,rw,noauto 0 0" >> /etc/fstab

ADD ./start.sh /home/$WD_USER/
RUN chown $WD_USER:$WD_USER /home/$WD_USER/start.sh && \
    chmod u+x /home/$WD_USER/start.sh

USER $WD_USER

WORKDIR /home/webdav

CMD ["./start.sh"]