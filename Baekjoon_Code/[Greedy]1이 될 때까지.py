'''
어떠한 수 N이 1이 될때까지 다음 두가지 방법중 하나를 선택한다.
1) N에서 1을 뺀다 
2) N을 K로 나눈다.

이때 1번 방법과 2번 방법의 최소 횟수를 구하시오 .
'''
N = 25
K = 5

count = 0

while N > 1 :
    if N % K == 0 :
        N //= K 
    else :
        N -= 1

    count += 1 
print( count )