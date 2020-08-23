# 패키지 안에 함수 실행 1
import module.module1

module.module1.module1func()

# 패키지 안에 함수 실행 2

#from module import Module2
from .module import module2

module2.module2func()

# 패키지 안에 함수 실행 3
from module.module2 import module2func

module2func()

import module

module.module2.module2func()  # 원래는 불가했으나 3.3부터는 가능
