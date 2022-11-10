import sys 
from collections import deque

input = sys.stdin.readline

# DFS, BFS 함수 작성 
def DFS(graph, visited, start) :
    visited[start] = 1

    print(start, end=' ')
    for i in graph :
        if not visited[i] :
            DFS(graph, i , visited)


def BFS() :
    print()


node, line, start = map(int, input().split())

graph = [ [] for _ in range(node+1) ]  
visited = [0] * (node+1)

for _ in range(line) :
    temp = list(map(int, input().split()))

    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])
    
for i in range(len(graph)) :
    graph[i] = sorted(list(set(graph[i])))

DFS(graph, visited, )
    




