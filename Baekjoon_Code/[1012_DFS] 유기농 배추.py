import sys
sys.setrecursionlimit(10000)

def make_graph() :
    N, M, K = map( int, input().split() )
    
    graph = [ [0]*M for _ in range(N) ]
    
    result = 0
    
    # 배추 위치 입력하기 
    # 배추 위치에 해당하는 방문 노드 생성
    for i in range(K) :
        x,y = map( int, input().split() )
        graph[x][y] = 1
     
    for i in range(N) :
        for j in range(M) :
            if DFS(graph,i,j,N,M) == True :
                result += 1
     
    print(result)
        
def DFS(graph, x,y, N, M) :
    if x < 0 or N <= x or y < 0 or M <= y :
    # 0 <= x <= N and 0 <= y <= M : 로 대체 
    
        return False
    
    if graph[x][y] == 1 :
        graph[x][y] = 0
        
        DFS(graph, x,y-1, N, M)
        DFS(graph, x,y+1, N, M)
        DFS(graph, x-1,y, N, M)
        DFS(graph, x+1,y, N, M)
        
        return True
    
    return False
    

for i in range( int(input()) ) :
    make_graph()
        
    
    