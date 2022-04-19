from math import fabs


class StatsInfo:
    def __init__(self, distribution):
        self.mean = distribution.mean()
        self.std = distribution.std()
        self.scv = (self.std / self.mean) ** 2
        self.second_moment = distribution.second_moment()


class Flow:
    def __init__(self, arrival, service, priority=1, weight=1.0):
        self.arrival = arrival
        self.service = service
        self.priority = priority
        self.weight = weight
        self.lambda_a = 1 / arrival.mean
        self.mu = 1 / service.mean
        self.ro = self.lambda_a / self.mu

    def __str__(self):
        return str(self.priority)


class Distribution:
    def __init__(self, var_list):
        self.variables = var_list

    def mean(self):
        return sum(self.variables)/len(self.variables)

    def std(self):
        mean = self.mean()
        count = 0
        accumulate = 0
        for var in self.variables:
            count += 1
            accumulate += fabs(mean-var)
        return accumulate / count

    def second_moment(self):
        count = 0
        sum = 0
        for var in self.variables:
            sum += var ** 2
            count += 1
        return sum / count
