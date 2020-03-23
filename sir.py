import matplotlib.pyplot as plt


def sir(s0, i0, r0, alpha, beta, t):
    """
    Calculates SIR model for t weeks

    :param s0:(int) starting number of susceptible
    :param i0:(int) starting number of infected
    :param r0:(int) starting number of recovered
    :param alpha: (float) infection rate
    :param beta: (float) recovery rate
    :param t: (int) timespan

    :returns susceptible: (list) numbers of susceptible
    :returns infected:(list) numbers of infected
    :returns recovered:(list) numbers of recovered
    :returns t: (int) param t + 1
    """

    susceptible = [s0]
    infected = [i0]
    recovered = [r0]
    for _ in range(t):
        s = s0 - alpha * s0 * i0
        i = i0 + alpha * s0 * i0 - beta * i0
        r = r0 + beta * i0
        susceptible.append(s)
        infected.append(i)
        recovered.append(r)
        s0 = s
        i0 = i
        r0 = r
    return susceptible, infected, recovered, t + 1


def dif(lst):
    '''
    Calculates the diffrence in the list by lopping through the first and second time stample.
    :param lst: (list)
    :returns lst2: (list, len lst-1)
    '''
    lst2 = []
    for i in range(len(lst) - 1):
        lst2.append(lst[i + 1] - lst[i])
    return lst2


def draw_sirmodel(susceptible, infected, recovered, t, ):
    """
    Plots the SIR-model over t weeks

    :param susceptible: (list, len t) mubers of susceptible
    :param infected: (list, len t) mubers of infected
    :param recovered: (list, len t) mubers of recovered
    :param t:

    """
    time = [i for i in range(t)]

    fig, axs = plt.subplots(2)
    ax1, ax2 = axs
    ax1.plot(time, susceptible, marker='', color='blue', label='susceptible')
    ax1.plot(time, infected, marker='', color='orange', label='infected')
    ax1.plot(time, recovered, marker='', color='green', label='recovered')

    deaths = dif(recovered)
    deaths.insert(0, 0)
    deaths = [i * 0.05 for i in deaths]
    total_deaths = 0
    for i in deaths:
        total_deaths += i
    ax2.plot(time, deaths, marker='', color='red', label=str(total_deaths))

    ax1.legend()
    ax2.legend()

    plt.show()


n = 1000
alpha = 0.001

beta = 1 / 7
s, i, r, t = sir(n, 5, 0, alpha, beta, 40)
draw_sirmodel(s, i, r, t)

print('running')