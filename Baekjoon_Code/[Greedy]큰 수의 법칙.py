import sys

# N : 배열의 크기
# M : 숫자가 더해지는 횟수
# K : 연속으로 더해질 수 있는 횟수

N,M,K = map(int, input().split())

number = sorted( list( map(int, sys.stdin.readline().rstrip().split(' ')) ), reverse = True )

# 아래의 식을 조금 더 간결하게 정리하여 작성하는 것도 방법.
result = (M // (K+1)) * K * number[0] + (M // (K+1)) * number[1] + (M % (K+1)) * number[0]

print( result )

