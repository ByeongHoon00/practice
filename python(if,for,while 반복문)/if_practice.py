# if문
weather = input("오늘의 날씨는? ")  ## str형태를 입력을 받음
if weather == "비" or weather == "눈":  ## 조건이 참이면 출력 아니면 넘어감
    print("우산을 챙기세요")
elif weather == "미세먼지" :     ## 조건이 참이면 출력 아니면 넘어감
    print("마스크를 챙기세요")
else :
    print("준비물이 필요없어요")

# for문
for wating_no in range(5): # [0,1,2,3,4]
    print("대기번호 : {0}".format(wating_no))

## list를 활용한 for문
starbucks = ["유재석","박명수","하하","조세호"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

