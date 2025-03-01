#!/usr/bin/env bash

XINPUT_ID=7

xinput set-button-map $XINPUT_ID 1 2 3 4 5 6 7 8 9 10

PID=$(cat background.pid)

while : ; do
    NEW_PID=$(pgrep -P $PID)
    if [ -z "$NEW_PID" ]; then
      break;
    fi
    PID=$NEW_PID
done

kill $PID
rm background.pid
