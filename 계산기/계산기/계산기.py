cal = input("사칙연산(+, -, *, /)을 입력하세요:")

if cal != '+' and cal != '-'  and cal != '*' and cal != '/' :
    exit( print("잘못된 입력입니다.") )

N1 = input("첫 번째 양의 정수:")

if N1.isdigit() == False :
        exit( print("잘못된 입력입니다.") )    

n1 = N1

if  int(n1) <= 0 or float(n1) != int(n1) :
    exit( print("잘못된 입력입니다.") )

N2 = input("두 번째 양의 정수:")

if N2.isdigit() == False :
        exit( print("잘못된 입력입니다.") )   

n2 = N2

if  int(n2) <= 0 or float(n2) != int(n2) :
    exit( print("잘못된 입력입니다.") )

num1 = 0
num2 = 0

N1 = int(n1)
N2 = int(n2)

if N1 > N2 : 
    num1 = N1 
    num2 = N2

else : 
    num1 = N2 
    num2 = N1

if cal == '+' : 
    result = num1 + num2
    R = "%s + %s = %s"
elif cal == '-' :
    result = num1 - num2
    R = "%s - %s = %s"
elif cal == '*' :
    result = num1 * num2
    R = "%s * %s = %s"
elif cal == '/' :
    result = num1 / num2
    round(result)
    R = "%s / %s = %s"


print( R % (int(num1), int(num2), int(result)) )
