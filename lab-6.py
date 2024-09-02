# define parameters
carrier_frequency = 900 * 10**6  # Carrier frequency in Hz
c = 9 * 10**8  # speed of light
waveLength = c / carrier_frequency
vehicle_speed = 70 * (1000 / (60 * 60))
# case of vehicle A
print("Question Number A")
print("The vehicle is moving directly toward the transmitter : ")
The_received_frequency_of_A = carrier_frequency + (vehicle_speed / waveLength) / 1e6
print(f"The frequency is : {The_received_frequency_of_A}")

# case of vehicle A
print("Question Number B")
print('The vehicle is moving directly away from the transmitter: ')
The_received_frequency_of_B_is = (carrier_frequency - (vehicle_speed / waveLength)) / 1e6
print(f'The received frequency is: {The_received_frequency_of_B_is} MHz')
print()
