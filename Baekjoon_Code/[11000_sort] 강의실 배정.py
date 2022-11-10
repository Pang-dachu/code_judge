
import sys
import heapq

input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

time.sort()

time_q = []

heapq.heappush(time_q, time[0][1])

for i in range(1, N):
    if 


