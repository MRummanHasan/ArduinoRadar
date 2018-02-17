import serial
import numpy as np
import matplotlib.pyplot as plt
ser = serial.Serial ('/dev/ttyUSB0', 9600)
angle=(np.arange(0,50,1))
num=[]
tab_1=angle.tolist()
tab_2=[]
i=0
while (i<=50):
    a=ser.readline()
    print (a)
    a=a[0]
    num.append(int(a))
    i=i+1
num=[-x for x in num]
for l in range (0, 50):
    tab_2.append(num[l])
tab_1=np.array(tab_1)
tab_2=np.array(tab_2)
plt.plot(tab_1,tab_2)
plt.show()
