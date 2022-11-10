def solution(lottos, win_nums):
    ## 일치한 번호에 따른 등수를 딕셔너리에 저장. 
    ## 딕셔너리의 key : value 의 구조는 아래와 같음. 
    ## 일치한 갯수 : 등수
    grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6 }
    
    ## return 형식은 List를 사용하며, [최고순위, 최저순위] 의 형식으로 전달함.
    ## 1. 최고 순위
    ## grade[len( set(win_nums) & set(lottos) ) + lottos.count(0)] 
    ## 단순히 일치한 갯수를 확인한 뒤에, 0으로 계산된 값을 다 일치했다고 생각 => 0을 당첨된 갯수로 생각
    ## 당첨 번호와 입력받은 번호의 교집합 확인 뒤에 0의 갯수만 더해줌.
    
    ## 2. 최저 순위
    ## 최고 순위에서 0의 갯수를 고려하지 않고 교집합 갯수만 고려하면 됨.
    return [ grade[len( set(win_nums) & set(lottos) ) + lottos.count(0)] , grade[len( set(win_nums) & set(lottos) )] ]
    
