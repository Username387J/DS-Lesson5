import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-5,5.1,0.1)
y1=x
y2=x**2
y3=x**3

plt.plot(x,y1,color="red",linestyle="--",linewidth=2,label="Y=X")
plt.plot(x,y2,color="blue",linestyle="-",linewidth=2,label="Y=X**2")
plt.plot(x,y3,color="green",linestyle="-.",linewidth=2,label="Y=X**3")
plt.title("Relationship Between X and Various Y's")
plt.xlabel("X line")
plt.ylabel("Y line")
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
plt.show()
