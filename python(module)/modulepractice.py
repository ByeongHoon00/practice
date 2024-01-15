# python은 코드 유지보수를 위해 코드를 모듈 단위로 관리함, 모듈이 확장자는 .py임

## import 모듈명 을 사용해 호출함.

import theater_module
theater_module.price(3) # 3명에서 영화보러 갔을 때 가격
theater_module.price_morning(4) # 4명에서 조조 할인 영화보러 갔을 때 가격
theater_module.price_soldier(5) # 5명에서 군인이 영화보러 갔을 때 가격

## 모듈명이 긴 경우 as를 이용해 짧게 사용가능

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

## from 모듈명 import를 이용해 모듈명을 쓰지 않고 사용 가능
## *을 사용하는 경우 해당 모듈 내 모든 내용을 선언, *대신 원하는 변수, 함수만을 선언할 수도 있음

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)


from theater_module import price, price_morning
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price_soldier as price
price(5)