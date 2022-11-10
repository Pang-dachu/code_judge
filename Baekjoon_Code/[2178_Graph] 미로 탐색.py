import sys 
from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue : 
        x,y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 크기 예외 처리 
            if nx < 0 or ny < 0 or N <= nx  or M <= ny :
                continue
                
            if graph[nx][ny] == 0 :
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
 
    return graph[N-1][M-1]
    
    
N, M = map(int, input().split())

graph = []

for i in range(N) :
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print( BFS(0,0) )