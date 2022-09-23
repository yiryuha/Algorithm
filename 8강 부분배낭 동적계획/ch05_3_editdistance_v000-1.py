def editDistance(S, T):
    ##입력: 스트링 S, T, 단, S와 T의 길이는 각각 m과 n이다.
    ##출력: S를 T로 변환하는 편집 거리, E[m,n]
    ##1. for i=0 to m E[i,0]=i    // 0번 열의 초기화
    ##2. for j=0 to n E[0,j]=j     // 0번 행의 초기화
    ##3. for i=1 to m
    ##4.     for j=1 to n
    ##5.          E[i,j] = min{E[i,j-1]+1, E[i-1,j]+1, E[i-1,j-1]+α}
    ##6. return E[m,n]

    #배열초기화
    E = []
    P = []
    m = len(S)      #6
    n = len(T)      #7

    #6칸 7줄의 2차원 배열 만들면서 0초기화
    for i in range(0, m + 1):
        E.append([0 for j in range(0, n + 1)])  # 0으로 0~n까지 추가
        P.append([None for k in range(0, n + 1)])

    E[0][0] = 0
    for i in range(1, m + 1):
        E[i][0] = i
        P[i][0] = (i-1,0)

    for j in range(1, n + 1):
        E[0][j] = j
        P[0][j] = (0, j-1)

    ### TODO TODO
    ##3. for i=1 to m
    for i in range(1, m+1):     #단어 strong 1~6까지 0.0은 0
    ##4.     for j=1 to n
        for j in range(1, n+1):  #비교할 대상 sto
    ##5.          E[i,j] = min{E[i,j-1]+1, E[i-1,j]+1, E[i-1,j-1]+α}
           # if S[i-1] == T[j-1]: alpha = 0      #s와 t는 문자열이라서 0부터시작
           # else: alpha = 1

           #if else와 위와 같은 표현
            alpha = int (S[i-1] != T[j-1])      # ==시 같으면 1반환 틀리면 0반환 !=시 같으면 0 틀리면 1

          #  E[i][j] = min(E[i][j-1]+1, E[i-1][j]+1, E[i-1][j-1]+alpha )

            if(E[i][j-1]+1 < E[i-1][j]+1 and
            E[i][j-1]+1 < E[i-1][j-1]+alpha):
                E[i][j] = E[i][j-1]+1
                P[i][j] = (i, j-1)

            elif (E[i-1][j]+1 < E[i][j-1]+1 and
                    E[i-1][j] + 1 < E[i - 1][j - 1] + alpha):
                    E[i][j] = E[i-1][j] + 1
                    P[i][j] = (i-1,j)

            else:
                E[i][j] = E[i-1][j-1]+alpha
                P[i][j] = (i-1, j-1)
                
    print_matrix(E, m, n)
    print()

    print("For tracking ....")

    i, j = m, n
    path = []
    path.append( ((i,j), "end") )

    while P[i][j] != None:
        path.append(P[i][j])        #이부분은 오류가 떠서 더공부하겠습니
        i, j = P[i][j]
    print(path)


    # list1 = []
    # for op in path[:-1]:
    #     if path[path.index(op)+1][1] == "insert":
    #         list1.insert(0, "insert" + T[path[path.index(op)+1][0][1]])
    #     elif path[path.index(op)+1][1] == 'delete' :
    #         list1.insert(0, 'delete' + S[path[path.index(op)+1][0][1]])
    #     elif path[path.index(op) + 1][1] == 'change':
    #         list1.insert(0, 'change' + S[path[path.index(op)+1][0][1]])
    #     elif path[path.index(op)+1][1] == 'match' :
    #         list1.insert(0, 'match' + S[path[path.index(op)+1][0][1]])
    # for m in list1: print(op)

    return E[m][n]

def print_matrix(E, m, n):
    for i in range(0, m+1):
        for j in range(0, n+1):
            print("%3d" % (E[i][j]), end=' ')
        print()


if __name__ == '__main__':
    S = "stone"
    T = "strong"
    print("S=", S)
    print("T=", T)
    d = editDistance(S, T)
    print("Total distance=", d)

    print()
