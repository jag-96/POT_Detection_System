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
	#Get Start Time
	#start_time = int(round(time.time()*1000))
	#print(start_time)

	#Setup and Calibration for Gyro
	#print("Gyroscope Setup/Info: ")
	gyro.Set_PowerMode("Normal")
	gyro.Set_FullScale_Value("250dps")
	gyro.Set_AxisX_Enabled(True)
	gyro.Set_AxisY_Enabled(True)
	gyro.Set_AxisZ_Enabled(True)
	gyro.Init()
	gyro.Calibrate()
	#print("Gyroscope calibrated and ready to go!\n")

	#Setup and Calibration for Lidar
	#print("RPLidar Setup/Info: ")
	#print(lidar.info)
	#print("RPLidar calibrated and ready to go!\n")

	#Setup and Calibration for GPS
	#print("GPS Setup/Info: ")
	#print(ugps.next)
	#print("GPS calibrated and (maybe) ready to go!\n")

	#defining internal variables
	#starttime = time.time()		#start time
	LIDAR_THRES = 1		#Lidar threshold value
	GYRO_THRES = 1		#Gyro threshold value
	gyro_x = 0
	gyro_y = 0
	gyro_z = 0
	dt = 0.010 		#reading at 100 Hz
	lat = 0
	lon = 0
	
	#Data Collection Loop
	#print("\n...data collection is happening...\n")
	print("T_G(ms), GyroX, GyroY, GyroZ, T_L(ms), LidarAngle, Lidar Distance(mm), Lat,Lon")
	start_time = int(round(time.time()*1000))
	while True:
		for scan in lidar.iter_scans():
			gps_report = ugps.next()
			if(gps_report['class'] == 'TPV'):
				if hasattr(gps_report, 'lat') and hasattr(gps_report, 'lon'):
					lat = gps_report.lat
					lon = gps_report.lon

			for(quality, angle, distance) in scan:
				current_time_lidar = int(round(time.time()*1000))
				
				gyro_xyz = gyro.Get_CalOut_Value()
				gyro_x = gyro_xyz[0]
				gyro_y = gyro_xyz[1]
				gyro_z = gyro_xyz[2]
				current_time_gyro = int(round(time.time()*1000))

				delta_t_gyro = (current_time_gyro - start_time)
				delta_t_lidar = (current_time_lidar-start_time)
				if( angle >= 240 and angle <=300):	#center on 267.3, corrected on filter end
					print("{:14.0f}, {:7.2f}, {:7.2f}, {:7.2f}, {:14.0f}, {:10.6f}, {:10.6f}".format(delta_t_gyro,gyro_x,gyro_y,gyro_z, delta_t_lidar, angle, distance, lat, lon))
		


except KeyboardInterrupt:
	#print("...Stopping")

	lidar.stop()
	lidar.disconnect()


