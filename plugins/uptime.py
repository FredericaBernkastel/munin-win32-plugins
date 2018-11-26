import sys
import psutil
import datetime
import time

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		print("graph_title Uptime")
		print("graph_args --base 1000 -l 0 ")
		print("graph_scale no")
		print("graph_vlabel uptime in days")
		print("graph_category system")
		print("uptime.label uptime")
		print("uptime.draw AREA")
		print(".")
	if sys.argv[1] == "name":
		print("uptime")

if len(sys.argv) == 1:
	print("uptime.value " + str((time.time() - psutil.boot_time()) / 86400))
	print(".")