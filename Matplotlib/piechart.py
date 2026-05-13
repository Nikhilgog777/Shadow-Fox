from matplotlib import pyplot as plt
import numpy as np
time = [1, 2, 3, 4, 5]
colors = ['red', 'blue', 'green', 'yellow', 'cyan']
work = ["Sleeping", "Eating", "Working", "Playing", "Others"]
fig = plt.figure(figsize = (4,4))
plt.pie(time, labels=work, wedgeprops={"edgecolor":"black","linewidth":1}, colors=colors)
plt.title("My Daily Activities")
plt.show()