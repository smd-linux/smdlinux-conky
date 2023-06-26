#!/usr/bin/env python3
import os

if os.path.isdir("/proc/sys/net/ipv4/conf/tun0"):
    print("${color4}${execi 600 wget http://ipecho.net/plain -qO -}${color0}")
else:
    print("${execi 600 wget http://ipinfo.io/ip -qO -}")


