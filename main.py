from GG1delay.generate import weibull
from GG1delay.flow_model import *
from GG1delay.calculate_waiting_time import *

beta_list_arrival = [2.0, 1.5, 0.7]
beta_list_service = [2.1, 1.3, 0.6]

arrival_flows = []
#priority = 1
for beta in beta_list_arrival:
    var_list = weibull(beta=beta)
    arrival_flows.append(var_list)

service_flows = []
for beta in beta_list_service:
    var_list = weibull(alpha=0.03, beta=beta)
    print(var_list)
    service_flows.append(var_list)

priority_flows = []
for i in range(1, 4):
    flow = Flow(StatsInfo(arrival_flows[i-1]), StatsInfo(service_flows[i-1]), i)
    priority_flows.append(flow)

#print(priority_waiting_time(priority_flows, 1))
#print(priority_waiting_time(priority_flows, 2))
print(priority_waiting_time(priority_flows, 1))
print(mg1(priority_flows, 1))

arr1 = weibull()
print(kingman(priority_flows[0]))

