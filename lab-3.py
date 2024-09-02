#  How many users can be supported for 0.5% blocking probability for the following
# number of trunked channels in a blocked calls cleared system? (a) 1, (b) 5, (c) 10, (d) 20,
# (e) 100. Assume each user generates 0.1 Erlangs of traffic.
gos = 0.5 / 100
Au = 0.1
# from Erlang B table
A = [0.005, 1.13, 3.96, 11.1, 80.9]
e = [1, 5, 10, 20, 100]
# Given blocking probability
print("Blocking Probability : ", gos)
# traffic intensity per user
print("Traffic intensity per user ", Au)

# Calculate number of users
# U = [a / Au for a in A]
# u = [round(u_val) for u_val in U]
U = []
for a in A:
    U.append(a / Au)
u = []
for u_val in A:
    u.append(round(u_val))
print("Number of users ")
print(u)
