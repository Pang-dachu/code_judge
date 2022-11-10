import sys

person = []

for _ in range(9) :
    person.append( int( sys.stdin.readline().rstrip() ) ) 

person = sorted( person )

for i in person :
    if sum(person) - 100 - i in person :
        person.remove( sum(person) - 100 - i )
        person.remove( i )

for i in person :
    print( i )

