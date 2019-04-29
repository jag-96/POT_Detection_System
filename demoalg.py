##file input, while(file) search for peaks, based on relative maxiumums

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import scipy.interpolate as spi
import pymysql 

#def findpotholes:

peaks = []
def detect_peaks(data_1):
    absdata = []
    for i in data_1:
        absdata.append(abs(i))
    found = False
    peaks = []
    for y in range(len(absdata)):
        if y == 0 or y == len(absdata)-1 or found == True:
            perpoint = []
            perpoint.append(0)
            perpoint.append("no available gps location")
            peaks.append(perpoint)
            #print(y)      
        else:
            perpoint = []
            if ((absdata[y] - absdata[y+1] > 15) or (absdata[y] - absdata[y-1] > 15) and found == False): 
                perpoint.append(data_1[y])
                #here we can append the GPS location in LAT | LON
                latit = 0
                lotit = 0
                perpoint.append(latit)
                perpoint.append(lotit)
                #peaks.append(data_1[y])
                peaks.append(perpoint)
                found = True
            else:
                perpoint = []
                perpoint.append(0)
                #here we can append the GPS location in LAT | LON
                perpoint.append("no available gps location")
                peaks.append(perpoint)
                #peaks.append(0)
            #print("B")

    return peaks


def detect_peaks_output(data_1):
    absdata = []
    for i in data_1:
        absdata.append(abs(i))
    found = False
    peaks2 = []
    for y in range(len(absdata)):
        if y == 0 or y == len(absdata)-1 or found == True:
            peaks2.append(0)
            #print(y)      
        else:
            #perpoint = []if ((absdata[y] - absdata[y+1] > 15) or (absdata[y] - absdata[y-1] > 15)): 
            #((data_1[y] - data_1[y+1] < -15) or (data_1[y] - data_1[y-1] < -15) ): 
            if ((absdata[y] - absdata[y+1] > 15) or (absdata[y] - absdata[y-1] > 15) and found == False): 
                peaks2.append(100)
                found = True
            else:
                peaks2.append(0)
                
    #print("length of peaks is: ", len(peaks))
    return peaks2


def insert_into_db(full_list):
    #the full list inserted should be the of peaks as well as GPS locations. the peaks list should be either 0's or the "peaks".
    l2 = []
    for l in full_list:
        if l[0] != 0:
            l2.append(l)

    #print(l2)

    con = pymysql.connect('127.0.0.1','root','pothole','test_db',local_infile=True) #:3306
    
    with con:
        cur = con.cursor()
        cur.execute("USE test_db;")
        for sub in l2:
            print(sub)
            cur.execute("INSERT INTO demotable (gyro,gpsLAT,gpsLON) VALUES (%s,%s,%s);",(sub[0],sub[1],sub[2]))
  

    
        


with open('driving_test4.csv') as csvfile:
    data = csv.reader(csvfile,delimiter = ',')
    #for row in data:
     #   print(row)
    data_list = list(csv.reader(csvfile,delimiter = ','))


gyro_x_non = np.array(data_list)[:,2]
gyro_x = []
averages = []
avg = 0
for row in range(10000):#10000
    gyro_x.append(float(gyro_x_non[row]))
    
##startfor
buffer = []
detectedbuffer = []
plotholes = []
outlierbuffer = []
detectrange = 40
for i in range(len(gyro_x)):
    buffer.append(gyro_x[i])
    if i < detectrange and i >= 0:
        inlist = []
        inlist.append(0)
        inlist.append("false location")
        detectedbuffer.append(inlist)
        plotholes.append(0)
        #detectedbuffer.append(0)
    if i % detectrange == 0 and i > 0:
        outlierbuffer = detect_peaks(buffer)
        detectedbuffer.extend(outlierbuffer)
        outlierbuffer = detect_peaks_output(buffer)
        plotholes.extend(outlierbuffer)
        #print("current index: ", i)
        buffer = []        
##endfor


insert_into_db(detectedbuffer)

print(len(gyro_x))
print(len(detectedbuffer))
plt.plot(gyro_x)
plt.plot(plotholes)
plt.show()
