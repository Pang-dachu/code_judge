
# 첫번째 줄은 수열의 수의 갯수 N
# 두번째 줄부터는 N개의 숫자가 입력 

# 입력으로 주어진 수열이 내림차순으로 출력될 수 있도록 공백으로 구분하여 출력 

N = int(input())

permu = []

for _ in range(N) :
    permu.append( int(input()))


permu = sorted( permu, reverse=True)

for i in permu :
    print( i , end = ' ')