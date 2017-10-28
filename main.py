import math
import matplotlib.pyplot as plt
import numpy as np

sample = 1000
t = np.arange(sample)

#t = None
#t = [0,1,2,3,4,5]

# Define Carrier Frequency(f_c)
f_c = 10000000

# Carrier Signal Amplitude
A_c = 12

# Carrier Signal
c_s = A_c*np.cos(2*3.14*f_c*t)

# Define Message Signal
f_m = 5000

# Message Signal Amplitude
A_m = 2

# Message Signal m(t)
m_t = A_m*np.sin(2*3.14*f_m*t)

# Message Signal m(t) for plotting
sample_m = 100
t_m = np.arange(sample_m)
m_t_m = A_m*np.sin(2*3.14*f_m*t_m)
plt.subplot(3,1,1)
plt.title('Message Signal')
plt.ylabel('m(t)')
plt.plot(t_m,m_t_m)


# Non-Linear Device Constants
A1 = 0.2
A2 = 0.3


#for xe,ye in zip(t,A1*A_c*(1+(2*A2*A_m*math.sin(2*3.14*f_m*t))/A1)*math.cos(2*3.14*f_c*t)):
#	plt.scatter([xe] * len(ye),ye)

#for t in xrange(100):
	#output = A1*A_c*(1+(2*A2*A_m*math.sin(2*3.14*f_m*t))/A1)*math.cos(2*3.14*f_c*t)
	#test = t*t

#output = A1*A_c*(1+(2*A2*A_m*np.sin(2*np.pi*f_m*t))/A1)*np.cos(2*np.pi*f_c*t)
output = A1*(1+(2*A2*m_t)/A1) * c_s
plt.subplot(3,1,2)
plt.title('Modulated SIgnal')
plt.ylabel('s(t)')
plt.plot(t,output)



# Demodulation Part

sample_dm = 100
t_dm = np.arange(sample_dm)

demodulated_output = A2*A_c*A_c*((2*A2)/A1)*m_t_m
plt.subplot(3,1,3)
plt.title('Demodulated Signal')
plt.ylabel('m(t)')
plt.plot(t_m,demodulated_output)
plt.show()
