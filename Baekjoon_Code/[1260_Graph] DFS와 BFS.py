from collections import deque

# 노드, 간선, 시작점 입력 
N, M, start = map( int, input().split() )

graph = [[]]

# 노드 갯수만큼 빈 리스트 생성
# 0이 없으므로 빈리스트 
for i in range(N) :
    graph.append([])

# 간선 갯수만큼 값 입력받음. 
for j in range(M) :
    x,y = map( int, input().split() )
    
    graph[x].append(y)
    graph[y].append(x)
    
# 그래프 정렬 
for k in range(len(graph)) :
    
    graph[k] = sorted( list(set(graph[k])) ) 
    
# DFS 메서드 정의 
def DFS(graph, start, visited) :
    visited[start] = True
    print(start, end = " ")
    
    for i in graph[start] :
        if not visited[i] :
            DFS(graph, i, visited)        

# BFS 메서드 정의 
def BFS(graph, start, visited) :
    queue  = deque([start])
    visited[start] = True
    
    while queue :
        v = queue.popleft()
        print( v , end = " ")
        
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

visited = [False] * (N+1)
DFS(graph, start, visited)

print()

visited = [False] * (N+1)
BFS(graph, start, visited)