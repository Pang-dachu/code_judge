import sys
from collections import deque

input = sys.stdin.readline

def BFS(v) :
    result = 0
    queue = deque([v])
    visited[v] = True
    
    while queue :
        v = queue.popleft()
        
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                
                result += 1
                
    return result 

N = int(input())

graph = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)

result = 0

for i in range( int(input())) :
    x,y = map(int, input().split())
    
    graph[x].append(y)
    graph[y].append(x)

print( BFS(1) )

    

    
