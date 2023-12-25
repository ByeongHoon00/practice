# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "하하", "박명수"}
python = set(["유재석", "정형돈"])

## 교집합(java와 python의 교집합)
print(java & python)
print(java.intersection(python))

## 합집합(java와 python의 합집합)
print(java | python)
print(java.union(python))

## 차집합(java와 python의 차집합)
print(java - python)
print(java.difference(python))

## set에 값 추가
python.add("조세호")
print(python)

## set에 값 제거
python.remove("정형돈")
print(python)


# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
