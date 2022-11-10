
M, N, K = map(int, input().split())

graph = [ [0]*N ] * M
coord = [ list(map(int, input().split())) for _ in range(K) ]

for i in graph:
    print( i )

for x1,y1, x2,y2 in coord :
    print()
    for i in range(x1, x2) :
        for j in range(y1, y2) :
            graph[j][i] = 1

            for i in graph:
                print( i )


for i in graph:
    print( i )
    