#!/bin/sh

export PATH="/usr/local/bin/:$PATH"
export ANEMO_REC_USER=""
export ANEMO_REC_PASSWORD=""
/usr/local/bin/node /home/pi/Developer/AneMo/receiver/lib/index.js >> /home/pi/Developer/AneMo/receiver/log/cron.log
