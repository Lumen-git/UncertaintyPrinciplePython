import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-poster')

x = np.linspace(0, 100, 1500)

# Z changes the amount of waves added together. More waves = more certainty about
# position = less certainty about velocity

z = 2
y = 0
mult = .2

for i in np.arange(0, z, mult):
    y += np.sin(x  * i)

# Don't change y, but Z and the .2 value above can be played with
# 1 and .2 worked well in my tests

y = y ** 2

plt.figure(figsize = (8, 6))
plt.plot(x, y, 'b')
plt.ylabel('Amplitude')
plt.xlabel('Location (x)')
plt.show()
