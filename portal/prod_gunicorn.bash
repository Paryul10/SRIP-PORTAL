#!/bin/bash
NAME="SRIP_Portal"
DJANGODIR=/root/SRIP-PORTAL/portal
USER=root
GROUP=sudo
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=portal.settings
DJANGO_WSGI_MODULE=portal.wsgi


cd $DJANGODIR
source /root/SRIP-PORTAL/portal/prod_env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  -D --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=0.0.0.0:9000 \
  --log-level=debug \
  --log-file=/root/SRIP-PORTAL/portal/logs/debug.log
