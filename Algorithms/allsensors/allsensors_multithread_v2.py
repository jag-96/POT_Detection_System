#importing all sensor imports
import gps
from adafruit_rplidar import RPLidar
from L3GD20 import L3GD20
import smbus

#other imports
import time
import threading
import numpy
import serial
import sqlite3 as lite
import pandas as pd

#Initial Database Connection
DB_NAME = "tempDB"

#Inital lidar setup
lidar = RPLidar(None,'/dev/ttyUSB0') #check usb port with dmesg
start_time = int(round(time.time()*1000))

#Gyroscope Function
def run_gyroscope():
	gyro_conn = lite.connect(DB_NAME)
	gyro_curs = gyro_conn.cursor()
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
	dt = 0.002#readings at 1000Hz
	#print("X\tY\tZ\t")
	while True:
		current_time_gyro = int(round(time.time()*1000))
		delta_t_gyro = (current_time_gyro - start_time)
		time.sleep(dt)
		xyz = gyro.Get_CalOut_Value()
		x = xyz[0]
		y = xyz[1]
		z = xyz[2]
		print("{:14.0f},,,{:7.2f}, {:7.2f}, {:7.2f}".format(delta_t_gyro, x, y, z))
		gyro_curs.execute("INSERT INTO sensors (Time,GX,GY,GZ) VALUES (?,?,?,?);", (delta_t_gyro,x,y,z))
		gyro_conn.commit()

#GPS Function
def run_gps():
	gps_conn = lite.connect(DB_NAME)
	gps_curs = gps_conn.cursor()
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
			current_time_gps = int(round(time.time()*1000))
			delta_t_gps = (current_time_gps - start_time)
		print("{:14.0f}, {:10.6f}, {:10.6f}".format(delta_t_gps, lat, lon))
		gps_curs.execute("INSERT INTO sensors (Time,Lat,Lon) VALUES (?,?,?);", (delta_t_gps,lat,lon))
		gps_conn.commit()

#LIDAR Function
def run_lidar():
	lidar_conn = lite.connect(DB_NAME)
	lidar_curs = lidar_conn.cursor()
	while True:
		
		for scan in lidar.iter_scans():
			for(quality, angle, distance) in scan:
				current_time_lidar = int(round(time.time()*1000))				
				delta_t_lidar = (current_time_lidar - start_time)
				if( angle >= 240 and angle <=300):	#center on 267.3, corrected on filter end
					print("{:14.0f},,,,,,{:7.2f}, {:7.2f}".format(delta_t_lidar,angle, distance))
					lidar_curs.execute("INSERT INTO sensors (Time,LidAngle,LidDist) VALUES (?,?,?);", (delta_t_lidar,angle,distance))
					lidar_conn.commit()

def s_flush():
	ser = serial.Serial('/dev/ttyUSB0')
	ser.flushInput()
	ser.flushOutput()

def run_detection():
	#DEFINE DETECTION ALGORITHM HERE
	print("Detection Running")
		
#Main Thread
try:
	gyro_thread = threading.Thread(name='Gyroscope', target=run_gyroscope)
	#gps_thread = threading.Thread(name='GPS', target=run_gps)
	lidar_thread = threading.Thread(name='Lidar', target=run_lidar)
	gyro_thread.daemon = True
	#gps_thread.daemon = True
	lidar_thread.daemon = True
	gyro_thread.start()
	#gps_thread.start()
	lidar_thread.start()

	while 1:
		pass

except KeyboardInterrupt:
	lidar.stop()
	#print("Stopping")
	
except:
	print("ERROR: unable to start thread :-(")


#finally:
	#print("stop")
