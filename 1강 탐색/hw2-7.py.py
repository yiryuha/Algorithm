#Binary Search
# Time complex  : O(LogN) _ 상황에 따른 log n만큼 시간 복잡도를 가집니다

# 초기 값은 중간 값을 가르키며 반으로 줄여 가며  값을 찾는 코드를 구현

def binarySearch(a_list, n):

    listSize = len(a_list)                   #반복할 리스트 크기
    l, r = 0, listSize                       #start end = 첫번째, 마지막
    mid = 0                                  #mid


    while l <= r:                           #0배열 부터 끝배열까지 반복합니다

        mid = int (l + (r - l) / 2)        #중간 값: overflow 발생을 처리를 위해 * 보단 +로 처리했습니다. 기타 (l+r) //2

        if a_list[mid] == n:                #key값이 중간 값일시 리턴합니다
            return mid
        elif a_list[mid] < n:               #key값이 중간값 보다 클시 0번째 요소를 mid + 1번째 요소로 둡니다
            l = mid + 1
        else:
            r = mid - 1                     #key값이 중간값 보다 작을시 마지막 요소를 mid - 1번째 요소로 둡니다

    return -1                               #값이 없는 경우 (반복 문에 찾아도 안나올 때)




#메인 모듈
if __name__ == '__main__':
    #Value 초기화
    a_list = [12, 34, 3, 66, 30, 21, 88, 44, 22, 99]
    a_list = sorted(a_list)                                             
    num = a_list[5]

    #함수 대입
    x = binarySearch(a_list, num)

    #출력
    if x == -1:
        print("찾는 숫자가 없습니다")
    else:
        print("찾는 숫자는" + str(num) + "은/는" + " " + str(x) + "번째 요소에 있습니다")
