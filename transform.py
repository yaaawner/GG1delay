from generate import weibull


def sum_lambda(lambda_lists):
    # copy lists
    buf_lists = []
    for l_list in lambda_lists:
        buf_lists.append(l_list.copy())

    # calculate max length
    max_length = 0
    for l_list in buf_lists:
        length = len(l_list)
        if length > max_length:
            max_length = length

    # equalise lists
    for l_list in buf_lists:
        for i in range(max_length - len(l_list)):
            l_list.append(0)

    return list(map(sum, zip(*buf_lists)))


def arrival_transform(arrival_lists):
    new_arrival = []
    for i in range(len(arrival_lists[0])):
        s = 0
        for j in range(len(arrival_lists)):
            s += 1 / arrival_lists[j][i]
        new_arrival.append(1/s)
    return new_arrival


arr1 = weibull()
arr2 = weibull(alpha=0.10)
print(arr1)
print(arr2)

print(arrival_transform([arr1, arr2]))