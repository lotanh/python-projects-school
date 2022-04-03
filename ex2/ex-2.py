import numpy as np

suger_range = int(np.floor(np.random.random() * 10 + 1))

arr = np.random.randint(0,suger_range, size=(16,21))

def get_suger_avg(array):
    avg = np.average(array, axis=1)
    return avg

print(get_suger_avg(arr))


