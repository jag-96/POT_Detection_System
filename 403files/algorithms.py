##file input, while(file) search for peaks, based on relative maxiumums

import csv
import numpy as np
import matplotlib.pyplot as plt
print("testing algorithms")

with open('fixed_data.csv') as csvfile:
    data = csv.reader(csvfile,delimiter = ',')
    #for row in data:
     #   print(row)
    data_list = list(csv.reader(csvfile,delimiter = ','))

for row in range(5):
    print(data_list[row])


acc_x_non = np.array(data_list)[:,3]
acc_y = np.array(data_list)[:,4]
acc_z = np.array(data_list)[:,5]

#results = list(map(int, results))
acc_x = list(map(int,acc_x_non))
#acc_x = data_list[:,3]
for row in range(5):
    print(int(acc_x[row]))

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
