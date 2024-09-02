# define
transmitted_data = 270.833
time_slot_bit = 8
control_slot_bit = 156.25

print("===============A================")
time_duration_bit = 1 / transmitted_data
print(f"The time duration of a bit {time_duration_bit:.4f} ms")

print("================B===============")
time_duration_slot = control_slot_bit * time_duration_bit
print(f"The time duration of slot : {time_duration_slot:.4f} ms")

print("================C===============")
time_duration_frame = time_slot_bit * time_duration_slot
print(f"The time duration of a frame {time_duration_bit:.4f} ms")
# (D) Waiting time for a new frame
print("(D)")
print(
    "A user has to wait 4.615 ms, the arrival time of a new frame for its next transmission."
)


# Define parameters
# trans_data = 270.833  # Transmission data rate in kbps
# each_time_slot_bit = 156.25  # Each time slot in bits
# num_of_time_slot = 8  # Number of time slots

# # (A) Calculate time duration of a bit (Tb)
# time_duration_of_a_bit_Tb = 1 / trans_data
# print("(A)")
# print(f"Time duration of a bit Tb: {time_duration_of_a_bit_Tb:.4f} ms")
# print()

# # (B) Calculate time duration of a slot (Ts)
# time_duration_of_a_slot_Ts = each_time_slot_bit * time_duration_of_a_bit_Tb
# print("(B)")
# print(f"Time duration of a slot Ts: {time_duration_of_a_slot_Ts:.2f} ms")
# print()

# # (C) Calculate time duration of a frame (Tf)
# time_duration_of_a_frame_Tf = time_duration_of_a_slot_Ts * num_of_time_slot
# print("(C)")
# print(f"Time duration of a frame Tf: {time_duration_of_a_frame_Tf:.3f} ms")
# print()

# # (D) Waiting time for a new frame
# print("(D)")
# print(
#     "A user has to wait 4.615 ms, the arrival time of a new frame for its next transmission."
# )
