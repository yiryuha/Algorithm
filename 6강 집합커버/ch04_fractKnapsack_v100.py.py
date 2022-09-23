def fractionalKnapsack(V, c):
    ##입력: n개의 물건, V 각 물건의 무게와 가치, 배낭의 용량 C
    ##출력: 배낭에 담은 물건 리스트 L과 배낭에 담은 물건의 가치 합 v
    # n: 불필요한 입력, V: 딕셔너리형 {'물건명':(무게, 가치), .....}, V['물건묭'] = (무게, 가치),
    # c " 숫자형(int 또는 float)
    # L : list형, [('물건명', 실은무게), ....], v : 가치의 합(int)

    ##1. 각 물건에 대해 단위 무게 당 가치를 계산한다.
    s = []
    for item in V.keys():                                   #물건들에 이름을 for루프돌림
        s.append((item, V[item][1]/V[item][0]))             #추가(단어,숫자)

    ##2. 물건들을 단위 무게 당 가치를 기준으로 내림차순으로 정렬하고,
    ##    정렬된 물건 리스트를 S라고 하자.
    # TODO TODO TODO TODO   # a의 1번째 값을 기준으로 역정렬
    s.sort(reverse=True, key = lambda  a: a[1])
    print("s:", s)

    ##3. L=∅, w=0, v=0
    ##	// L은 배낭에 담을 물건 리스트,
    ##        // w는 배낭에 담긴 물건들의 무게의 합,
    ##        // v는 배낭에 담긴 물건들의 가치의 합이다.
    # TODO TODO TODO
    L = []
    v = 0
    w = 0



    ##4. S에서 단위 무게 당 가치가 가장 큰 물건 x를 가져온다.
    # TODO TODO TODO TODO
    if len(s) > 0:
        x = s.pop(0)
    else:
        return L, v

    ##5. while ( (w+x의 무게) ≤ C ) {
    #TODO 튜플가져오가
    # xx = V[x[0]]        #백금이 있는곳 x가 백금 10 60
    # xxx =  [x[0]][0]
    # xxxx= V[x[0]][0]   #백금이있는 곳 v[백금요소x][0째요소] 10
    # xxxxx = w+V[x[0]][0] #10
    # xxxxxx = x[0] #백금
    # xxxxxxxxxx = x[0][0] #백

    while w+V[x[0]][0] <= c:
        xxxx= V[x[0]][0]            #0,0 -> 10, 0,1 -> 60

    ##6.    x를 L에 추가시킨다.
    # TODO
        L.append((s[0],V[x[0]][1]))
    ##7.    w = w + x의 무게
    # TODO
        w = w + V[x[0]][0]
    ##8.    v = v + x의 가치
        v = v+V[x[0]][1]
    ##9.    x를 S에서 제거한다.
        if len(s) > 0:
            x = s.pop(0)
        else:
            break

    ##10.	S에서 단위 무게 당 가치가 가장 큰 물건 x를 가져온다.
    # TODO TODO TODO TODO
    ##     }

    ##11. if ((c - w) > 0) { // 배낭에 물건을 부분적으로 담을 여유가 있으면
    # TODO
    if c-w > 0:
    ##12. 	물건 x를 (c-w)만큼만 L에 추가한다.
    # TODO
        L.append((x[0], (c-w)))
    ##13. 	v = v +(c- w)만큼의 x의 가치
    # TODO
        v = v+(c-w) *x[1]           #가치는 1 무게는 0

    ##      }
    ##14. return L, v
    # TODO
    return L, v


if __name__ == "__main__":
    mList = {'주석': (50, 5), '백금': (10, 60), '은': (25, 10), '금': (15, 75)}
    sackWt = 40
    print(mList, sackWt)

    sack_mList, sack_Value = fractionalKnapsack(mList, sackWt)
    #print(sack_mList, sack_Value)
