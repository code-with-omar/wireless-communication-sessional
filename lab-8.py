Am_signal_power = 400  # transmitted signal with 400kw power
modulated_depth = 0.75  # modulated dept
# calculate the carrier power
carrier_power_pc = Am_signal_power / (1 + (modulated_depth**2) / 2)
print(f"Carrier power Pc: {carrier_power_pc:.2f} KW")
# Total power in the carrier
print("===========A==========")
total_power = (carrier_power_pc / Am_signal_power) * 100
print(f"Total power i the carrier is : {total_power:.3f}")
print("===========B============")
power_of_each_side_band = (Am_signal_power - carrier_power_pc) * 0.5

print(f"power in each sideband : {power_of_each_side_band: .2f} Kw")

print("===========C==============")
percentage_power_saving = (1 - (power_of_each_side_band / Am_signal_power)) * 100
print(f"Percentage power saving: {percentage_power_saving:.2f}%")
