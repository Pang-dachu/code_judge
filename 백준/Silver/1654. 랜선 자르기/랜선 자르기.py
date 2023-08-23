import sys

K, N = map(int, input().split())
lansun = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lansun)

while (start<=end) :
    cut_cnt = 0
    mid = (start+end) // 2

    for x in lansun :
        if x >= mid :
            cut_cnt += (x//mid)

    if cut_cnt < N :
        end = mid-1
    
    else :
        start = mid + 1

print( end )