# Dictionary 타입
my_dic = {3:"유재석", 100:"박명수"}

## key&value 접근
print(my_dic[3])
print(my_dic.get(100))

## key값이 존재한다면 value를 없으면 "없음"을 가져옴
print(my_dic.get(5,"없음"))

## key값으로 str형 사용가능
my_dic2 = {"A-3":"유재석", "B-100":"박명수"}
print(my_dic2["A-3"])
print(my_dic2.get("B-100"))

## key&value 추가
print(my_dic2)
my_dic2["C-20"] = "조세호"
print(my_dic2)

## key&value 제거
del my_dic2["A-3"]
print(my_dic2)

## key만 출력
print(my_dic2.keys())

## value만 출력
print(my_dic2.values())

## key&value 쌍으로 출력
print(my_dic2.items())

## key&value 지우기
my_dic2.clear()
print(my_dic2)



