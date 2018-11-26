import sys
import wmi
import psutil
import re

c = wmi.WMI()
disks = {}
for disk in c.Win32_DiskDrive(["Caption", "DeviceID"]):
	DeviceId = disk.DeviceID.replace("\\\\.\\", "").lower()
	Caption = disk.Caption.replace(" ATA Device", "").replace(" SCSI Disk Device", "")
	Caption = re.sub(r"\s", "", Caption)
	disks[DeviceId] = Caption
counters = psutil.disk_io_counters(perdisk=True)

if len(sys.argv) == 2:
	if sys.argv[1] == "config":
		print("graph_order down up")
		print("graph_title Disk IOs per device")
		print("graph_args --base 1000")
		print("graph_vlabel IOs/${graph_period} read (-) / write (+)")
		print("graph_category disk")
		
		for disk in counters:
			DeviceId = disk.lower()
			print(DeviceId + "_read.label " + disks[DeviceId])
			print(DeviceId + "_read.type COUNTER")
			print(DeviceId + "_read.graph no")
			print(DeviceId + "_write.label " + disks[DeviceId])
			print(DeviceId + "_write.type COUNTER")
			print(DeviceId + "_write.negative " + DeviceId + "_read")
			
		print(".")
		
	if sys.argv[1] == "name":
		print("diskstats_io")

if len(sys.argv) == 1:
	for disk in counters:
		DeviceId = disk.lower()
		print(DeviceId + "_read.value " + str(counters[disk].read_count))
		print(DeviceId + "_write.value " + str(counters[disk].write_count))
	print(".")