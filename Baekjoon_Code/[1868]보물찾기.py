
graph = {}

for i in range( int(input()) - 1 ) :
    temp = list( map(int, input().split(' ')) )
    graph[temp[0]] = temp[1]


print( graph )