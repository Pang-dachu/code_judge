import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

end = max(array)
temp = 0

def binary_search(array,temp, start, end) :
    if start > end :
        return None
    
    mid = (start+end) // 2
    length = 0

    for i in array :
        if i  > mid :       
            length += (i - mid)
    
    
    if length < M :
        return binary_search(array, temp, start, mid-1)

    else :
        temp = mid
        return binary_search(array, temp, mid+1, end)

print( temp )
    


        
