import sys 

input = sys.stdin.readline

line, brand = map(int, input().split())

six_ = []
one_ = []

for _ in range( brand ) :
    temp = input().split()
    six_.append( int( temp[0] ) )
    one_.append( int( temp[1] ) )

six_ = min( six_ )
one_ = min( one_ )


if six_ < one_ * 6 :
    temp = ( line // 6 ) * six_
    remain_ = line % 6

    if six_ < one_ * remain_ :
        print( temp + six_ )
    else :
        print( temp + one_ * remain_ )
else : 
    print( one_ * line )