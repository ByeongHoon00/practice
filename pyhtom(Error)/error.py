# try내부에 있는 문장을 실행하다가 오류가 발생한 경우 except 부분을 확인해  해당하는 오류가 발생한 경우 명령을 실행
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1])) 
    print("{0} / {1} = {2}".format(nums[0], nums[1],nums[2]))
## 에러가 발생할 경우 except의 코드 실행 후 종료(에러를 내면서 종료하지 않음)
except ValueError:
    print("에러 ! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err :
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
