import time

start_time = time.time()

fault = True  # system is faulted


def fault_isolation():  # method to isolate a fault
    print("Fault detected!")
    time.sleep(2)  # time taken to isolate the fault
    if (fault):
        return True
    else:
        return False


def calculate_weight(priority, load_necessary):  # method to calculate priority of load
    weight = priority * load_necessary
    return weight


def detect_loss(load_present, load_necessary):  # method to calculate needed current to restore
    if fault:
        power_from_dg = abs(load_present - load_necessary)
        return power_from_dg


def form_island(a):  # method helping to form an island
    if bool(a) == True:
        return True


# defining system units(variables)
load_agent1 = ['0001', 'Load at bus 1', 1, 160, 0.1]  # agent ID, its local name, the node it is attached to,
# the load at the node in Amps, the priority of the load (from 0 to 1), higher priority is better
load_agent2 = ['0002', 'Load at bus 2', 2, 100, 0.08]
load_agent3 = ['0003', 'Load at bus 3', 3, 210, 0.06]
dg_agent = ['0011', 'Distributed Generator', 300, None]  # agent ID, its local name, its generation capacity and ID of
# the other DG agents
switch_agent12 = ['1001', 'Switch agent between bus 1 and 2',
                  12,
                  1]  # agent ID, its local name and the node numbers to which it is connected, condition: closed = 1, open = 0
switch_agent23 = ['1002', 'Switch agent between bus 2 and 3', 23, 0]

isFault_isolated = fault_isolation()
if isFault_isolated:
    print("Fault is isolated.")
    weight1 = calculate_weight(load_agent1[3], load_agent1[4])
    print("Weight coefficient of the bus " + str(load_agent1[2]) + " is " + str(weight1) + ".")
    time.sleep(1)  # time to calculate weights
    weight2 = calculate_weight(load_agent2[3], load_agent2[4])
    print("Weight coefficient of the bus " + str(load_agent2[2]) + " is " + str(weight2) + ".")
    time.sleep(1)  # time to calculate weights
    weight3 = calculate_weight(load_agent3[3], load_agent3[4])
    print("Weight coefficient of the bus " + str(load_agent3[2]) + " is " + str(weight3) + ".")
    time.sleep(1)  # time to calculate weights
    weights = [weight1, weight2, weight3]
    weights.sort(reverse=True)

if fault:
    load_agent1.append(16)  # loads after fault between bus 1 and 2
    load_agent2.append(10)
    load_agent3.append(21)
loss1 = detect_loss(load_agent1[3], load_agent1[5])
time.sleep(1)  # ime taken to make complex calculations
print("Needed current at the bus " + str(load_agent1[2]) + " is " + str(loss1) + " A.")
loss2 = detect_loss(load_agent2[3], load_agent2[5])
time.sleep(1)  # ime taken to make complex calculations
print("Needed current at the bus " + str(load_agent2[2]) + " is " + str(loss2) + " A.")
loss3 = detect_loss(load_agent3[3], load_agent3[5])
time.sleep(1)  # ime taken to make complex calculations
print("Needed current at the bus " + str(load_agent3[2]) + " is " + str(loss3) + " A.")
losses = [loss1, loss2, loss3]
power_available = dg_agent[2]
print("Available power at DG is equiavalent of " + str(power_available) + " A.")
for i in range(0, 3):
    if power_available > 0:
        if weights[i] == max(weights):
            if (power_available - losses[i]) > 0:
                power_available = power_available - losses[i]
                weights[i] = 0
time.sleep(1)  # time to calculate distribution
print("Power left at DG is " + str(power_available))

if form_island(weights[0]):
    switch_agent12[3] = 0
    time.sleep(1)  # switching time is set to 1 sec
    print("Switch agent between bus 1 and 2 is opened")
else:
    print("Switch agent between bus 1 and 2 is closed")

if form_island(weights[2]):
    switch_agent23[3] = 0
    time.sleep(1)  # switching time is set to 1 sec
    print("Switch agent between bus 2 and 3 is opened")
else:
    print("Switch agent between bus 2 and 3 is closed")

print("System is succesfully restored! Time taken for restoration is %s seconds ---" % (time.time() - start_time))
