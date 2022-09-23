from inspect import k
import time
from random import randint

def pivotSplit ( A, left, p, right ) :
    # print("....bef....", left, p, right, A )
    A[p], A[left] = A[left], A[p]  # A[left]와 A[p]의 자리를 바꾼 후,
    i = left+1                              # 피봇 A[left]와 배열 A[left+1]~A[right]의 각 원소A[i]를
    j = right                                # 비교하여 피봇보다 작은 숫자는 A[left]~A[p-1]로 옮기고,
    while ( i <= j ) :                       # 피봇보다 큰 숫자들은 A[p+1]~A[right]롤 옮기며,
        # print("............", i, j, A )
        while ( i <= j and A[i] <= A[left] ) :  # it is OK
            i = i + 1
        while ( i <= j and A[j] >= A[left] ) : # it is OK
            j = j - 1
        if ( i < j ) :
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j= j - 1
    new_p = i-1
    A[left], A[new_p] = A[new_p], A[left]      #  피봇 A[left]는 A[p]에 놓는다.
    # print("....aft....", left, new_p, right, A )
    return new_p

def selection(A, left, right, k):
    p = randint(left, right)
    p = pivotSplit(A, left, p, right)

    S = p - left

    #KEY가 스몰 그룹에게 있을때(스몰이클때) VS 없을때
    if k <= S:
        return selection(A, left, p-1, k)
    elif k == S + 1:
        return A[p]
    else:
        return selection(A, p+1, right, k- S - 1)



def test_fn(n):
        A = sample(range(10000), n)    # sample()함수에 의해 n개의 무작위 수를 자동 추출
        Origin_A = tuple(A)
        print ()
        print ('Original Data : ', Origin_A )
        sA = sorted(Origin_A)
        print ('Sorted  Data : ', sorted(Origin_A))
        k = randint(1, n)  # random of (1, 2, ..., n)
        print ("expected value in rank ", k, " : ", sA[k-1] )
        result = selection (A, 0, len(A)-1, k)
        print ("selection value in rand ", k, " : ", result )


if __name__=='__main__' :
    from random import sample

    start = time.time()
    test_fn(10)
    print("timer:", time.time() - start)

    start2 = time.time()
    test_fn(100)
    print("timer3:", time.time() - start2)

    start3 = time.time()
    test_fn(1000)
    print("timer3:", time.time() - start3)

    start4 = time.time()
    test_fn(10000)
    print("timer4:", time.time() - start4)
