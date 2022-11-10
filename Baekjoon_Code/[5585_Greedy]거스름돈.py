import sys 

client = 1000 - int( sys.stdin.readline().rstrip() )

money = [500, 100 ,50 , 10, 5, 1]
count = 0

for coin in money :
    count += client // coin
    client %= coin 
    
print( count )
