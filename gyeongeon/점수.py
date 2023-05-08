lst=[]
count=0

for i in range(5):
    value=int(input("점수를 입력하시오: "))
    lst.append(value)

print("성적 평균=", sum(lst)/len(lst))
print("최대 점수=", max(lst))
print("최소 점수=", min(lst))

for score in lst:
    if score>=80:
       count +=1

print("80점 이상=", count)