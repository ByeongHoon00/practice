# 전달값과 반환값
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0 ## 잔액
balance = deposit(balance, 1000) ## 입금
print(balance)

balance = withdraw(balance, 800) ## 출금
print(balance)

balance = withdraw(balance, 800) ## 출금
print(balance)

# 기본값
def profile(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어:{2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 키워드값
def profile2(name, age, main_lang):
    print(name, age, main_lang)

## 함수의 매개변수의 값을 키워드를 통해 전달받으면 순서가 바뀌어있어도 정상적으로 전달 가능함
profile2(name="유재석", main_lang="python" , age=20)
profile2(main_lang="java", age=25, name="김태호")

# 가변인자를 이용한 함수 호출
def profile3(name, age, *lang): # *을 이용해 가변인자 선언
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for language in lang:
        print(language, end=" ")
    print()

profile3("유재석", 20, "python", "java", "c", "c++", "c#")
profile3("김태호", 27, "kotlin", "swift")

# 지역변수와 전역변수
i = 10

def check(n):
    # i = 20 ## 지역변수 함수내에서만 사용됨
    global i ## 전역 공간에 있는 i를 사용
    i = i - n
    print("함수 내 i : {0}".format(i))

def check2(i,n):
    i = i - n
    print("함수 내 i : {0}".format(i))
    return i

print("처음 i : {0}".format(i))
check(2)
print("1번 함수 사용 후 i : {0}".format(i))
i = check2(i,2)
print("2번 함수 사용 후 i : {0}".format(i))


