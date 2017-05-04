from scipy.io.wavfile import read
import matplotlib.pyplot as plt

input_data = read("fijo.wav")
plt.plot(input_data[1])
plt.ylabel("Value")
plt.xlabel("Time")
plt.show()