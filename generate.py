import random
import sys

NUMBER = 100
TIME_INTERVAL = 1


def pareto(alpha=1.4, k=0.05):
    variable_list = []
    random.seed(1)
    for i in range(0, NUMBER):
        var = random.paretovariate(alpha) * k
        variable_list.append(var)
    return variable_list


def weibull(alpha=0.15, beta=2.0):
    variable_list = []
    random.seed(1)
    for i in range(0, NUMBER):
        var = random.weibullvariate(alpha, beta)
        variable_list.append(var)
    return variable_list


def lognormal(mu=0.99, sigma=0.005):
    variable_list = []
    random.seed(1)
    for i in range(0, NUMBER):
        var = random.lognormvariate(mu, sigma)
        variable_list.append(var)
    return variable_list


def convert_to_intensity(variable_list):
    intensity_list = []
    t = 0.0
    count = 0
    current_time = 0
    for var in variable_list:
        t += var
        if t // TIME_INTERVAL == current_time:
            count += 1
        else:
            intensity_list.append(count)
            current_time += 1
            while current_time != t // TIME_INTERVAL:
                intensity_list.append(0)
                current_time += 1
            count = 1
    intensity_list.append(count)



#print("pareto")
#pareto()

# print("weibull beta=2")
# print(weibull())

#print("weibull beta=1.5")
#print(weibull(beta=1.5))

#print("lognormal")
#lognormal()
