class StatsInfo:
    def __init__(self, distribution):
        self.mean = distribution.mean()
        self.std = distribution.std()
        self.scv = (self.std / self.mean) ** 2


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