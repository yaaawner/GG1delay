import random
import sys

NUMBER = 100
TIME_INTERVAL = 1


def pareto(alpha=1.4, k=0.05):
    #output_file = open(argv[1], "w")
    t = 0.0
    count = 0
    current_time = 0
    random.seed(1)
    for i in range(0, NUMBER):
        ti = random.paretovariate(alpha) * k
        #print(ti)
        t += ti
        #print(t)
        if t // TIME_INTERVAL == current_time:
            count += 1
        else:
            #output_file.write(str(count) + '\n')
            print(count)
            current_time += 1
            while current_time != t // TIME_INTERVAL:
                #output_file.write(str(0) + '\n')
                print(0)
                current_time += 1
            count = 1
    print(count)
#output_file.write(str(count) + '\n')
#output_file.close()


def weibull(alpha=0.15, beta=2):
    # output_file = open(argv[1], "w")
    t = 0.0
    count = 0
    current_time = 0
    random.seed(1)
    for i in range(0, NUMBER):
        ti = random.weibullvariate(alpha, beta)
        # print(ti)
        t += ti
        # print(t)
        if t // TIME_INTERVAL == current_time:
            count += 1
        else:
            # output_file.write(str(count) + '\n')
            print(count)
            current_time += 1
            while current_time != t // TIME_INTERVAL:
                # output_file.write(str(0) + '\n')
                print(0)
                current_time += 1
            count = 1
    print(count)


def lognormal(mu=0.99, sigma=0.005):
    # output_file = open(argv[1], "w")
    t = 0.0
    count = 0
    current_time = 0
    random.seed(1)
    for i in range(0, NUMBER):
        ti = random.lognormvariate(mu, sigma)
        print(ti)
        t += ti
        # print(t)
        if t // TIME_INTERVAL == current_time:
            count += 1
        else:
            # output_file.write(str(count) + '\n')
            print(count)
            current_time += 1
            while current_time != t // TIME_INTERVAL:
                # output_file.write(str(0) + '\n')
                print(0)
                current_time += 1
            count = 1
    print(count)


print("pareto")
pareto()

print("weibull")
weibull()

#print("lognormal")
#lognormal()
