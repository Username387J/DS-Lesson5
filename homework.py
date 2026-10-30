import matplotlib.pyplot as plt
import numpy as np

m=float(input("Enter your slope:"))
c=float(input("Enter your y-intercept:"))


x=np.arange(-20,20.1,0.1)
y1=m*x+c
y2 = x*0
plt.plot(x,y2,color="black",linestyle="-",linewidth=1)
plt.plot(y2,x,color="black",linestyle="-",linewidth=1)
plt.plot(x,y1,color="black",linestyle="-.",linewidth=2,label="Y=MX+C")
plt.title("Dynamic Linear Equation Plotter")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.legend()
plt.show()
