import sys, time
from math import pi
import MergeSort #Imports mergesort functions
import numpy as np
import os
path = './res/'
file_limit = int(sys.argv[1])
files = os.listdir(path)
#retrive job id (same for all files)
string_job_id = files[0].split('.')[1].split('_')[0]
#sorted.219689_0.out
def makeFileName(file_number):
    str_fn = 'sorted.'+string_job_id +'_'+ str(file_number) +'.out'
    return str_fn

def mergeKLists(lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = MergeSort.merge(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None

def make_list_of_lists(start,end):
    list_of_lists = []
    for i in range(start,end):
        fname = makeFileName(i)
        list_load = np.loadtxt(os.path.join(path,fname))
        list_load = [int(i) for i in list(list_load)]
        list_of_lists.append(list_load)
    return list_of_lists


list_of_lists = make_list_of_lists(0, file_limit)

start_time = time.time() #Records start time
final = mergeKLists(list_of_lists)

time_taken = time.time() - start_time #Calculates and records time_taken

with open("time_combine_files.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write("%s %.5f \n" %(file_limit, time_taken))

for element in final:
    print(element)

