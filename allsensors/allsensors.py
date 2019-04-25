#importing all sensor imports
import gps
from adafruit_rplidar import RPLidar
from L3GD20 import L3GD20

#other imports
import os
import time
import math
import statistics

#declaring connections to sensors
lidar = RPLidar(None,'/dev/ttyUSB0') #check usb port with dmesg
gyro = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
ugps = gps.gps("localhost", "2947")
ugps.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


try:
	#Setup and Calibration for Gyro
	print("Gyroscope Setup/Info: ")
	gyro.Set_PowerMode("Normal")
	gyro.Set_FullScale_Value("250dps")
	gyro.Set_AxisX_Enabled(True)
	gyro.Set_AxisY_Enabled(True)
	gyro.Set_AxisZ_Enabled(True)
	gyro.Init()
	gyro.Calibrate()
	print("Gyroscope calibrated and ready to go!\n")

	#Setup and Calibration for Lidar
	print("RPLidar Setup/Info: ")
	print(lidar.info)
	print("RPLidar calibrated and ready to go!\n")

	#Setup and Calibration for GPS
	print("GPS Setup/Info: ")
	print(ugps.next)
	print("GPS calibrated and (maybe) ready to go!\n")

	#defining internal variables
	starttime = time.time()		#start time
	LIDAR_THRES = 1		#Lidar threshold value
	GYRO_THRES = 1		#Gyro threshold value
	gyro_x = 0
	gyro_y = 0
	gyro_z = 0
	dt = 0.01 		#reading at 10 Hz
	
	#Data Collection Loop
	print("\n...data collection is happening...\n")
	while True:
		for scan in lidar.iter_scans():
			#time.sleep(dt)
			for(quality, angle, distance) in scan:
				gyro_xyz = gyro.Get_CalOut_Value()
				#gyro_x = gyro_xyz[0]
				#gyro_y = gyro_xyz[1]
				gyro_z = gyro_xyz[2]
				if( angle >= 330 or angle <=30):
					print("{:7.2f} {:7.2f} {:7.2f} {:7.2f}".format(gyro_z, quality, angle, distance))
		


except KeyboardInterrupt:
	print("...Stopping")
