

def factorial( num : int) -> int : 
    if num > 0 : 
        return num * factorial( num-1 )
    
    else :
        return 1
    

if __name__ == '__main__' :
    num = int( input("숫자 입력 : ") )
    print(f"{num}의 factorial 값은 {factorial(num)}입니다." ) 