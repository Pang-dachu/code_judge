import sys 

coord = []

for i in range( int(input()) ) :
    coord.append( sys.stdin.readline().rstrip().split(' ') )

for j in sorted( coord, key = lambda x : ( int(x[1]), int(x[0] )  )) :
    print( ' '.join(j) )


