'''

from itertools import combinations

N = int(input())

liquid = list(map(int,input().split()))

temp = sorted( list( combinations(liquid, 2) ) , key = lambda x : abs( x[0]+x[1] ) ) 

for i in sorted( temp[0] ) :
    print(i, end= ' ')
    
'''
import sys 
input = sys.stdin.readline 

N = int(input())
liquid = sorted( list(map(int,input().split())) )

left = 0
right = len(liquid) - 1

temp = liquid[left] + liquid[right]

# 서로 같은 특성의 용액 
if liquid[-1] * liquid[0] > 0 :
    print( min(liquid[0], liquid[1]) , max(liquid[0], liquid[1]) )

# 서로 다른 특성의 용액
else :
    while True :
        if liquid[left] < 0 :
            left += 1 
        if liquid[right] > 0 :
            right -= 1
        
        if liquid[left+1] > 0 and liquid[right-1] < 0 :
            break
    
if abs(temp) > abs(liquid[left] + liquid[right]) :
    print( min(liquid[left], liquid[right]) , max(liquid[left], liquid[right]) )
else : 
    print( liquid[0], liquid[-1] )
    
        
            
    
        