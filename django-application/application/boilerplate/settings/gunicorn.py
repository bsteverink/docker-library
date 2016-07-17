import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

name = "django_boilerplate"
log_level = "info"
log_file = "/var/log/gunicorn/gunicorn.log"
access_logfile = "/var/log/gunicorn/access.log"
