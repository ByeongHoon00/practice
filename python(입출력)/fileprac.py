# 파일입출력

## w는 write로 쓰기위한 목적으로 파일을 염
""" score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() """

## a는 append로 내용을 추가하기 위해 파일을 염
""" score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close() """

## r은 read로 파일을 읽는 용도로 파일을 여는 역할
""" score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close() """

""" score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end = "") # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close() """

## while문과 readline을 이용해 파일 내용 읽기
""" score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close() """

## readlines를 이용해 파일 내용 읽기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()