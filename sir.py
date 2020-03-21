import matplotlib.pyplot as plt


def diff(array):
    diff_array = []
    for i in range(len(array) - 1):
        ndiff = array[i + 1] - array[i]
        diff_array.append(ndiff)

    return diff_array


def sir(s0, i0, r0, a, b, T):
    sarr = []
    iarr = []
    rarr = []
    for i in range(T):
        s = s0 - a * s0 * i0
        i = i0 + a * s0 * i0 - b * i0
        r = r0 + b * i0
        sarr.append(s)
        iarr.append(i)
        rarr.append(r)
        s0 = s
        i0 = i
        r0 = r

    return sarr, iarr, rarr, T


def plot_sir(suceptible, infected, recoverd, T, death_tolls=True):
    time = [i for i in range(T)]
    if death_tolls:
        fig, axs = plt.subplots(2)
        ax1 = axs[0]
        ax2 = axs[1]
        deaths = diff(recoverd)
        deaths.insert(0, 0)
        ax2.plot(time, deaths, marker='o', color='red', label='death tolls')
        ax2.legend()

    else:
        fig, ax1 = plt.subplots()

    ax1.plot(time, suceptible, marker='o', color='blue', label='suceptible')
    ax1.plot(time, infected, marker='o', color='orange', label='infected')
    ax1.plot(time, recoverd, marker='o', color='green', label='recovered')
    ax1.legend()

    plt.show()


s, i, r, T = sir(995, 5, 0, 0.0006, 1 / 5, 100)

plot_sir(s, i, r, T)
