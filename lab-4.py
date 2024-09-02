# An urban area has a population of two million residents. Three competing trunked mobile networks
# (systems A, B, and C) provide cellular service in this area. System A has 394 cells with 19 channels
# each, system B has 98 cells with 57 channels each, and system C has 49 cells, each with 100
# channels. Find the number of users that can be supported at 2% blocking if each user averages two
# calls per hour at an average call duration of three minutes. Assuming that all three trunked systems
# are operated at maximum capacity, compute the percentage market penetration of each cellular
# provider
blocking_probability = 2 / 100
lamda = 2
H = 3 / 60
Au = lamda * H
P = 2000000


# System A
def calculation_all_ans(channel, cell, A,system_name):
    U = A / Au
    subscriber = U * cell
    percentage_market_penetration=(subscriber/P)*100
    print("=============================")
    print(f"System {system_name}")
    print("=============================")
    print(f"Number of users in system {system_name}= {U}")
    print(f"Total number of subscriber in system {system_name} ={subscriber}")
    print(f"Percentage market penetration for {system_name} = {percentage_market_penetration} ")

calculation_all_ans(19,394,12,"A")
calculation_all_ans(57,98,45,"B") 

calculation_all_ans(100,49,88,"C")