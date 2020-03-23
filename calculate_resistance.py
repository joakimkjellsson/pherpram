import numpy as np
import matplotlib.pyplot as plt

xI = np.linspace(1,5,20)
xV = np.linspace(1,10,20)
xO = np.zeros((20,20))
dI = 0.2
dV = 0.5
dO = np.zeros((20,20))

for jj in range(0,xV.shape[0]):
   for ji in range(0,xI.shape[0]):
      xO[jj,ji] = xV[jj]/xI[ji]
      dO[jj,ji] = xO[jj,ji] * np.sqrt( (1/xI[ji])**2 * dI**2 + (1/xV[jj])**2 * dV**2 )

fig, ax = plt.subplots(2,1)
cf1 = ax[0].pcolormesh(xI,xV,xO)
cf2 = ax[1].pcolormesh(xI,xV,dO)
cb = plt.colorbar(cf1,ax=ax[0]) ; cb.set_label(r'$\Omega$')
cb = plt.colorbar(cf2,ax=ax[1]) ; cb.set_label(r'$\sigma_\Omega$')
for a in ax:
   a.set_xlabel('Current [A]')
   a.set_ylabel('Voltage [V]')
   a.set_xlim([xI.min(),xI.max()])
   a.set_ylim([xV.min(),xV.max()])
fig.tight_layout()
fig.savefig('viva_la_resistance.jpg',format='jpeg')