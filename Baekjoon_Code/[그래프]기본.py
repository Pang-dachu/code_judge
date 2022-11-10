def dfs( v, visited = [] ) :
    visited.append( v )
    for i in graph[v] :
        if not i in visited :
            visited = dfs(i, visited)
    return visited 



# n개의 정점이 존재하고, m개 만큼의 입력을 받는다.

# n+1 만큼의 공간을 만들어서 graph[n]이 n번의 정점을 나타내도록.
n = 5
m = 4

graph = [ [] for _ in range(n+1) ]
# 실행 결과 []를 n+1 만큼 가지는 리스트 생성


for _ in range(m) :
    x,y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

print( graph )









