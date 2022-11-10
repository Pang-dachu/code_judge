from collections import deque

def DFS(x,y) :
    global num
    if x < 0 or x >= N or y < 0 or y >= N :
        return False
    
    if graph[x][y] == 1 :
        graph[x][y] = 0
        num += 1
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            DFS(nx, ny)
        return True
        
    return False 

def BFS(x,y) :
    count = 1
    queue = deque()
    queue.append( (x,y) )
    graph[x][y] = 0
    
    while queue :
        x,y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or N <= nx or ny < 0 or N <= ny :
                continue
            
            if graph[nx][ny] == 0 :
                continue
            
            if graph[nx][ny] == 1 :
                queue.append((nx,ny))
                graph[nx][ny] = 0
                count += 1
    
    return count

        
N = int(input())

graph = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

amount = []
count = 0
num = 0 

for i in range(N) :
    graph.append( list(map(int, input())) )

print("DFS") 
# DFS
for i in range(N) :
    for j in range(N) :
        
        if DFS(i,j) == True :
            amount.append( num )
            num = 0
            
print( len(amount) ) 
amount.sort()
for i in amount : 
    print( i )

print("BFS") 
# BFS   
for i in range(N) :
    for j in range(N) :
        
        if graph[i][j] == 1 :
            amount.append( BFS(i,j) )

 
print( len(amount) ) 
amount.sort()
for i in amount : 
    print( i )
        
        
