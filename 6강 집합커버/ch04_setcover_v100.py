#  잘못된 코드 부분을 수정함.

def commonList(A, B):
    A = set(A)
    B = set(B)
    C = A.intersection(B)
    return list(C)


def setCover(U, F):
    ##입력: U:커버할 항목들의 전체 집합, F={Si}, i=1,⋯,n, Si:부분커버집합
    ##출력: 집합 커버 C   : 부분커버집합들의 집합
    ##
    ##1. C=∅
    C = []
    U = list(U)
    F = list(F)
    F.sort(reverse=True, key=lambda S: len(commonList(S[1], U)))
    # ---> 이방법은 표현이 간단하고, 정확하기는 하나, 비효율적인 처리를 함.
    ##2. while (U≠∅) do {
    ##3.      U의 원소들을 가장 많이 포함하고 있는 집합 Si를 F에서 선택한다.
    ##4.      U=U-Si
    while len(U) > 0:       #0보다크면 0이면 공집합
        s = F.pop(0)
        for i in s[1]:      #마을이름 만큼
            n = U.count(i)  #갯수세기
            for j in range(n):
                U.remove(i)
    ##5.      Si를 F에서 제거하고, Si를 C에 추가한다.
    C.append(s)
    F.sort(reverse=True, key=lambda S: len(commonList(S[1], U)))
    #U내용변경되어 F를 새로정렬


    ##    }

    ##6. return C
    return C


if __name__ == '__main__':
    U = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    S1 = ('S1', (1, 2, 3, 8))
    S2 = ('S2', (1, 2, 3, 4, 8))
    S3 = ('S3', (1, 2, 3, 4))
    S4 = ('S4', (2, 3, 4, 5, 7, 8))
    S5 = ('S5', (4, 5, 6, 7))
    S6 = ('S6', (5, 6, 7, 9, 10))
    S7 = ('S7', (4, 5, 6, 7))
    S8 = ('S8', (1, 2, 4, 8))
    S9 = ('S9', (6, 9))
    S10 = ('S10', (6, 10))
    ##    F = {S7, S8, S9, S10, S1, S2, S3, S4, S5, S6}
    F = {S10, S9, S8, S7, S6, S5, S4, S3, S2, S1}
    C = setCover(U, F)
    print(C)
    print()

    U = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o')
    S1 = ('S1', ('a', 'b', 'c', 'd', 'e', 'm'))
    S2 = ('S2', ('g', 'c', 'i'))
    S3 = ('S3', ('a', 'f'))
    S4 = ('S4', ('d', 'o', 'l'))
    S5 = ('S5', ('b', 'j', 'l', 'n', 'k', 'g'))
    S6 = ('S6', ('e', 'h', 'o', 'n', 'i'))
    S7 = ('S7', ('k', 'm'))
    S8 = ('S8', ('j', 'm'))
    F = (S1, S2, S3, S4, S5, S6, S7, S8)

    C = setCover(U, F)
    print(C)
