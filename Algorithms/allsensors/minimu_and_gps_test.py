from L3GD20 import L3GD20
import gps
import time
import numpy

# Declare GPS and gyroscope
gyro = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
ugps = gps.gps("localhost", "2947")
ugps.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

try:
    # Setup and Calibrate Gyroscope
    gyro.Set_PowerMode("Normal")
    gyro.Set_FullScale_Value("250dps")
    gyro.Set_AxisX_Enabled(True)
    gyro.Set_AxisY_Enabled(True)
    gyro.Set_AxisZ_Enabled(True)
    gyro.Init()
    gyro.Calibrate()  

    
    # Read values loop
    t = 0
    x = 0
    y = 0
    z = 0
    dt = 0.01    #readings at 100Hz
    lat = 0
    lon = 0
    
    print("Time(ms)\tX\tY\tZ\Lat\tLon")
    start_time = int(round(time.time()*1000))
    while True:
        time.sleep(dt)
        gps_report = ugps.next()
        if gps_report['class'] == 'TPV':
        	lat = gps_report.lat
        	lon = gps_report.lon
        xyz = gyro.Get_CalOut_Value()
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        delta_t = int(round(time.time()*1000)) - start_time
        print("{:10.0f}, {:7.2f}, {:7.2f}, {:7.2f}, {:10.6f}, {:10.6f}".format(delta_t, x, y, z, lat, lon))
    
except KeyboardInterrupt:
    print('Stoping.')




