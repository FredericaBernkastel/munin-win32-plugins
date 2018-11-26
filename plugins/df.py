import sys
import psutil

partitions = psutil.disk_partitions()

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		print("graph_title Filesystem usage (in %)")
		print("graph_category disk")
		print("graph_info This graph shows disk usage on the machine.")
		print("graph_args --upper-limit 100 -l 0")
		print("graph_vlabel %")
		
		for partition in partitions:
			try:
				sdiskusage = psutil.disk_usage(partition.device)
				print(partition.device[0] + ".label " + partition.device[:2])
			except:
				continue
		print(".")
		
	if sys.argv[1] == "name":
		print("df")

if len(sys.argv) == 1:
	for partition in partitions:
		try:
			sdiskusage = psutil.disk_usage(partition.device)
			print(partition.device[0] + ".value " + str(sdiskusage.used / float(sdiskusage.total) * 100))
		except:
			continue
	print(".")