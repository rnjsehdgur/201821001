import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import streamlit as st 
 
num = [100]

den = [2, 3, 0]

L = signal.TransferFunction(num, den)

t, y = signal.step(L)

w, mag, phase = signal.bode(L)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')

plt.subplot(1, 2, 2)
plt.semilogx(w, mag)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Bode Diagram')

plt.tight_layout()
st.pyplot(fig)
