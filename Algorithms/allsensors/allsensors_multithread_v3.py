#importing all sensor imports
import gps
from adafruit_rplidar import RPLidar
from L3GD20 import L3GD20
import smbus

#other imports
#import os
import time
import threading
import numpy

#Gyroscope Function
def run_gyroscope():
	gyro = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
	gyro.Set_PowerMode("Normal")
	gyro.Set_FullScale_Value("250dps")
	gyro.Set_AxisX_Enabled(True)
	gyro.Set_AxisY_Enabled(True)
	gyro.Set_AxisZ_Enabled(True)
	gyro.Init()
	gyro.Calibrate()
	t = 0
	x = 0
	y = 0
	z = 0
	dt = 0.1    #readings at 10Hz
	print("X\tY\tZ\t")
	while True:
		time.sleep(dt)
		xyz = gyro.Get_CalOut_Value()
		x = xyz[0]
		y = xyz[1]
		z = xyz[2]
		print(",,{:7.2f}, {:7.2f}, {:7.2f}".format(x, y, z))

#GPS Function
def run_gps():
	ugps = gps.gps("localhost", "2947")
	ugps.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
	lat = 0
	lon = 0
	print("LAT\tLON")
	while True:
		gps_report = ugps.next()
		if (gps_report['class'] == 'TPV'):
			lat = gps_report.lat
			lon = gps_report.lon
		print("{:10.6f}, {:10.6f}".format(lat, lon))

#LIDAR Function
def run_lidar():
	try:
		lidar = RPLidar(None,'/dev/ttyUSB0') #check usb port with dmesg
		while True:
			for scan in lidar.iter_scans():
				for(quality, angle, distance) in scan:
					if( angle >= 240 and angle <=300):	#center on 267.3, corrected on filter end
						print(",,,,,{:7.2f}, {:7.2f}".format(angle, distance))

	except KeyboardInterrupt:
		lidar.stop()
		lidar.clear_input()
		lidar.disconnect()
	finally:
		lidar.stop()
		lidar.disconnect()
#Main Thread
try:
	gyro_thread = threading.Thread(name='Gyroscope', target=run_gyroscope)
	gps_thread = threading.Thread(name='GPS', target=run_gps)
	lidar_thread = threading.Thread(name='Lidar', target=run_lidar)
	gyro_thread.daemon = True
	gps_thread.daemon = True
	lidar_thread.daemon = True
	gyro_thread.start()
	gps_thread.start()
	lidar_thread.start()
except KeyboardInterrupt:
	print("Stoping")
	
except:
	print("ERROR: unable to start thread :-(")
while 1:
	pass

