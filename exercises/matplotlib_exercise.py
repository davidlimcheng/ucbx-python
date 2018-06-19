import numpy as np
import matplotlib.pyplot as plt

# create an array "a" with 512 points in the range (-2*pi, 2*pi)
a = np.linspace(-np.pi*2, np.pi*2, 512, endpoint=True)

# 'sin' and 'cos' functions have the same number of points (512)
b_sin, c_cos = np.sin(a), np.cos(a)

# plot the results of the two functions above
plt.plot(a, b_sin)
plt.plot(a, c_cos)
plt.show()

# we can create a figure with a specific size and dpi (dots per inch)
plt.figure(figsize=(10,8), dpi=120)

# when two graphics are needed in the same graphic window, we can use 'subplot'
plt.subplot(3, 2, 6)
# this will create an empty plotting space inside the window
# where 'y' is the y-axis, 'x' is the x-axis, and
# 'n' is the number of the window to be created after setting x and y

plt.show()
