import numpy as np
import matplotlib.pyplot as plt

S = 1360.
alpha = 0.5
nu = 1.5e-5 
k  = 2.5e-2
xw = np.array([3,5,8]) 
xd = np.linspace(0,5,20) * 1e-3

fig, ax = plt.subplots(1,1)
dT = np.zeros((xw.shape[0],xd.shape[0]))
for i in range(0,xw.shape[0]):
   dT[i,:] = S * (1-alpha) / (0.34 * k) * 0.25 * (nu/xw[i])**0.6 * xd[:]**0.4 
   ax.plot(xd*1e3,dT[i,:],label="w=%d m/s" % (xw[i],))

ax.set_xlabel('Thermometer diameter [mm]')
ax.set_ylabel('Temperature error [K]')
ax.legend()
fig.tight_layout()
fig.savefig('radiation_error_radiosonde.png', format='png',dpi=600)
plt.show()
