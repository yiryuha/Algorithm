from math import sqrt
import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%.2f, %.2f)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()


def distPair(p):
    if (p[0] and p[1]):
        d = sqrt((p[1].x - p[0].x) * (p[1].x - p[0].x) + (p[1].y - p[0].y) * (p[1].y - p[0].y))
        return d
    else:
        return float('inf')


def dist(p1, p2):
    if (p1 and p2):
        d = sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))
        return d
    return float('inf')


def pivotSplit_in_X(S, left, p, right, descend=False):
    S[p], S[left] = S[left], S[p]
    i = left + 1
    j = right
    # print (S[left], left, right, S)
    while (i <= j):
        # print (i, j)
        while (i <= j and ((descend == False and S[i].x <= S[left].x) or
                           (descend == True and S[i].x >= S[left].x))):
            i = i + 1
        while (i <= j and ((descend == False and S[j].x >= S[left].x) or
                           (descend == True and S[j].x <= S[left].x))):
            j = j - 1
        if (i < j):
            S[i], S[j] = S[j], S[i]
            i = i + 1
            j = j - 1
    new_p = i - 1
    S[left], S[new_p] = S[new_p], S[left]
    return new_p


def quickSort_in_X(S, left, right, descend=False):
    if (left < right):
        p = int((left + right) / 2)
        p = pivotSplit_in_X(S, left, p, right, descend)
        quickSort_in_X(S, left, p - 1, descend)
        quickSort_in_X(S, p + 1, right, descend)


def pivotSplit_in_Y(S, left, p, right, descend=False):
    S[p], S[left] = S[left], S[p]
    i = left + 1
    j = right
    while (i <= j):
        while (i <= j and ((descend == False and S[i].y <= S[left].y) or
                           (descend == True and S[i].y >= S[left].y))):
            i = i + 1
        while (i <= j and ((descend == False and S[j].y >= S[left].y) or
                           (descend == True and S[j].y <= S[left].y))):
            j = j - 1
        if (i < j):
            S[i], S[j] = S[j], S[i]
            i = i + 1
            j = j - 1
    new_p = i - 1
    S[left], S[new_p] = S[new_p], S[left]
    return new_p


def quickSort_in_Y(S, left, right, descend=False):
    if (left < right):
        p = int((left + right) / 2)
        p = pivotSplit_in_Y(S, left, p, right, descend)
        quickSort_in_Y(S, left, p - 1, descend)
        quickSort_in_Y(S, p + 1, right, descend)


def closestPairInThree(pair1, pair2, pair3):
    d1 = dist(pair1[0], pair1[1])
    d2 = dist(pair2[0], pair2[1])
    d3 = dist(pair3[0], pair3[1])
    if d1 < d2 and d1 < d3:
        return pair1
    elif d2 < d1 and d2 < d3:
        return pair2
    else:
        return pair3


def extractCenterRegionInSLeft(S, d):
    theMostRight_In_S = S[-1]
    for i in range(-1, -len(S) - 1, -1):
        if abs(theMostRight_In_S.x - S[i].x) > d:
            return S[i + 1:]
    return S[:]


def extractCenterRegionInSRight(S, d):
    theMostLeft_In_S = S[0]
    for i in range(0, len(S), 1):
        if abs(theMostLeft_In_S.x - S[i].x) > d:
            return S[0:i]
    return S[:]


def closestPairInCenter(S_left, S_right, d):
    S_centerLeft = extractCenterRegionInSLeft(S_left, d)
    S_centerRight = extractCenterRegionInSRight(S_right, d)
    S_center = S_centerLeft + S_centerRight

    quickSort_in_Y(S_center, 0, len(S_center) - 1)
    ## print("S_center : ", S_center)

    min_i = min_j = -1

    min_d = d
    for i in range(0, len(S_center) - 1):
        j = i + 1
        dij = dist(S_center[i], S_center[j])
        if dij < min_d:
            min_i = i
            min_j = j
            min_d = dij
    ##          ## TODO 추가해야할 사항: 반복구간의 조기 탈출
    ##          ## 위의 코드는 비효율적인 코드이다.
    ##          ## 모든 점들간에 비교를 할 필요는 없다.
    ##          ## TODO TODO TODO TODO
    ##          ## TODO TODO TODO
    ##          ## TODO TODO TODO TODO

    if (min_i >= 0):
        # print( S_centerLeft[min_i], S_centerRight[min_j], "d:", min_d)
        return (S_center[min_i], S_center[min_j])
    else:
        return (None, None)


