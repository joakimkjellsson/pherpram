import numpy as np
import matplotlib.pyplot as plt

p0 = 101325 #Pa
T0 = 99.97 + 273.15 #K
Rd = 287 #J/K/kg
Lv = 2257000 #J/kg

# Calculate boiling point from pressure
vp  = np.linspace(20000,100000,10)
vTb = 1./ (1.0/T0 - Rd * np.log(vp/p0) / Lv)

# Calculate pressure from boiling point
vT  = np.linspace(50,100,10) + 273.15
vpb = p0 * np.exp( Lv/Rd * (1.0/T0 - 1.0/vT) )

fig, ax = plt.subplots(1,1)
ax.scatter(vTb - 273.15, vp/100., c='k')
ax.scatter(vT - 273.15, vpb/100., c='r')
ax.set_xlabel('Boiling point [degC]')
ax.set_ylabel('Pressure [hPa]')
ax.invert_yaxis()
fig.tight_layout()
fig.savefig('boiling-point.png',format='png')