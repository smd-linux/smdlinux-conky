#!/usr/bin/env python3
import os

if os.path.isdir("/proc/sys/net/ipv4/conf/tun0"):
    print("${color4}${execi 600 wget ipinfo.io/city -qO -}, ${execi 600 wget ipinfo.io/region -qO -}, ${execi 600 wget ipinfo.io/country -qO -}${color0}")
else:
    print("${execi 600 curl ipinfo.io/city}, ${execi 600 curl ipinfo.io/region}, ${execi 600 curl ipinfo.io/country}")