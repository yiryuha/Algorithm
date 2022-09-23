##MatrixChain
##입력: 연속된 행렬 A1xA2x⋯xAn, 단, A1은 d0xd1, A2는 d1xd2, ⋯, An은 dn-1xdn이다.
##출력: 입력의 행렬 곱셈에 필요한 원소의 최소 곱셈 횟수 C[1,n]
##1. for i = 1 to n
##2.         C[i,i] = 0      //대각선 초기화
##3. for L = 1 to n-1 { // L은 부분 문제의 크기를 조절하는 인덱스이다.
##4.       for i = 1 to n-L {
##5.              j = i + L
##6.             C[i,j] = ∞
##7.             for k = i to j-1 {
##8.                     temp = C[i,k] + C[k+1,j] + di-1dkdj
##9.                     if (temp < C[i,j])
##10.                             C[i,j] = temp
##                          }
##                   }
##      }
##11. return C[1,n]

def matrixChain(dList):
    # dList = (d0, d1, d2,.....dn)   ; n개의 연속된 행렬의 행수와 열수의 리스트.
    n = len(dList) - 1
    c = []
    f = []

    # Making multi-dimensional array_ compile easy will be understanded
    for i in range(n + 1):  #0~4까지
        c.append([])
        f.append([])

        #dLlist extended _ multi-dimensional array
        for j in range(n + 1):
            c[i].append(0)
            f[i].append("")         #문자열 null string으로 초기화
            if i == j:
                f[i][j] = "a%d"%i

    #Making multi-dimensional array_ test
    #print_Matrix(c)

    # TODOTODO
    for l in range(1,n):            #1~n-1, 0 is not include(0 = 0      )가로끝까지 1~4

        #회전할때마다 넣는 수 가 적어진다.
        for i in range(1,n-l+1):    #행열 개수 보다 작은값까지 반복합니다 즉)n-l을 사용해서 -1씩 반복합니다 -> 첫동작시 3번 두번째는 2번만 3번째는 1번만 넣어주면 됩니다_대각선으로
            #a = n - l + 1
            j = i + l               #j는 처음에 2라면 두번째는 3이되어야합니다 첫동작시 행렬[1][3]에 넣고 다음동작시 i증가 [2][4]에 넣는 방식으로 대각선으로 넣습니다
            c[i][j] = float('inf')  #최솟값을 찾기위해 대각선 성분에 무한대 값을 넣습니다 무한대에 최소값이 들어갑니다


            for k in range(i, j):   #가로줄 i의 세로줄 j에 값을 넣는
                temp = c[i][k] + c[k+1][j] + dList[i-1]*dList[k]*dList[j]   #앞서구한 값 + dlist요소
                #컴파일
                #q = dList[i-1]     #k의 기준점-1
                #d = dList[k]       #k는 기준점 i
                #x = dList[j]       #k의 기준점 +1

                if temp < c[i][j]:  #행렬에서 i라는 값은 배열 끝까지 동작하는데, 다음 동작마다 +1해서 동작해야합니다 -> 1000 자리가아닌 다음자리에 1750을 계산해야 되기때문입니다. 거기의 세로줄 j
                    c[i][j] = temp
                    f[i][j] = "("+f[i][k]+")X("+f[k+1][j]+")" #문자열 출력
        #print_Matrix(c)




    return c[1][n], f[1][n]


def print_Matrix(M):
    print('------%dx%d--------' % (len(M), len(M[0])))
    for row in M:
        for col in row:
            print("%5d" % col, end=' ')
        print()
    print('-------------------')


if __name__ == '__main__':
    #행열 A B C D
    dL = (10, 20, 5, 15, 30)  # 10x20 , 20x5, ...

    c, f = matrixChain(dL)

    #최소 곱셈 횟수수
    print("필요한 곱셉횟수 : ", c)
    print("곱셉순서 : ", f)
