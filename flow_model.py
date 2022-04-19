from math import fabs


class StatsInfo:
    def __init__(self, variables):
        self.variables = variables
        length = len(self.variables)
        self.mean = sum(self.variables) / length

        accumulate = 0
        for i in range(length):
            accumulate += fabs(self.mean - self.variables[i])
        self.std = accumulate / length
        self.scv = (self.std / self.mean) ** 2

        s = 0
        for var in self.variables:
            s += var ** 2
        self.second_moment = s / length


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