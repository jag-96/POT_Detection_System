#testing Data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
#from scipy.signal import butter, lfilter, freqz, lfilter_zi, filtfilt
from scipy import signal

features = ["Quality","Angle","Distance","CorrectedDistance"]
test = pd.read_csv('realtime_lidar_test_v2.csv', sep='\s+',skiprows=2,names = features)#_v2
#X = test.drop()

#print(test.dtypes)

d = []
for i in range(0,len(test.Quality)):
    #print(test.Quality[i])
    d.append(test.Distance[i]*(math.cos(math.radians((test.Angle[i] - 270)))))

e = pd.Series(d)

test["CorrectedDistance"] = e.values

#plt.plot(test.CorrectedDistance)
#plt.show()

"""print(d)
b, a = butter(3,.001)
zi = lfilter_zi(b,a)
z, _ = lfilter(b,a, d, zi=zi*d[0])
z2, _ = lfilter(b,a,z, zi=zi*zi[0])

y = lfilter(b,a,d)"""

n = 50
b = [1.0 / n] * n
a = 1
yy = signal.lfilter(b,a,e)


plt.plot(e)
plt.plot(yy)
plt.show()
