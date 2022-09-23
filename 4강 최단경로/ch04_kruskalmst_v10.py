from ch03_quicksort_v30 import quickSort
from ch04_graphutils_v10 import *

def kruskal_MST(g):
    # 입력: 가중치 그래프 G=(V, E), n개의 점과 m개의 선분
    # 출력: 최소 신장 트리
    n = len(g.vertexes())
    m = len(g.edges())
    # 1.가중치의 오름차순으로 선분들을 정렬한다. 정렬된 선분리스트를 L이라고 하자.
    L = list(g.edges())
    #길이, 오름차순, (key = 람다 매개변수):표현식
    quickSort(L, descend=False, key=lambda e: g.edgeweight(e))

 #   print("Sorted edges :")
    for __e in L:                       #L에서 하나씩 꺼냅니다(리스트)
        print(__e, g.edgeweight(__e))

    # 2. T=empty_graph  //트리를 초기화시킨다.
    t = Tree_Weighted([], dict({}))         #그래프라이브러리에서 제공
    ##    t.print()

    # 3. while(T의 선분수 < n-1 {
    # tree의 간선 갯수가 n-1보다 작을때 까지반복합니다 리스트의 길이가 0보다 클때까지 반복해 0보다작으면 탈출
    while len(t.edges()) < n-1 and len(L) > 0 :
    # 4. L에서 가장 작은 가중치를 가진 선분 e를 가져오고, e를 L에서 제거한다.
        e = L.pop(0)

    ##        # 디버깅 목적으로 필요시에 아래의 코드를 사용함. 디버깅후 지우기
    ##    print ("poped edges :", e)
    ##    print ("Remain edges :")
        for __e in L:
            print ( __e, g.edgeweight(__e))

    ##6. 사이클이 안만들어지면 e와 가중치를 트리에 추가시킨다.
        if not t.check_cycle_with_edge(e) :
            t.addedge (e, g.edgeweight(e))
    ##     print ("추가된 선분:" , e)

    ##7.  // e가 T에 추가되어 사이클이 만들어지는 경우 e를 버린다.
    return t


if __name__ == "__main__":
    V_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g')       #튜플구조에 a~g까지 요소

    # 점이 연결된 구조
    EW_dict = {('a', 'b'): 18, ('a', 'c'): 8, ('a', 'd'): 2, ('a', 'f'): 10,
               ('b', 'd'): 12, ('b', 'e'): 4, ('c', 'f'): 5,
               ('d', 'e'): 14, ('d', 'f'): 3, ('d', 'g'): 30,
               ('e', 'g'): 26, ('f', 'g'): 16}          #딕셔너리 구조 key:값(가중치)

    g = Graph_Weighted(V_tuple, EW_dict, undirected=True)
    g.print()                              #함수선언 여기서함

    k_tree = kruskal_MST(g)                #트리만들고
    k_tree.print()                          #트리 출력

