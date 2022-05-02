#!/bin/sh

if [ "$DESKTOP_SESSION" = "xfce" ]; then 
   sleep 20s
   killall conky
   cd "$HOME/.conky"
   conky -c "$HOME/.conky/Seamod-all-in-one.conkyrc" &
   exit 0
fi
