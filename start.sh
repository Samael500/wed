#!/bin/bash
cd /home/vagrant/proj
source venv/bin/activate
exec gunicorn -b 127.0.0.1:8000 -w 2 mywed.wsgi:application
