array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
    if start >= end :   # 원소가 한 개인 경우
        return 
    
    pivot = start
    
    left = start + 1
    right = end

    while left <= right :
        
        while left <= end and array[left] <= array[pivot] :
            left += 1
        
        while right > start and array[right] >= array[pivot] :
            right -= 1

        
        if left > right :   # The moment the left and right cross.
            array[right], array[pivot] = array[pivot], array[right]
        
        else : # Not cross.
            array[left], array[right] = array[right],  array[left]
    
    # 분할한 이후 pivot을 기준으로 나눈 왼쪽과 오른쪽 부분을 각각 정렬 수행 
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array) - 1)
print( array )
