import sys 

sugar = int( sys.stdin.readline().rstrip() )

count = 0

# count += (sugar // 15) * 3
# sugar %= 15
        
while True:
    sugar -= 5 
    count += 1
    
    if sugar % 5 == 0 :
        count += sugar // 5
        break
    
    elif sugar % 3 == 0 :
        count += sugar // 3
        break
    
    if sugar <= 0 :
        count = -1
        break
    
print( count )