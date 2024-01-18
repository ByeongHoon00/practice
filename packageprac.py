# __init__.py는 from import *로 패키지를 호출 할 때 어느 모듈을 공개할지 결정한다.

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to2 = thailand.ThailandPackage()
trip_to2.detail()