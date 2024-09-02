# Find the Fraunhofer distance for an antenna with maximum dimension of 1 m and operating
# frequency of 900 MHz . If antennas have unity gain, calculate the path loss.

import math

# define parameters
c = 3 * 10**8  # velocity of light in m/s
f = 900 * 10**6  # frequency in Hz
D = 1  # Distance in meters
# calculate the wave length(lambda)
lamda = c / f
# Calculate Fraunhofer distance (df)
df = 2 * (D**2) / lamda
# calculate the path loss
pl = -10 * math.log10((lamda**2) / (((4 * math.pi) ** 2) * (df**2)))
print(f"Operating frequency :{lamda:.2f} m")
print(f"Fraunhofer distance, df = {df:.2f} m")
print(f"Path Loss, PL(dB) = {pl:.2f} dB")
