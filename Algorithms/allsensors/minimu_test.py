from L3GD20 import L3GD20
import time
import smbus

# Communication object
gyro = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

try:
    # Preconfiguration
    gyro.Set_PowerMode("Normal")
    gyro.Set_FullScale_Value("250dps")
    gyro.Set_AxisX_Enabled(True)
    gyro.Set_AxisY_Enabled(True)
    gyro.Set_AxisZ_Enabled(True)
    #gyro.Set_DataRateAndBandwidth(95, 12.5)
    #gyro.Set_FifoMode_Value("Bypass")

    gyro.Init()
    gyro.Calibrate()



    # Read values loop
    starttime = time.time()         # this is our start time
    t = 0
    x = 0
    y = 0
    z = 0
    dt = 0.05    #readings at 10Hz
    
    print("X\tY\tZ")
    while True:
        time.sleep(dt)
        t = time.time() - starttime #dont need now, might later
        xyz = gyro.Get_CalOut_Value()
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))
    
except KeyboardInterrupt:
    print('Stoping.')




