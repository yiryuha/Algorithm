def dpcoinchange(n, dList):
##DPCoinChange(n, [d1, d2, ⋯ ,dk ])
##입력: 거스름돈 n원, k개의 동전의 액면, d1> d2> ⋯ > dk=1
##출력: C[n]
##
##1. for i = 1 to n C[i]=∞
##2. C[0]=0
##3. for j = 1 to n { // j는 1원부터 증가하는 (임시) 거스름돈 액수이고, j=n이면 입력에 주어진 거스름돈이 된다.
##4.       for i = 1 to k {
##5.             if (di ≤ j) and (C[j-di]+1<C[j])
##6.                      C[j]=C[j-di]+1
##            }
##    }
##7. return C[n]

    k = len(dList)
    C = []
    D =[]
    ### TODO TODO


    for i in range(0, n+1):
        C.append(float('inf'))      #비어있는 항목은 append시켜야됩니다
        D.append(float('inf'))
       #C[i] = float('inf')         #불가능 비어있습니다 -> 0초기화 가능
    C[0] = 0                        #C의 0는 0초기화
    D[0] = 0

# 동전의 액면가 종류 di
    for j in range(1, n+1):         #1원부터 끝까지
        for i in range(0, k):       #1원 부터 끝까지 를 리스트와 0~k의 요소와 비교

            # dlist[i]돈보다 지금 반복하는 1[j]원이 더커야됩니다 and 기존값 - 현재값 < 기존값 이면 업데이트
            if dList[i] <= j and C[j - dList[i]] + 1 < C[j]:
                C[j] = C[j - dList[i]]+ 1       #최솟값 갱신후 리턴
               # D[j] = D[j - dList[i]] + ", %d" % (dList[i])
        print(C)
    return C[n]

if __name__ == '__main__' :
    n = 20
    dList = [16, 10, 5, 1]
    total_coin = dpcoinchange(n, dList)
    print ("The number of coins=", total_coin)
