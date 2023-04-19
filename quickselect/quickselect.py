import math
import random
import copy

# https://www.geeksforgeeks.org/quickselect-algorithm/
def partition(arr, l, r):
      
    x = arr[r]
    i = l
    for j in range(l, r):
          
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i]
    return i
  
# finds the kth position (of the sorted array) 
# in a given unsorted array i.e this function 
# can be used to find both kth largest and 
# kth smallest element in the array. 
# ASSUMPTION: all elements in arr[] are distinct
def kthSmallest(arr, l, r, k):
  
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
  
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)
  
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
  
        # If position is more, recur 
        # for left subarray 
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
  
        # Else recur for right subarray 
        return kthSmallest(arr, index + 1, r, 
                            k - index + l - 1)
    print("Index out of bound")

def run_sim(scores):
    array = []

    for score in scores:
        if score != -1:
            array.append(score)
        else:
            k = len(array) - math.ceil(len(array) * 0.25) - 1
            if k >= 0:
                ds = copy.deepcopy(array)
                bottom_25th_percentile = kthSmallest(ds,0, len(ds)-1, k)

                array = [x for x in array if x >= bottom_25th_percentile]

    return array




input_scores = [1, 2, 9, 5, -1, 8, 3, 1, 3, 2, 9, -1, 8]
output = run_sim(input_scores)
print(output)  # Output: [9, 5, 8, 3, 3, 9, 8]