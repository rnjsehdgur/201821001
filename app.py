import streamlit as st
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

st.title("201821001 권동혁")
# 전달함수 계수 입력
numerator = st.text_input("Numerator coefficients (separated by commas)", "100")
denominator = st.text_input("Denominator coefficients (separated by commas)", "1, 5, 6")

# 전달함수 계수 파싱
num = [float(coeff.strip()) for coeff in numerator.split(",")]
den = [float(coeff.strip()) for coeff in denominator.split(",")]

# 폐루프 전달함수 계산
L = signal.TransferFunction(num, den)

# Unit step 입력의 응답곡선 계산
t, y = signal.step(L)

# 주파수 응답의 보드선도 계산
w, mag, phase = signal.bode(L)

# 그래프 그리기
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# 응답곡선 그리기
axs[0].plot(t, y)
axs[0].set(xlabel='Time', ylabel='Output', title='Step Response')

# 보드선도 그리기
axs[1].semilogx(w, mag)
axs[1].set(xlabel='Frequency [rad/s]', ylabel='Magnitude [dB]', title='Bode Diagram')

# 그래프 출력
st.pyplot(fig)
