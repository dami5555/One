import turtle

len = 80
x = -350
y = -50

p = turtle.Turtle()

num = int(turtle.numinput("입력", "변의 수를 입력하세요:"))
if num < 4:
    exit("잘못된 입력입니다.")
n = num - 1
while n <= num+1:
    for c in ["red", "green", "blue"]:
        p.penup()
        p.home()
        p.setposition(x,y)
        p.pendown()

        for i in range(n):
            p.color(c)
            angle = 360/(n)
            p.forward(len)
            p.left(angle)
    
        p.penup()
        p.right(90)
        p.forward(35)
        p.pendown()
        p.write("정"+str(n)+"각형",font=("Arial", 15, "normal"))

        n += 1
        x += 40*n

p.penup()
p.forward(20)

turtle.done()