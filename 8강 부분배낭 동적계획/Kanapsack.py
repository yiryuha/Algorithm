
def knapsack(C, n, W, V):
    K = []
    P = []
    for i in range(0, n+1):
        K.append([0 for j in range(0, C+1)])
        P.append([(0,0) for j in range(0, C+1)])

    K[0][0] = 0
    P[0][0] = (-1,-1)
    for i in range(1, n + 1):
        K[i][0] = 0
        P[i][0] = (0, 0)
    for j in range(1, C + 1):
        K[0][j] = 0
        P[0][j] = (0, 0)

    for i in range(1, n+1):         #세로 none( 0 ) 부터 x
        for w in range(1, C+1):     #가로
            if W[i] > w:            #물건의 무게 w[i]가 배낭의 무게 w보다 무거운 경우 배낭의 무게는 변동됨
                K[i][w] = K[i-1][w] #배낭의 무개 = i를 고려하지 않은 배낭의 무게(최고의 무게 값)
                P[i][w] = (i - 1, w)
            else:
                #K[i][w] = max(K[i-1][w], K[i-1][w-W[i]]+V[i])
                if K[i-1][w] > K[i-1][w-W[i]]+V[i]:
                    K[i][w] = K[i-1][w]
                    P[i][w] = (i - 1, w)
                else:
                    K[i][w] = K[i-1][w-W[i]] + V[i]
                    P[i][w] = (i - 1, w - W[i])


    print("For Debugging ....")
    print_matrix(K, n, C)
    p = P[n][C]
    print((n, C))
    pp = (n, C)

    while p != (-1, -1):
        print(p)
        if p[1] == pp[1]:
            print("%d 물건은 담지 않음"%pp[0])
        else:
            print("%d 물건을 담음"%pp[0])
        pp = p
        p = P[p[0]][p[1]]

    print()
    return K[n][C]

def print_matrix(K, n, C):
    for i in range(0, n+1):
        for w in range(0, C+1):
            print("%3d" % K[i][w] ,end = ' ')
        print()


if __name__ == '__main__':      #무조건 if 한칸띄우기

    C = 10                      #배낭에 담을수 있는 총 무게
    n = 4                       #물건의 갯수
    W = [None, 5, 4, 6, 3]      #무게 처음은 null
    V = [None, 10, 40, 30, 50]  #가치 Value
    total_v = knapsack(C, n, W, V)
    print("Total Values =", total_v)
