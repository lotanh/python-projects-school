import numpy as np
# #First part
# #1
suger_range = np.random.randint(11)
# # #################
# # #2
arr = np.random.randint(suger_range + 1 , size=(16,21))
print(arr)
# # ##################
# # #3
def get_suger_avg(array):
    return np.average(array , axis=1)
# # ###################
# #4
avgArrSuger = get_suger_avg(arr)
# ###################
# #5
patients_avg_time = np.random.exponential(size=16)
print(patients_avg_time)
# #######################
# #Second part
# # #######################
def max_suger_day(array):
    return np.argmax(np.average(array , axis=0)) + 1
# # ########################
def max_suger_patient(array):
    return np.argmax(get_suger_avg(array)) + 1
# # ########################
def get_max_time_patient(array):
    return np.argmax(array) + 1
# ##########################
print('The day with the maximum suger is: ', 'day ',max_suger_day(arr)) 
print('The patient with maximum avg suger is: ', 'patient number',max_suger_patient(arr)) 
print('The patient who waited the most is: ', 'patient number',get_max_time_patient(patients_avg_time))
##########################
def cumulative_suger(array):
    return np.cumsum(array)
# #################################
def count_item(array, number):
    return len(array[array == number])
####################################
import matplotlib.pyplot as plt
fig=plt.figure()

x = np.arange(0,16)
y = avgArrSuger
print(y)
plt.plot(x,y)
plt.show()

