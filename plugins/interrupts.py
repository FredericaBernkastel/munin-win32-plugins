import sys
import psutil

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		# The title of the graph
		print("graph_title Interrupts and context switches")
		# Arguments to "rrdtool graph". In this case, tell it that the
		# lower limit of the graph is '0', and that 1k=1000 (not 1024)
		print("graph_args --base 1000 --logarithmic")
		# The Y-axis label
		print("graph_vlabel interrupts & ctx switches / ${graph_period}")
		# Graph category
		print("graph_category system")
		# Graph information
		print("graph_info This graph shows the number of interrupts and context switches on the system. These are typically high on a busy system.")
		print("intr.info Interrupts are events that alter sequence of instructions executed by a processor. They can come from either hardware (exceptions, NMI, IRQ) or software.")
		print("ctx.info A context switch occurs when a multitasking operatings system suspends the currently running process, and starts executing another.")
		# The fields. "label" is used in the legend. "label" is the only
		# required subfield.
		print("intr.label interrupts")
		print("ctx.label context switches")
		print("sfintr.label soft interrupts")
		print("syscalls.label syscalls")
		# Specify type
		print("intr.type DERIVE")
		print("ctx.type DERIVE")
		print("sfintr.type DERIVE")
		print("syscalls.type DERIVE")
		print("intr.min 0")
		print("ctx.min 0")
		print("sfintr.min 0")
		print("syscalls.min 0")
		print(".")
	if sys.argv[1] == "name":
		print("interrupts")

if len(sys.argv) == 1:
	result = psutil.cpu_stats()
	print("intr.value " + str(result.interrupts))
	print("ctx.value " + str(result.ctx_switches))
	print("sfintr.value " + str(result.soft_interrupts))
	print("syscalls.value " + str(result.syscalls))
	print(".")