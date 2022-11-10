from collections import deque

def BFS(x, y) :
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 2
    cnt = 1
    
    while queue :
        x,y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or row <= nx or ny < 0 or col <= ny :
                continue
            
            if graph[nx][ny] != 0 :
                continue
            
            if graph[nx][ny] == 0 :
                queue.append((nx,ny))
                graph[nx][ny] = 2
                cnt += 1
    return cnt  
            
row, col ,K = map(int, input().split())

graph = [[0] * col for _ in range(row) ]

rect = [ list(map(int, input().split())) for i in range(K)]
area = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for c1,r1, c2,r2 in rect :
    for y in range(c1,c2) :
        for x in range(r1,r2) :
            graph[x][y] = 1


for i in range(row) :
    for j in range(col) :
        
        if graph[i][j] == 0 :
            area.append(BFS(i,j))
        
area.sort()
print( len(area) )

for i in area :
    print( i , end = ' ')


        
    