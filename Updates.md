# Updates #

**week of 11/11**
- Group Work
  - LiDAR, GPS, & GYRO all run concurrently through a multithreaded process.
  - LiDAR runs at 5Hz, GPS runs at 1 Hz, GYRO runs at 500 Hz. This will be our final frequency implementations.
  - The SOFT Detection Algorithm has been multithreaded into our main system, however we encountered slight errors. If this does not resolve by 11/15, we will run the detection algorithm all together after a full day of driving data, or we will send all the data to the database and do the algorithm on the webpage. Both of these implementations are possible and availabale.
  - All data can be sent to the MySQL server on WiFi, with no issues.
  - SOFT Detection algorithm has been tested and works well on & off the Pi, HARD detection (filters included) may be added into the webpage if it comes to that.

**week of 10/7**
- Group Work
  - Continued to get LiDAR & Gyro Data
  - Went to a location with known potholes (may have been too many)
  - Went to a location with a Speed-Bump & tested.
  - Next steps is configuring GPS with sensor array & testing
- Andy
  - Continued testing of GPS with sensor array
  - Next Steps: Looking back into Accelerometer data as well as the GYRO data.
  - Next Steps: Connect Pi to MYSQL server and send data to the proper DB.
- George
  - Continued test of new filters for LiDAR.
  - Encountered issues with LiDAR data & GyroZ, hoping to solve by 10/16

**day of 10/2**
- Group work
  - We've successfully connected the sensor array & LiDAR onto the casing and zip-tied the casing onto the vehicle. 
  - We successfully gathered both LiDAR & Gyro data. 
  - Next steps is gathering LiDAR, Gyro, & GPS data on visable Potholes & Speed bumps
- George 
  - Working and testing new filters & algorithms on the LiDAR data to attempt to detect road disturbances. 

**week of 9/30**
- Group Work
  - We've reprinted a new casing and we are planning on weight testing on Wednesday during lab, because we will need to drive and test we will be unavailable during lab.
  - We hope that we can zip-tie our sensor array and zip-tie our POTHOLE Detector onto the vehicle to get any data at all. We also plan to do this on Wednesday after our weight tests.
  - After we get data, we will be able to continue writing our algorithms to detect a pothole in the road, however until we get live data we won't be able to do anything else and we will remain behind.




**week of 9/23**
- Brennan
  - Changing appearance on the webpage
  - Worked on how markers are added to webpage
- Andy
  - Connected Pi connected to AWS DB from Pi. 
  - Working on sending data to DB from Pi.
  - Still messing with GPS, planning on asking Andrew about antennas.
- George
  - Realized issues within filtering through small sets of data.
  - Attempting to existing filter through small sets of data.
  - Running algorithm on Pi testing time it takes to compute.
- Group Work
  - Creating new Prototype for weight testing & data gathering. Hope to have printed by Friday 9/27
  
  
  
  
