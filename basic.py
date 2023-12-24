# List 타입

a = [1,2,3]
b = [4,5,6]

print(a+b)
print(a,b)

my_list = ["유재석", "조세호", "박명수"]
print(my_list)

# 조세호가 몇 번째 칸에 있는가?
print(my_list.index("조세호"))

# List 원소 추가(append, insert(index, ))

## 하하가 다음 칸에 탐
my_list.append("하하")
print(my_list)

## 정형돈이 유재석과 조세호 사이에 탐
my_list.insert(1, "정형돈")
print(my_list)

# List 원소 제거(pop, remove(특정값))

## pop 뒤에서 한 명씩 꺼냄(return값이 존재)
print(my_list.pop())
print(my_list)

## List 중간에 있는 특정값(정형돈)을 제거
my_list.remove("정형돈")
print(my_list)

# Tuple 타입
## List보다 메모리를 덜 차지, 수정이 불가함
menu = ("돈까스", "치킨까스")
print(menu[0])
print(menu[1])

