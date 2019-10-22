import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,2*np.pi,1000)
plt.figure()
plt.plot(t, np.cos(t))
plt.savefig('cos.png')