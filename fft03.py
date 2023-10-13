import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt # library for plotting
#from signalgen import sine_wave # import the function

f = 10 #frequency = 10 Hz
overSampRate = 30 #oversammpling rate
fs = f*overSampRate #sampling frequency
phase = 1/3*np.pi #phase shift in radians
nCyl = 5 # desired number of cycles of the sine wave

(t,x) = np.sin(f,overSampRate) #function call
NFFT=1024 #NFFT-point DFT  
X=fft(x,NFFT) #compute DFT using FFT     

fig2, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
   
nVals=np.arange(start = 0,stop = NFFT)/NFFT #Normalized DFT Sample points         
ax.plot(nVals,np.abs(X))     
ax.set_title('Double Sided FFT - without FFTShift')        
ax.set_xlabel('Normalized Frequency')
ax.set_ylabel('DFT Values')
fig2.show()

