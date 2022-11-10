
coord = input()

x, y = ord( coord[0] ) - 96 , int( coord[1] )

steps = [(-2,1),(-2,-1), (2,1),(2,-1), (-1,2),(1,2), (-1,-2),(1,-2)]
count = 0

for i in steps :
    if 1<= x + i[0] <=8 and 1<= y + i[1] <= 8 :
        count += 1

print( count )

