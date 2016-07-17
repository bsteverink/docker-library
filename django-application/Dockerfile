################################################################################
# Django application Dockerfile based on Debian/jessie
# Using Python3 and Django 1.9.7
# Sets up basic user and location for app.
################################################################################

FROM bsteverink/django-boilerplate:python3

MAINTAINER Bart Steverink (IN2SYSTEMS)

COPY ./application /home/django

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /home/django
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
