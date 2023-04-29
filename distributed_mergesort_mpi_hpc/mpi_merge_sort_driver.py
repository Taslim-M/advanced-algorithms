from mpi4py import MPI
import sys, time
import numpy as np

import MergeSort #Imports mergesort functions

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
name = MPI.Get_processor_name()

file_limit = int(sys.argv[1])

def makeFileName(file_number):
    file_number = str(file_number).zfill(4)
    str_fn = '../../data/numbers2sort_' + file_number
    return str_fn

def mergeKLists(lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = MergeSort.merge(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None

def make_big_list(start,end):
    big_list = []
    for i in range(start,end):
        fname = makeFileName(i)
        list_load = np.loadtxt(fname)
        list_load = [int(i) for i in list(list_load)]
        big_list.extend(list_load)
    return big_list

if rank == 0:
    list_of_lists = make_big_list(0,file_limit)
    big_arr = np.array(list_of_lists)
    #if I have 5 process, 1 is master so 4 slaves to do work
    slaves = nprocs-1
    splits = np.array_split(big_arr, slaves)
    for i in range(1,nprocs):
        data = splits[i-1]
        comm.send(data, dest=i)
    
    sorted_lists = []
    for i in range(1,nprocs):
        data = comm.recv(source=i)
        sorted_lists.append(data)
    
    start_time_merge = time.time()
    
    final = mergeKLists(sorted_lists)
    
    time_taken_merge = time.time() - start_time_merge #Calculates and records time_taken
    with open("mpi_time_combine_files.txt", "a") as file_object:
        file_object.write("%s %s %.5f \n" %(nprocs,file_limit, time_taken_merge))
    #Save to file as output
    for element in final:
        print(element)

else:  
    data = comm.recv(source=0)
    #Every Slave process convert data to array and perform MergeSort
    data = [x for x in data]
    start_time_sort = time.time()
    data = MergeSort.merge_sort(data)
    time_taken_sort = time.time() - start_time_sort #Calculates and records time_taken
    with open("mpi_time_merge_indiv.txt", "a") as file_object:
        file_object.write("%s %s %.5f \n" %(file_limit, rank, time_taken_sort))
    comm.send(data, dest=0)

