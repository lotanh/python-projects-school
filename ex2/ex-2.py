import numpy as np
#First part
#1
suger_range = np.random.randint(11)
#2
arr = np.random.randint(suger_range , size=(16,21))
#3
def get_suger_avg(array):
    return np.round(np.average(array , axis=1), 3)
#4
get_suger_avg(arr)
#5
patients_avg_time = np.random.exponential(size=16)
print(patients_avg_time)
