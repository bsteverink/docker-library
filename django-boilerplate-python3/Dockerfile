################################################################################
# Django boilerplate Dockerfile based on Debian/jessie
# Using Python3 and Django 1.9.7
# Inspired by http://www.luiselizondo.net/a-production-ready-docker-workflow/
################################################################################

FROM python:3.5

MAINTAINER Bart Steverink (IN2SYSTEMS)

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client libmysqlclient-dev \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set up user
RUN useradd django -u 1000

RUN mkdir /home/django && chown -R django: /home/django
RUN mkdir /var/log/django && chown -R django: /var/log/django
RUN mkdir /var/log/gunicorn && chown -R django: /var/log/gunicorn

RUN mkdir /www
RUN mkdir /www/boilerplate && chown -R django: /www/boilerplate

# How to properly make sure that the user can write to site-packages (pip install)
#	and be able to run django-admin commands?
RUN chown -R django: /usr/local/lib/python3.5/site-packages
RUN chown -R django: /usr/local/bin

ENV HOME /home/django

USER django
WORKDIR /home/django
COPY ./application /home/django

RUN pip install -r requirements.txt
