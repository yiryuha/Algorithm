#Binary Search_Recursive

def binarySearch_Rerusive(a_list, mid, start, end, key):
    mid = (start + end)//2

    if a_list[mid] == key:
        return mid
    elif a_list[mid] < key:
        return binarySearch_Rerusive(a_list, mid, mid - 1, end, key)
    else:
        return binarySearch_Rerusive(a_list, mid, start, mid + 1, key)



#메인 모듈
if __name__ == '__main__':
    #Value 초기화
    a_list = [12, 34, 3, 66, 30, 21, 88, 44, 22, 99]
    a_list = sorted(a_list)

    key = a_list[5]
    start, end = 0, len(a_list)
    mid = 0

    #함수 대입
    x = binarySearch_Rerusive(a_list, mid, start, end, key)

    #출력
    if x == -1:
        print("찾는 숫자가 없습니다")
    else:
        print("찾는 숫자는" + str(key) + "은/는" + " " + str(x) + "번째 요소에 있습니다")























