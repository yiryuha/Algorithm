#!/usr/bin/python

def bubbleSort(A):
##입력: 크기가 n인 배열 A
##출력: 정렬된 배열 A
##1. for pass = 1 to n-1
##2.    for i = 1 to n-pass
##3.         if (A[i-1] > A[i])     // 위의 원소가 아래의 원소보다 크면
##4.             A[i-1] ↔ A[i]   // 서로 자리를 바꾼다.
##5. return 배열 A
    A = A[:] # 원래의 배열 리스트를 훼손하지 않은 채로, 
             # 복제된 리스트를 정렬한다. 
    n = len(A)

##1. for pass = 1 to n-1
    for pss in range(1, n):
##2.    for i = 1 to n-pass
        for i in range(1, n-pss+1):
##3.         if (A[i-1] > A[i])     // 위의 원소가 아래의 원소보다 크면
            if A[i-1] > A[i]:
##4.             A[i-1] ↔ A[i]   // 서로 자리를 바꾼다.
                A[i-1], A[i] = A[i], A[i-1]
    
    return A

def bubbleSort2(A):
    A = A[:] # 원래의 배열 리스트를 훼손하지 않은 채로, 
             # 복제된 리스트를 정렬한다. 
    n = len(A)
    for pss in range(1, n):
        for i in range(1, n-pss+1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
    return A


import time
import random

def time_experiment(N=200, size=100):
    alist = random.sample(range(size*5), size) 

    print ("Time Experiment: Repetition %d, Data Size:%d"%(N, size))

    start = time.process_time()
    for _ in range(N):
        slist = bubbleSort(alist)
    end = time.process_time()
    print("Bubble Sort: %f sec"%(end-start))
    
    start = time.process_time()
    for _ in range(N):
        slist = bubbleSort2(alist)
    end = time.process_time()
    print("BubbleSort2: %f sec"%(end-start))

if __name__ == '__main__':
    print ("Bubble Sort:")
    alist = random.sample(range(100), 10) 
    slist = bubbleSort(alist)
    print ("Original: ", alist)
    print ("Sorted  : ", slist)
    print ()

    print ("BubbleSort2:")
    alist = random.sample(range(100), 10) 
    slist = bubbleSort2(alist)
    print ("Original: ", alist)
    print ("Sorted  : ", slist)
    print ()

    for s in range(100, 1001, 100):
        time_experiment(200, s)
