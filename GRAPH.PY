import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
count = 1

def add_data(x=[],y=[]):
    p=input("marks:")
    q=input("names:")
    count=count+1
    x.resize(1,count)
    y.resize(1,count)
    z=np.append(x,p)
    w=np.append(y,q)
    print(z,w)
    return z,w

a = np.array([21,23,54,23,46,85,95,26])
b = np.array(['a','b','c','d','e','f','g','h'])
print(a,b)
plt.scatter(b,a)
plt.plot(b,a,'r','+')
plt.step(b,a)
plt.xlabel("Name")
plt.ylabel("Marks")
plt.legend()
plt.savefig('Students_Grades.pdf')
plt.get_cmap('Spectral')
# for i in range(3):
#     add_data(a,b)
plt.show()
x_data1 = a[:4]-(np.sum(a))/8
y_data1 = [1, 2, 3, 4]

x_data2 = [0.1, 0.2, 0.3, 0.4]
y_data2 = [1, 4, 9, 16]

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(x_data1, y_data1, label='data 1',)
ax2.plot(x_data2, y_data2, label='data 2')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Scale (Bananas)')
ax1.set_title('first data set')
ax1.legend()
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Scale (Bananas)')
ax2.set_title('second data set')
ax2.legend()

plt.show()