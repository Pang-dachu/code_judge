import sys
from collections import deque

input = sys.stdin.readline

def BFS(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    
    while queue :
        v = queue.popleft()
        
        for i in graph[v] :
            if not visited[i] :
                queue.append( i )
                visited[i] = True
    
N, M = map( int, input().split() )

graph = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)
result = 0

for i in range(M) :
    x, y = map( int, input().split() )
    
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1) :
    if visited[i] == True :
        continue
    
    else : 
        BFS(graph, i, visited)
        result += 1
        
print( result )