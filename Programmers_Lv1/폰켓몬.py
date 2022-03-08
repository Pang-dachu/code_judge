def solution(nums):
    
    half = int( len(nums) / 2 )
    unique = int( len( set(nums) ) )

    return min(half, unique)
