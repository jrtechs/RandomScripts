import matplotlib.pyplot as plt
import time
import Fibonacci as fib


def measureTime(n):

    total = 0
    for i in range(0, 200000):
        start_time = time.time()
        fib.fibClosedFormula(n)
        end_time = time.time()
        total += end_time - start_time
    return total/200


def generateData():
    time = []
    input = []

    for i in range(1, 1000, 20):
        input.append(i)
        time.append(measureTime(i))
    return input, time


data = generateData()
plt.plot(data[0], data[1])
plt.xlabel('Fibonacci Term')
plt.ylabel('Seconds')

plt.show()