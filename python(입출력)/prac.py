# 표준 입출력

## ljust(num) = 왼쪽 정렬 , rjust(num) = 오른쪽 정렬
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4), sep=":")

## str.zfill(num) = num칸 만큼 공간을 채우고 str이외의 나머지 칸을 0으로 채움
for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))

# 다양한 출력 포멧    
## 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

print("{0: >10}".format(500))

## 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

## 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

## 3자리 마다 , 찍어주기
print("{0:,}".format(100000000))

## 3자리 마다 , 찍고 +- 부호 붙이기
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

## 소수점 출력
print("{0:f}".format(5/3))
## 소수점 특정 자리수 까지만 표시 (소수점 3째 자리째에서 반올림)
print("{0:.2f}".format(5/3))
