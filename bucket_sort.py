import random
import time
import multiprocessing
import math

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    
             
def bucketSort(x):
    arr = []
    slot_num = 100

    for i in range(slot_num):
        arr.append([])
         
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    print ('Buckets:')
    print (arr)
     
    processes = 10

    for i in range(slot_num):
        pool = multiprocessing.Pool(processes)
        size = int(len(x) / processes)
        arr[i] = [arr[i * size:(i + 1) * size] for i in range(processes)]
        extra = arr[i].pop() if len(arr[i]) % 2 == 1 else None
        arr[i] = [(arr[i], arr[i + 1]) for i in range(0, len(x), 2)]
        arr[i] = pool.map(insertionSort, arr[i]) + ([extra] if extra else [])

         
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x

if __name__ == "__main__":
    while (True):
        size = int(input('Size: '))
        arr = []
        for i in range(size):
            arr.append(random.random())
        
            print ('\nArray before sorting: ', arr)
        print()

        start = time.time()
        res = bucketSort(arr)
        end = time.time()

        print('\nArray after sorting: ', res)
        print('Time: ', round(end-start, 3))
        print()
