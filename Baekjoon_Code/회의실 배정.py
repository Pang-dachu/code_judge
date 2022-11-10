import sys 

time = []

for _ in range( int(input()) ) :
    time.append( sys.stdin.readline().rstrip().split(' ') )

for i in sorted( time , key = lambda x : x[0] ) :
    print( i )