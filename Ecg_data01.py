import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd

frequency = 360
df = pd.read_csv("ecg.csv")
x=df.iloc[:, 0].values
t = np.arange(x.size) / frequency
plt.plot(t,x)
plt.xlim(9,9.6)
#plt.ylim(-1, 1.5)
plt.show()


