import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy import stats

def systemofequations(t, S, eta, w, wo):
        c1, c2, c3 = S
        return [eta*w**2*c2*np.sin(wo*t),-eta*w**2*c1*np.sin(wo*t),0]

#intital conditions here
print('Insert your Intital Conditions')
x0 = int(input('Define Your X0 Value: '))
y0 = int(input('Define Your Y0 Value: '))
z0 = int(input('Define Your Z0 Value: '))

#Parameters
print('Insert your Parameters(lambda,w,wo)')
eta = float(input('Enter \u03B7 value: '))
w = float(input('Enter Frequency Here: '))
wo = float(input('Enter Resonance Here: '))

#Time Conditions
t0 = int(input('Insert Your Starting Time: '))
tf = int(input('Insert Your Final Time: '))

#Number of Samples
N = int(input('Insert The Number of Samples from 100 - 100000 (N): '))

#solution to the system of equations
fullsol = integrate.solve_ivp(systemofequations,[t0,tf], [x0,y0,z0],
args=(eta,w,wo),t_eval=np.linspace(t0,tf,N), dense_output=True, rtol = 1E-10)

#graph of y(t)
plt.plot(fullsol.t, fullsol.y[1,:],'-')
plt.xlabel('$t$')
plt.ylabel('$C1(t)$')
plt.legend(['y'])
plt.title('C2 Vs t  \u03B7 = %s,w = %s,wo = %s'%(eta,w,wo))
plt.savefig(r'C:\Users\thega\Desktop\Python General Scripts\C2Vst.png')
plt.show()
plt.close()

#Additonal Part
plt.plot(fullsol.y[0,:], fullsol.y[1,:],'-')
plt.xlabel('$C1(t)$')
plt.ylabel('$C2(t)$')
plt.title('C2(t) vs C1(t), for parameters \u03B7 = %s,w = %s,w0 = %s'%(eta,w,wo))
plt.savefig(r'C:\Users\thega\Desktop\Python General Scripts\C2vsC1.png')
plt.show()
