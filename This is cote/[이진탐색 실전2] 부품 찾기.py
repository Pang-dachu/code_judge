import sys
input = sys.stdin.readline 

def binary_search(array, target, start, end) :
    if start > end :
        return "no"
    
    mid = (start+end) // 2

    if array[mid] == target :
        return "yes"
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)    
    else :
        return binary_search(array, target, mid+1, end)

N = int(input())
first = sorted( list(map(int, input().split())) )

M = int(input())
second = list(map(int, input().split()))



for i in second :
    print( binary_search(first, i, 0, N-1), end=' ')


