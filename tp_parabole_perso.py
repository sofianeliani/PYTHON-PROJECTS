import time
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,num=100)
y1 =x*x
plt.plot(x, y1,"g--")
plt.show()
time.sleep(0.5)
plt.plot(y1,x)
plt.show()
time.sleep(0.5)
y2 =-(x*x)
plt.plot(x,y2)
plt.show()
time.sleep(0.5)
plt.plot(y2,x)
plt.show()
time.sleep(0.5)
  
