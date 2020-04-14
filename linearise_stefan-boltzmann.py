import numpy as np
import matplotlib.pyplot as plt

sigma = 5.67e-8 
vT    = np.linspace(270,300) # [K]
T0    = 288 # linearise around this 
vB    = sigma * vT**4 # black-body radiation
B0    = sigma * T0**4 
vBp   = B0 + 4. * sigma * T0**3 * (vT - T0)

fig, ax = plt.subplots(1,1)
ax.plot(vT,vB,'-k',label='S-B radiation')
ax.plot(vT,vBp,'-r',label='Linearised')
ax.scatter([T0],[B0])
ax.legend()
ax.set_xlabel('Temperature [K]')
ax.set_ylabel('Black-body radiation [W/m2]')
fig.tight_layout()
fig.savefig('linearised_stefan-boltzmann.png',format='png')
