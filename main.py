import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
hours = [1, 2, 1.5, 3, 2.5]

plt.plot(days,hours,color="red",marker="o",linestyle="--",linewidth=3,label="Study")
plt.title("Study Hours")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.show()