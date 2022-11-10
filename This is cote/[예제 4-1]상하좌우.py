import sys

size = int( sys.stdin.readline().rstrip() )

dir = sys.stdin.readline().rstrip().split()

x, y = 1 , 1

dx = [1,-1,0,0]
dy = [0,0,-1,1]
move_types = ['R','L','U','D']

for i in dir :
      
    temp_x = x + dx[ move_types.index(i) ]
    temp_y = y + dy[ move_types.index(i) ]

    if 1 <= temp_x <= size and 1 <= temp_y <= size :
        x, y = temp_x, temp_y
    
    print(y, x)

print("최종도착 : ",  y,x  )     



