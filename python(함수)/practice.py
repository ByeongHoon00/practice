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