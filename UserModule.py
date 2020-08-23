# 모듈의 사용 
# *는 모든것을 의미
# 파일명 으로 부터 어떤걸 가져올지를 지정 py는 생략
from CalculatorClass import *

cal = SafeCalculatorExp(10, 2)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())
print(cal.square())
print(cal.cube())

import sys

# 다른 경로에 있는 모듈을 추가하기 위해서는 sys.path에 추가해줘야함
print(sys.path)
# 또는 PYTHONPATH를 이용
# 환경변수를 추가해주면 됨.
