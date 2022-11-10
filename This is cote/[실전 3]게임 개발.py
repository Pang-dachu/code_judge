
map_size = list(map(int, input().split()))

pos_x, pos_y, cur = map(int, input().split())

game_map = []
count = 1

for i in range( map_size[1] ) :
    game_map.append( list(map(int, input().split())) )

game_map[pos_x][pos_y] = 1

# U R D L
set_dir = [(0,1),(1,0), (0,-1), (-1,0)]

while True :
    cur -= 1
    if cur < 0 : cur = 3

    if game_map[ pos_x + set_dir[cur][0] ][ pos_y + set_dir[cur][1] ] == 1 :