def closestPair(S):
    i = len(S)
    if i == 0:
        return (None, None)
    elif i == 1:
        return (S[0], None)
    elif i == 2:
        return (S[0], S[1])
    elif i == 3:
        return closestPairInThree((S[0], S[1]), (S[1], S[2]), (S[0], S[2]))

    half_i = int(i / 2 + 0.5)
    S_left = S[0:half_i]
    S_right = S[half_i:]

    # print ("Split: ", S_left, S_right)
    cp_left = closestPair(S_left)
    cp_right = closestPair(S_right)
    d = min(distPair(cp_left), distPair(cp_right))
    # print ("d : ", d)
    cp_center = closestPairInCenter(S_left, S_right, d)
    # print ("cp_center", cp_center, "cp_d : ", distPair(cp_center))
    return closestPairInThree(cp_left, cp_center, cp_right)


def simpleClosestPair(S):
    # Compare all pairs and find the cloest pair
    min_d = sqrt(box_h * box_h + box_w * box_w)
    for i in range(0, len(S)):
        for j in range(0, i):
            # print (int(dist( S[i], S[j] )), end=', ' )
            d = dist(S[i], S[j])
            if d < min_d:
                min_d = d
                min_i = i
                min_j = j
                # print ()
    # print ("cloest Pair: ", S[min_i], S[min_j])
    # print ("closest distance = ", min_d )
    return (S[min_i], S[min_j])


def fastClosestPair(S):
    S1 = S[:]
    ## print ("Before Sort_in_X : ",S1)
    quickSort_in_X(S1, 0, len(S1) - 1)
    # print ("After  Sort_in_X : ", S1)
    return closestPair(S1)


def generateRandomPoints(width, height, n):
    from random import random
    S = []
    for i in range(n):
        p = Point(random() * width, random() * height)
        S.append(p)
    return S


box_w = 500
box_h = 300


def simpleTest():

    start = time.time()
    S = generateRandomPoints(box_w, box_h, 10)

    cp = simpleClosestPair(S)
    print("Simple Closest Pair: ", end='')
    print(cp)
    print("Closest distance : %.2f" % distPair(cp))
    print()

    print("timer_10:", time.time() - start)

    start2 = time.time()
    S2 = generateRandomPoints(box_w, box_h, 10)

    cp2 = fastClosestPair(S2)
    print("Faster Closest Pair: ", end='')
    print(cp2)
    print("Closest distance : %.2f" % distPair(cp2))
    print()

    print("timer_fast_10:", time.time() - start2)

def simpleTest2():

    start = time.time()
    S = generateRandomPoints(box_w, box_h, 100)

    cp = simpleClosestPair(S)
    print("Simple Closest Pair: ", end='')
    print(cp)
    print("Closest distance : %.2f" % distPair(cp))
    print()

    print("timer_100:", time.time() - start)

    start2 = time.time()
    S2 = generateRandomPoints(box_w, box_h, 100)

    cp2 = fastClosestPair(S2)
    print("Faster Closest Pair: ", end='')
    print(cp2)
    print("Closest distance : %.2f" % distPair(cp2))
    print()

    print("timer_fast_100:", time.time() - start2)

def simpleTest3():

    start = time.time()
    S = generateRandomPoints(box_w, box_h, 1000)

    cp = simpleClosestPair(S)
    print("Simple Closest Pair: ", end='')
    print(cp)
    print("Closest distance : %.2f" % distPair(cp))
    print()

    print("timer_1000:", time.time() - start)

    start2 = time.time()
    S2 = generateRandomPoints(box_w, box_h, 1000)

    cp2 = fastClosestPair(S2)
    print("Faster Closest Pair: ", end='')
    print(cp2)
    print("Closest distance : %.2f" % distPair(cp2))
    print()

    print("timer_fast_1000:", time.time() - start2)

def simpleTest4():

    start = time.time()
    S = generateRandomPoints(box_w, box_h, 10000)

    cp = simpleClosestPair(S)
    print("Simple Closest Pair: ", end='')
    print(cp)
    print("Closest distance : %.2f" % distPair(cp))
    print()

    print("timer_10000:", time.time() - start)

    start2 = time.time()
    S2 = generateRandomPoints(box_w, box_h, 10000)

    cp2 = fastClosestPair(S2)
    print("Faster Closest Pair: ", end='')
    print(cp2)
    print("Closest distance : %.2f" % distPair(cp2))
    print()

    print("timer_fast_10000:", time.time() - start2)

if __name__ == '__main__':
    simpleTest()
    simpleTest2()
    simpleTest3()
    simpleTest4()



