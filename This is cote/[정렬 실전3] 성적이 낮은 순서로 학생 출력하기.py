
# 첫번째 줄에 학생수 N이 입력 
# 두번째 줄부터 학생의 이름과 성적이 공백으로 구분되어 입력 

# 성적이 낮은 순서대로 학생의 이름을 출력하기 

N = int(input())

student = []

for _ in range(N) :
    student.append( input().split() )


student = sorted( student , key = lambda x : int(x[1])) 

for i in student :
    print(i[0], end = ' ')

