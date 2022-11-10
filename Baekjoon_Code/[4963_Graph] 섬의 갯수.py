import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

def DFS(i,j) :
    # 맵을 벗어나지 않도록
    if i <= -1 or y <= i or j <= -1 or x <= j :
        return False
     
    if graph[i][j] == 1 :
        graph[i][j] = 0
    
        # 상하
        DFS(i,j-1)
        DFS(i,j+1)
        
        # 좌우
        DFS(i-1,j)
        DFS(i+1,j)
        
        # 대각
        DFS(i-1,j-1)
        DFS(i-1,j+1)
        
        DFS(i+1,j-1)
        DFS(i+1,j+1)

        return True 
    
    return False 

while True :
    x, y = map( int, input().split() )
    
    if x + y == 0 :
        break
    
    graph = []
    result = 0
    
    # 그래프 생성
    for i in range(y) :
        graph.append( list(map(int, input().split() )) )    
    
    for i in range(y) :
        for j in range(x) :
            if DFS(i,j) == True :
                result += 1

    print( result )