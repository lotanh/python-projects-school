import numpy as np

suger_range = int(np.floor(np.random.random() * 10 + 1))

arr = np.ones((16,21))

for i in range(0,suger_range):` `
    arr[i] = i
print(arr)


