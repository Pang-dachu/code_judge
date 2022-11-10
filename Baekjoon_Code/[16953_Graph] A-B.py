from collections import deque


A,B = map(int, input().split())

queue = deque()
queue.append((A,1))

res = -1

while queue : 
    A , cnt = queue.popleft()
    cnt += 1
    
    if A == B :
        res = cnt
        break
    
    if A * 2 <= B :
        queue.append((A * 2,cnt))
        
    if int( str(A)+'1' ) <= B :
        queue.append((int( str(A)+'1' ) ,cnt))
    
print( res )