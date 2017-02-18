#!/bin/sh

export PATH="/usr/local/bin/:$PATH"
/home/pi/set-env-vars.sh
/usr/local/bin/node /home/pi/Developer/AneMo/receiver/lib/index.js >> /home/pi/Developer/AneMo/receiver/log/cron.log
