import numpy as np
import matplotlib.pyplot as plt

def esat(T):
   es = 611.2 * np.exp( (17.67*T) / (T + 243.5) )
   return es

cp = 1012 # J/kg/K
Lv = 2.3e6 # J/kg
Ma = 29 #g/mol
Mw = 18 #g/mol
p  = 100000 #Pa 

gamma = cp/Lv * Ma/Mw #psychrometer constant K-1

fig, ax = plt.subplots(1,2)

vT = np.linspace(0,35,25) #degC
dT = np.linspace(0,10,20)  #T - Tw

e  = np.zeros((vT.shape[0],dT.shape[0]))
rh = np.zeros((vT.shape[0],dT.shape[0]))
for i in range(0,dT.shape[0]):
   es = esat(vT - dT[i]) #es(Tw)
   e[:,i] = es[:] - gamma * p * dT[i]
   rh[:,i] = e[:,i]/es[:] * 100.
   print(e[:,i],gamma * p * dT[i])

rh = np.ma.masked_where( rh < 0, rh )
e  = np.ma.masked_where( e < 0, e )

#for i in range(0,dT.shape[0]):
#   e[:,i] = es[:] 

cf = ax[0].pcolor(dT,vT,rh)
cb = plt.colorbar(cf,ax=ax[0])
ax[0].invert_yaxis()
ax[0].set_xlabel('Td-Tw')
ax[0].set_ylabel('Tdry [degC]')
cb.set_label('RH')

ax[1].plot(vT,e[:,0]/100.,label='dT=0')
ax[1].plot(vT,e[:,10]/100.,label='dT=5')
ax[1].plot(vT,e[:,19]/100.,label='dT=10')
ax[1].set_xlabel('T [degC]')
ax[1].set_ylabel('Vapour pressure [hPa]')
ax[1].legend()

fig.tight_layout()
fig.savefig('psychrometer.png',format='png')
plt.show()

