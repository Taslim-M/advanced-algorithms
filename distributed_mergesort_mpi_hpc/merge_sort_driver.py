import sys, time
import MergeSort #Imports mergesort functions
import numpy as np

my_id =int(sys.argv[1])
id_str = str(my_id).zfill(4)
file = '../data/numbers2sort_' + id_str

data = np.loadtxt(file)
data = [int(i) for i in list(data)]

#Sort and time sorting process
start_time = time.time() #Records start time

data = MergeSort.merge_sort(data) #Sorts array

time_taken = time.time() - start_time #Calculates and records time_taken

with open("time_merge_indiv.txt", "a") as file_object:
    file_object.write("%s %.5f \n" %(id_str, time_taken))

#Save to file as output
for element in data:
    print(element)
