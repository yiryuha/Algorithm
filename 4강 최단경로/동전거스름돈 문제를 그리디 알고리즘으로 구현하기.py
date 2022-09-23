
# 동전거스름돈 문제를 그리디 알고리즘으로 구현하기
#나중에 임의로 160원짜리 동전도 추가되더라고, changeCoin2함수를 그대로 사용할 수 있게 하라.

def changeCoin2(arr, gCoin):
    # (힌트2) 동전의 단위별로 갯수를 카운트하는 변수를 딕션너리 dict 구조로 표현하여 사용한다.
    numCoins = {}  # key와 값 : 결과 값을 딕셔너리에 넣어서 1 10 100 코인의 값이 0일때 0을 표현합니다
    numCoins[1] = 0
    numCoins[10] = 0
    numCoins[100] = 0
    cnt = 0
    value = gCoin

    for coin in arr:                                #coin은 arr(coins)[0]~ 끝 까지 반복합니다
        cnt = value//coin                           #총액을 coin번쨰 요소와 나눈 몫을 저장합니다 몇번 나눠떨어지는지
        value %= coin                                #총액은 코인으로 나눈 나머지 값이 되어야합니다 1300 %  500 = 2..650
        numCoins[coin] = cnt

    print(numCoins)


#(힌트1) 동전의 단위를 저장한 튜플리스트를 다음과 같이 정의하여 함수호출시에 인자로 함께 넘겨준다.
coins =  (1, 10, 100, 50, 500)
coins = sorted(coins,reverse = True)   #튜플정렬
getCoin = 1352
changeCoin2(coins, getCoin)


