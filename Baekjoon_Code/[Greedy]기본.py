
'''
사용할 수 있는 금액 : 500, 100, 50, 10
거슬러 주어야 하는 금액 : 1260

거스름 돈의 최소 갯수는 ? 
'''

n = 1260
count = 0

money = [500, 100, 50, 10]

for coin in money :
    count += n // coin
    n %= coin

    print("남은 금액 %d" %n)

print("동전의 최소 갯수 : %d" %count)

# 시간 복잡도는 O(동전의 종류 갯수)
