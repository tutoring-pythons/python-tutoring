import turtle

t=turtle.Turtle()
t.shape("turtle")

a=int(input("정수를 입력하세요: "))

if (a>0):
  t.goto(100,100)
  t.write("거북이가 여기로 오면 양수입니다.")
  

elif (a==0):
  t.goto(100,0) 
  t.write("거북이가 여기로 오면 0입니다.")
  

else:
  t.goto(100,-100)
  t.write("거북이가 여기로 오면 음수입니다.")

turtle.mainloop()