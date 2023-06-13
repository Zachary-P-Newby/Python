import pandas as pd, matplotlib as mpl, numpy as np
import random
import matplotlib.pyplot as plt

x_1 = np.array(range(0,random.randint(0,8)))
print(x_1)
y_1 = x_1 + 2** x_1
plt.plot(x_1,y_1)

plt.show()