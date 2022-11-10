from collections import deque

# DFS 메서드 정의 
def DFS( graph , v , visited ) :
    # 현재 노드를 방문 처리 
    visited[v] = True
    print(v, end=' ')
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[v] :
        if not visited[i] :
            DFS( graph, i, visited)

            
# BFS 메서드 정의 , deque 사용할 것 
def BFS(graph, start, visited) :
    queue  = deque([start])
    visited[start] = True
    
    while queue : 
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v] : 
            if not visited[i] :
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)
print("DFS 실행 : " , end = ' ')
DFS(graph, 1, visited)

print()

visited = [False] * len(graph)
print("BFS 실행 : " , end = ' ')
BFS(graph, 1, visited)