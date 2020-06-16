import numpy as np
import matplotlib.pyplot as plt

H0 = 30 # radar height, m
theta = np.arange(0,7,1) # radar angle in degrees
re = 6371e3 # Earth radius
re_prime = 4.0/3.0 * re
r = np.linspace(0,250,250) * 1e3 # distance in meter

fig,ax=plt.subplots(1,1)
for angle in theta:
   H = np.sqrt( r**2 + re_prime**2 + 2.0 * r * re_prime * np.sin(angle * np.pi/180.) ) - re_prime + H0
   ax.plot(r/1000.,H/1000.,label='%d deg' % (angle,))
   if angle == 0:
      H = np.sqrt( r**2 + re**2 + 2.0 * r * re * np.sin(angle * np.pi/180.) ) - re + H0
      ax.plot(r/1000.,H/1000.,label='%d deg (no refr)' % (angle,))

ax.legend()
ax.set_ylim([0,5])
ax.set_xlabel('Distance [km]')
ax.set_ylabel('Height [km]')
fig.savefig('radar_height.png',format='png',dpi=600)
plt.show()
