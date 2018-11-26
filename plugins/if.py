import sys
import psutil

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		print("graph_order down up")
		print("graph_title network traffic")
		print("graph_args --base 1000")
		print("graph_vlabel bits in (-) / out (+) per ${graph_period}")
		print("graph_category network")
		print("graph_info This graph shows the traffic of the network interface.")
		print("down.draw AREA")
		print("down.label received")
		print("down.type DERIVE")
		print("down.graph no")
		print("down.cdef down,8,*")
		print("down.min 0")
		print("up.draw AREA")
		print("up.label bps")
		print("up.type DERIVE")
		print("up.negative down")
		print("up.cdef up,8,*")
		print("up.min 0")
		print(".")
	if sys.argv[1] == "name":
		print("if")

if len(sys.argv) == 1:
	result = psutil.net_io_counters()
	print("up.value " + str(result.bytes_sent))
	print("down.value " + str(result.bytes_recv))
	print(".")