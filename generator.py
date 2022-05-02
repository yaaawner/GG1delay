


class Flow:
    def __init__(self, number_, alpha_, beta_, path_):
        self.number = number_        # номер потока
        self.alpha = alpha_      # интенсивность почтупления пакетов (параметр Пуассона)
        self.beta = beta_
        self.path = path_            # список коммутатор, через которые проходит поток

'''
def generate_general(slices, event_time, _weibull):
    print("Start generate")
    for key in slices.keys():
        sls = slices[key]
        packet_count = 1
        for flow in sls.flows_list:
            t = random.weibullvariate(flow.alpha, flow.beta)
            while t < T:
                # добавляем шейпинг
                if (packet_count * sls.packet_size) / t > sls.bandwidth:
                    t += ((packet_count * sls.packet_size / sls.bandwidth) - t)
                # print("sls_number", sls.number, "flow =", flow.path[0], "time = ", t)
                arrival_packet = Packet(sls.packet_size, sls.number, t, flow)
                # добавляем событие в общий список событий
                event_time.add_event(Event(State.ARRIVAL, t, arrival_packet, flow.path[0]))
                # генерируем экспоненциальное значение временного интервала между событиями
                t += random.weibullvariate(_weibull.alpha, _weibull.beta)
    print("Finish generate")
'''
