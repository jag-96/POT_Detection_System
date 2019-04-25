import os
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
lidar = RPLidar(None,'/dev/ttyUSB0')


try:
	print("RPLidar INFO: ")
	print(lidar.info)
	for scan in lidar.iter_scans():
	   for (_, angle, distance) in scan:
	      print([min([359, floor(angle)])], distance)
	  

except KeyboardInterrupt:
    	print('Stoping.')



lidar.stop()
lidar.disconnect()
