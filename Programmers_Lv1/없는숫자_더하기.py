def solution(ls):
    origin = list( range(0,10) )
    answer = [x for x in origin if x not in ls]
    return sum( answer )
