import os
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
lidar = RPLidar(None,'/dev/ttyUSB0') #check usb port with dmesg

try:
	print("RPLidar INFO: ")
	print(lidar.info)
	for scan in lidar.iter_scans():
	   for (quality, angle, distance) in scan:
	      if ( angle >= 240 and angle <=300):
	         print(quality, angle, distance) 

except KeyboardInterrupt:
    	print('Stoping.')

lidar.stop()
#lidar.stop_motor()
lidar.disconnect()
