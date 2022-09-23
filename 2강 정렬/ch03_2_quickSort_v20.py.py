def pivotSplit(A, left, p, right):
    # print("....bef....", left, p, right, A )
    # A[left]와 A[p]의 자리를 바꾼 후,
    # 피봇 A[left]와 배열 A[left+1]~A[right]의 각 원소A[i]를
    # 비교하여 피봇보다 작은 숫자는 A[left]~A[p-1]로 옮기고,
    # 피봇보다 큰 숫자들은 A[p+1]~A[right]롤 옮기며,
    #  피봇 A[left]는 A[p]에 놓는다.
    # print("....aft....", left, new_p, right, A )
    A[p], A[left] = A[left], A[p]                 #중앙값과 맨앞값을 바꾼다
    i = left + 1
    j = right

    while(i <= j):                              #맨앞값+1요소가 끝요소와 교차할때까지
        while(i <= j and A[i] <= A[left]):       #i가 j와 교차시에 탈출 and i가 중간 보다작으면 ok 크면 탈출
           i += 1
        while(i <= j and A[j] >= A[left]):
            j -= 1
        if(i < j):
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    new_p = i - 1 
    A[left], A[new_p] = A[new_p], A[left]  
    return new_p


def quickSort(A, left, right):
    """ 퀵정렬 알고리즘 """
    ##QuickSort(A, left, right)
    ##입력: 배열 A[left]~A[right]
    ##출력: 정렬된 배열 A[left]~A[right]
    ## 1 if (left < right) {
    ## 2     피봇 인덱스 p를  A[left]~A[right] 중에서 선택하고,
    ##       피봇 A[p]를 A[left]와 자리를 바꾼 후,
    ##       피봇 A[left]와 배열A[left+1]~A[right]의 각 원소 A[i]를 비교하여
    ##            피봇보다 작은 숫자들은 A[left]~A[p-1]로 옮기고,
    ##            피봇보다 큰 숫자들은 A[p+1]~A[right]로 옮기며,
    ##       피봇 A[left]는 A[p]에 놓는다.
    ## 3 QuickSort(A, left, p-1)   // 피봇보다 작은 그룹을 가지고 재귀호출
    ## 4 QuickSort(A, p+1 right)  // 피봇보다 큰 그룹을 가지고 재귀호출

    # print( ".....", left, right, " : ", A[left:right+1])
    if(left < right):
        p = (left+right)//2
        new_p = pivotSplit(A, left, p, right)
        quickSort(A,left, new_p-1)
        quickSort(A, new_p+1, right)


def test_fn(A):
    Origin_A = tuple(A)
    print()
    print('Original Data : ', Origin_A)
    print('Sorted  Data : ', sorted(Origin_A))
    quickSort(A, 0, len(A) - 1)
    print('QuickSorted  : ', A)


if __name__ == '__main__':
    from random import sample

    A = sample(range(100), 10)  # sample()함수에 의해 10개의 무작위 수를 자동 추출
    test_fn(A)

    List_OK1 = [14, 22, 11, 73, 39, 10, 90, 60, 21, 57]
    List_OK2 = [8, 67, 75, 50, 27, 71, 43, 20, 61, 76]
    List_OK3 = [32, 34, 41, 65, 49, 64, 5, 31, 61, 81]
    for x in List_OK1, List_OK2, List_OK3: test_fn(x)

    List_Incorrect1 = [32, 84, 22, 37, 21, 94, 34, 97, 58, 43]
    List_Incorrect2 = [91, 7, 4, 33, 45, 61, 94, 14, 9, 0]
    List_Incorrect3 = [85, 43, 64, 45, 84, 48, 13, 46, 0, 91]
    for x in List_Incorrect1, List_Incorrect2, List_Incorrect3: test_fn(x)

    List_Error1 = [40, 33, 11, 8, 1, 76, 47, 12, 9, 60]
    List_Error2 = [10, 2, 44, 89, 41, 13, 56, 81, 9, 85]
    List_Error3 = [19, 92, 97, 80, 28, 20, 64, 57, 91, 89]
    for x in List_Error1, List_Error2, List_Error3: test_fn(x)
