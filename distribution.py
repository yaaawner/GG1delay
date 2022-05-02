import random
import sys
from enum import Enum

NUMBER = 50000
TIME_INTERVAL = 1


weibull_0_1_1_list = [{"alpha": 0.15, "beta": 2.0, "statistic": "weibull/weibull_0_1_1/weibull_1_1.csv"},
                      {"alpha": 0.14, "beta": 2.1, "statistic": "weibull/weibull_0_1_1/weibull_1_2.csv"},
                      {"alpha": 0.15, "beta": 1.8, "statistic": "weibull/weibull_0_1_1/weibull_1_3.csv"},
                      {"alpha": 0.16, "beta": 1.5, "statistic": "weibull/weibull_0_1_1/weibull_2_1.csv"},
                      {"alpha": 0.2, "beta": 0.7, "statistic": "weibull/weibull_0_1_1/weibull_2_2.csv"},
                      {"alpha": 0.15, "beta": 0.7, "statistic": "weibull/weibull_0_1_1/weibull_2_3.csv"},
                      {"alpha": 0.11, "beta": 2.0, "statistic": "weibull/weibull_0_1_1/weibull_2_4.csv"}]


class Distribution(Enum):
    POISSON = 1
    PARETO = 2
    WEIBULL = 3
    LOGNORMAL = 4


class Poisson:
    def __init__(self, _lambda):
        self.lambda_p = _lambda


class Pareto:
    def __init__(self, _alpha, _k):
        self.alpha = _alpha
        self.k = _k


class Weibull:
    def __init__(self, _alpha, _beta):
        self.alpha = _alpha
        self.beta = _beta


def pareto(alpha=1.4, k=0.05):
    variable_list = []
    random.seed(1)
    for i in range(0, NUMBER):
        var = random.paretovariate(alpha) * k
        variable_list.append(var)
    return variable_list


def weibull(alpha=0.15, beta=2.0):
    variable_list = []
    #random.seed(1)
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


def convert_to_intensity(variable_list, output_file_name):
    output_file = open(output_file_name, "w")
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
            output_file.write(str(count) + '\n')
            current_time += 1
            while current_time != t // TIME_INTERVAL:
                intensity_list.append(0)
                output_file.write(str(0) + '\n')
                current_time += 1
            count = 1
    intensity_list.append(count)
    output_file.write(str(count) + '\n')
    output_file.close()
    return intensity_list


if __name__ == "__main__":
    for distr in weibull_0_1_1_list:
        convert_to_intensity(weibull(distr["alpha"], distr["beta"]), distr["output"])
