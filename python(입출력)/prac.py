# 표준 입출력

## ljust(num) = 왼쪽 정렬 , rjust(num) = 오른쪽 정렬
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4), sep=":")

## str.zfill(num) = num칸 만큼 공간을 채우고 str이외의 나머지 칸을 0으로 채움
for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))

