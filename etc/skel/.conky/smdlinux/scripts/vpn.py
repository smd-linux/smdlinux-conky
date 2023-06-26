#!/usr/bin/env python3
import os

if os.path.isdir("/proc/sys/net/ipv4/conf/tun0"):
    print("${color4}ON${color}")
else:
    print("${color3}OFF${color}")