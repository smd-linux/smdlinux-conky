#!/bin/sh

if [ "$DESKTOP_SESSION" = "plasma" ]; then 
   sleep 20s
   killall conky
   cd "$HOME/.conky/smdlinux"
   conky -c "$HOME/.conky/smdlinux/SMD-Thin-Time" &
   cd "$HOME/.conky/smdlinux"
   conky -c "$HOME/.conky/smdlinux/SMD-news-monitor" &
   exit 0
fi
