import os
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
lidar = RPLidar(None,'/dev/ttyUSB0') #check usb port with dmesg

try:
	print("RPLidar INFO: ")
	print(lidar.info)
	for scan in lidar.iter_scans():
	   for (quality, angle, distance) in scan:
	      if ( angle >= 330 or angle <=30):
	         print(quality, angle, distance) 

except KeyboardInterrupt:
    	print('Stoping.')

lidar.stop()
lidar.disconnect()
