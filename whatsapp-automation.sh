#!/bin/bash

DISPLAY=:0
PATH=/usr/local/bin/:/usr/bin:/usr/sbin

while [ true ]; do
	currenttime=$(date +%H:%M:%S)
	if [[ "$(date +%A)" = "Sunday" ] || [ "$(date +%A)" = "Wednesday" ]] && [ "$currenttime" = "12:21:00" ]; then
		source /home/loredana/Stuff/Projects/whatsapp-automation/env/bin/activate
		python3 /home/loredana/Stuff/Projects/whatsapp-automation/whatsapp-automation.py
	fi
done
