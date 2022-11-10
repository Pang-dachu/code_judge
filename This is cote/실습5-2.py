def gcd( x : int , y : int ) -> int :
    if y == 0 :
        return x
    
    else :
        return gcd(y , x%y)
    

if __name__ == "__main__" :
    x = int(input("첫번째 숫자 입력 : "))
    y = int(input("두번째 숫자 입력 : "))
    
    print(f"{x}와 {y}의 최대 공약수는 {gcd(x,y)}입니다.")