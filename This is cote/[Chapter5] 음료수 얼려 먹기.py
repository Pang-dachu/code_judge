N, M = map( int, input().split() )

graph = []
for i in range(N) :
    graph.append( list( map( int, input().split() ) ) )
    

def DFS(x,y) :
    # 맵을 벗어나지 않도록
    if x <= -1 or N <= x or y <= -1 or M <= y :
        return False
    
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리
        graph[x][y] = 1
        
        # 상하좌우 4방향 
        DFS(x, y-1)
        DFS(x, y+1)
        DFS(x-1, y)
        DFS(x+1, y)
        
        return True
     
    # 방문한 노드의 값이 1이면 
    return False

result = 0

for i in range(N) :
    for j in range(M) :
        if DFS(i,j) == True :
            result += 1

print( result )
        