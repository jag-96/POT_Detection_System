##file input, while(file) search for peaks, based on relative maxiumums

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import scipy.interpolate as spi
print("testing GYRO algorithms")

outliers = []
def detect_outlier(data_1):
    outliers = []
    print("FUNCTION")
    mean_1 = np.mean(data_1)
    std_1 = np.std(data_1)
    threshold = std_1 #6
    
    for y in data_1:
        z_score = (y - mean_1)/std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
            print("STd = ", std_1)
            print("threshold = ", threshold)
            print("zscore ", z_score)
        else: 
            outliers.append(0)
    
    return outliers

def detect_pothole(data_0,data_1):
    ##data_0 is previous 100 pts.
    ##data_1 is current 100 pts.

with open('driving_test4.csv') as csvfile:
    data = csv.reader(csvfile,delimiter = ',')
    #for row in data:
     #   print(row)
    data_list = list(csv.reader(csvfile,delimiter = ','))

#for row in range(5):
    #print(data_list[row])


gyro_x_non = np.array(data_list)[:,2]
gyro_x = []
averages = []
avg = 0
for row in range(10000):#10000
    gyro_x.append(float(gyro_x_non[row]))
    
#print(range(len(gyro_x)))
#detected = detect_outlier(gyro_x)

"""you need to, 
    first split the information, into a buffer, 
    every 10 is inputted into the "funciton" we created to find "outliers".
    and then output a list, 
    and append said list to overall list.
    plot overall list
"""
##startfor
buffer = []
detectedbuffer = []

#fuck = detect_outlier(gyro_x[3000:5000])

for i in range(len(gyro_x)):
    buffer.append(gyro_x[i])
    if i < 250 and i > 0:
        detectedbuffer.append(0)
    if i % 250 == 0 and i > 0:
            outlierbuffer = detect_outlier(buffer)
            detectedbuffer.extend(outlierbuffer)
            buffer = []
          
##endfor

print(len(detectedbuffer))
#print(detected)
plt.figure(1)
#plt.plot(detected)
#plt.figure(2)
plt.plot(gyro_x)
 #plt.plot(detectedbuffer)
plt.show()





"""plt.plot(gyro_x)
plt.plot(averages)
plt.show()"""


    
#print(gyro_x[row])
"""gyro_y = np.array(data_list)[:,1]
gyro_z = np.array(data_list)[:,2]

#results = list(map(int, results))
acc_x = list(map(float,gyro_x_non))
#acc_x = data_list[:,3]
for row in range(5):
    print(float(acc_x[row]))

##while buffernum < 19, (add too buffernum)
#find average of current values. compare next.
#buffernum = 0


detected = [[]]
q = [0,0]

plt.plot(acc_x)
plt.show()

for n in range(5000):#acc_x.size
    if n % 10 == 0:
        av = 0
        for i in range(10):
            av = av + acc_x[i+n]
        av = av/10

        for j in range(10):
            if abs(acc_x[n+j] - av) > 3000:
                print('subtraction = ') 
                print(abs(acc_x[n+j] - av))
                del q
                q = []
                #q[0] = n
                #q[1] = acc_x
                q.append(n+j)
                q.append(acc_x[n+j])
                q.append(av)
                #q = list(acc_x,n)
                print(q)
                detected.append(q)
print(detected)
 """