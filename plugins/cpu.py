import sys
import psutil

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		print("graph_args -l 0 --vertical-label percent --upper-limit 100")
		print("graph_title CPU usage")
		print("graph_category system")
		print("graph_info This graph shows what the machine uses its cpu for.")
		print("cpu_total.label total")
		print("cpu_total.draw AREA")
		print("cpu_total.info Total CPU usage.")
		print(".")
	if sys.argv[1] == "name":
		print("cpu")

if len(sys.argv) == 1:
	psutil.cpu_percent(interval=0.1)
	print("cpu_total.value " + str(psutil.cpu_percent(interval=0.1)))
	print(".")