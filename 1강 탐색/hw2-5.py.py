#순차탐색 알고리즘 (Sequential Search)
# Time complex  :T(n) = n_데이터 수가 N만큼 연산 합니다

# Date 수가 N만큼 연산을 진행 하는 코드를 구현
def mySearch( a_list, n):

    i = 0
    listSize = len(a_list)  #반복할 리스트 크기

    while(i < listSize):
        if a_list[i] == n:
            return i        #찾는 값이 있는 경우 찾는 값의 요소를 반환
        i += 1

    return -1               #찾는 값이 없는 경우

#메인 모듈 
if __name__ == '__main__':  
    #Value 초기화
    a_list = [99, 1, 10, 70, 20, 33, 30, 89, 23, 29]    
    num = a_list[5]
    
    #함수 대입
    x = mySearch(a_list, num)

    #출력 -> 찾는 값이 없는 경우 or 있는 경우
    if x == -1:
        print("찾는 숫자가 없습니다")    
    else:
        print("찾는 숫자는" + str(num) + "은/는" + " " + str(x) + "번째 요소에 있습니다")
