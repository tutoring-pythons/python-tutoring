i=[]

while True:
    print("add=추가, delete=삭제, end=입력종료")
    st = input("입력: ")

    if st == "add":
        s = input("추가할 원소 입력:")
        i.append(s)
        print("추가 완료")

    if st=="delete":
        if len(i)==0:
            print("리스트 비어있음")
        else:
            i.pop()
            print("삭제 완료")

    if st=="end":
        print("입력 종료")
        break

print("최종 리스트:", i)