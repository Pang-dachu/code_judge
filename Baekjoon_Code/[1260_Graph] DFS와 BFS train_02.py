from collections import deque
import sys

input = sys.stdin.readline

##
def DFS(graph, visited, start) :
    visited[start] = True
    
    print( start , end = ' ')
        
    for i in graph[start] :
        if not visited[i] :
            DFS(graph, visited, i)
            
##
def BFS(graph, visited, start) :
    queue = deque([start])
    visited[start] = True
    
    while queue :
        temp = queue.popleft()
        print( temp, end = ' ')
        
        for i in graph[temp] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

node, line, start = map(int, input().split())


graph = [ [] for _ in range(node+1) ]

for i in range(line) :
    temp = list(map(int, input().split()))
    
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])
    
for j in range(len(graph)) :
    graph[j].sort()

visited = [False] * (node+1) 
DFS(graph, visited, start)

print()

visited = [False] * (node+1) 
BFS(graph, visited, start)