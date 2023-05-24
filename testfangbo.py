import xlrd
import numpy as np
from matplotlib import pyplot as plt



# y = np.array(a,dtype= np.float32)
f = 10
Ts = 1.0/f
t = np.arange(-5,5,Ts)

xx = np.zeros_like(t)
xx[40:60]=1
r1 = np.fft.fft(xx)
freq = np.fft.fftfreq(xx.size,Ts)
# freq = np.linspace(0,len(y)/f,len(y))
mag = abs(r1)
plt.subplot(121)
plt.title("original")
plt.scatter(t,xx)

plt.subplot(122)
plt.title("fangbo")
plt.plot(freq,mag)
# plt.figure(figsize=(50,50))
plt.savefig("./new/imagetest.png")