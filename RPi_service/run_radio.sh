#!/bin/bash

echo 'Web Radio created by Daniel Svens'

source /home/pi/RadioPi/venv/bin/activate

export FLASK_APP=/home/pi/RadioPi/application.py

flask run --host=0.0.0.0

exit 0
