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
		print("graph_title Utilization per device")
		print("graph_info Time spent reading/writing from disk.")
		print("graph_args --base 1000 -l 0 -u 1 -r")
		print("graph_vlabel IO time in seconds")
		print("graph_category disk")
		
		for disk in counters:
			DeviceId = disk.lower()
			print(DeviceId + ".label " + disks[DeviceId])
			print(DeviceId + ".type COUNTER")
			print(DeviceId + ".draw LINE1")
			#print(DeviceId + ".cdef 0," + DeviceId + ",1000,/,+")
			
		print(".")
		
	if sys.argv[1] == "name":
		print("diskstats_utilization")

if len(sys.argv) == 1:
	for disk in counters:
		DeviceId = disk.lower()
		print(DeviceId + ".value " + str(counters[disk].read_time + counters[disk].write_time))
	print(".")