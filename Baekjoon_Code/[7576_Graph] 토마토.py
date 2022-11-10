from collections import deque
import sys 

def BFS(one_queue) :
    while one_queue :
        x,y = one_queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or N <= nx or ny < 0 or M <= ny :
                continue
            
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                one_queue.append((nx,ny))
                
M,N = map(int, input().split())

one_queue = deque()
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 :
            one_queue.append((i,j))

BFS(one_queue)

# graph = sum(graph, [])
# print( -1 if 0 in graph else max(graph)-1)
for i in graph :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)

print( max(map(max, graph)) - 1)

