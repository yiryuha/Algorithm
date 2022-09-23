#!/usr/bin/python

def shellSort(A):
##1. for each gap h = [ h0 > h1 > ... > hk=1] // 큰 gap부터 차례로
##2.    for i = h to n-1 { 
##3.         CurrentElement=A[i];
##4.         j = i;
##5.        while (j>=h) and (A[j-h]>CurrentElement) {
##6.              A[j]=A[j-h];
##7.               j=j-h;
##             }
##8.         A[j]=CurrentElement;
##     }
##9. return 배열 A
   
    A = A[:] # 원래의 배열 리스트를 훼손하지 않은 채로, 
             # 복제된 리스트를 정렬한다. 
    n = len(A)

    # hop을 피보나치 수열에 의해 지정되도록 함. 단, 일부 수(1, 2)를 제외함. 
    hopsList =[5, 3, 1]
    while hopsList[0]*2 < n :
        hopsList.insert(0, hopsList[0]+hopsList[1])
    for h in hopsList :
        pass

        #TODO TODO TODO
        #TODO TODO TODO
        #TODO TODO TODO
        #TODO TODO TODO
        #TODO TODO TODO
        #TODO TODO TODO
        #TODO TODO TODO    
    return A

import time
import random


if __name__ == '__main__':
    print ("Shell Sort:")
    alist = random.sample(range(100), 10) 
    slist = shellSort(alist)
    print ("Original: ", alist)
    print ("Sorted  : ", slist)
    print ()

