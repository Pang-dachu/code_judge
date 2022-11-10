import sys
from collections import deque

input = sys.stdin.readline

def BFS(x,y, visited) :
    queue = deque()
    queue.append( (x,y) )
    visited[x][y] = True
    
    while queue :
        x,y = queue.popleft()
        
        # 그래프의 상하좌우 
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N :
                if graph[nx][ny] >= k and visited[nx][ny] == False :
                    visited[nx][ny] = True
                    queue.append((nx,ny))
        
N = int(input())

graph = [ list(map(int, input().split() )) for _ in range(N) ]

graph_max = max(map(max, graph))
graph_min = min(map(min, graph)) 

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

result = 0
    
#for k in range(max_num+1) :
for k in range(graph_min, graph_max+1) :    
    visited = [ [False]*N for _ in range(N) ]
    temp = 0

    for i in range(N) :
        for j in range(N) :
            if graph[i][j] >= k and visited[i][j] == False :
                
                BFS(i,j, visited)
                temp += 1
    
    if result < temp :
        result = temp 
            
print( result )
