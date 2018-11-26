import sys
import psutil

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		
		print("graph_title CPU times")
		print("graph_order system user interrupts dpc idle")
		print("graph_args --base 1000 -r -l 0 -u " + str(psutil.cpu_count()))
		print("graph_vlabel seconds")
		print("graph_info This graph shows how CPU time is spent.")
		print("graph_category system")
		print("graph_period second")
		
		print("system.label system")
		print("system.draw AREA")
		print("system.min 0")
		print("system.type DERIVE")
		print("system.info CPU time spent by the kernel in system activities")

		print("user.label user")
		print("user.draw STACK")
		print("user.min 0")
		print("user.type DERIVE")
		print("user.info CPU time spent by normal programs and daemons")
		
		print("interrupts.label interrupts")
		print("interrupts.draw STACK")
		print("interrupts.min 0")
		print("interrupts.type DERIVE")
		print("interrupts.info CPU time spent for servicing hardware interrupts")
		
		print("dpc.label dpc")
		print("dpc.draw STACK")
		print("dpc.min 0")
		print("dpc.type DERIVE")
		print("dpc.info CPU time spent servicing deferred procedure calls (DPCs); DPCs are interrupts that run at a lower priority than standard interrupts.")
		
		print("idle.label idle")
		print("idle.draw STACK")
		print("idle.min 0")
		print("idle.type DERIVE")
		print("idle.info Idle CPU time")
		
		print(".")
	if sys.argv[1] == "name":
		print("cpu_times")

if len(sys.argv) == 1:
	result = psutil.cpu_times()
	print("system.value " + str(int(result.system)))
	print("user.value " + str(int(result.user)))
	print("interrupts.value " + str(int(result.interrupt)))
	print("dpc.value " + str(int(result.dpc)))
	print("idle.value " + str(int(result.idle)))
	print(".")