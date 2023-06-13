import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import streamlit as st 
 
#전달함수 계수
num = [100]

den = [2, 3, 0]

#폐루프 전달함수 계산
L = signal.TransferFunction(num, den)

#Unit step 입력의 응답곡선 계산
t, y = signal.step(L)

#주파수 응답의 보드선도 계산
w, mag, phase = signal.bode(L)

#응답곡선 그리기
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')

#보드선도 그리기
plt.subplot(1, 2, 2)
plt.semilogx(w, mag)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Bode Diagram')

plt.tight_layout()
st.pyplot(fig)
