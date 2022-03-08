def solution(lottos, win_nums):
    ## 일치한 번호에 따른 등수 
    ## 일치한 갯수 : 등수
    grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6 }  
        
    return [ grade[len( set(win_nums) & set(lottos) ) + lottos.count(0)] , grade[len( set(win_nums) & set(lottos) )] ]
