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

balance = 0 # 잔액
balance = deposit(balance, 1000) # 입금
print(balance)

balance = withdraw(balance, 800) # 출금
print(balance)

balance = withdraw(balance, 800) # 출금
print(balance)
