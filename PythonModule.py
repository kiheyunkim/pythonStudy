# 패키지 안에 함수 실행 1
import Module.Module1

Module.Module1.module1func()

# 패키지 안에 함수 실행 2

from Module import Module2
from .Module import Module2  # .은 현재 경로, .. 은 부모경로

Module2.module2func()

# 패키지 안에 함수 실행 3
from Module.Module2 import module2func

module2func()

import Module

Module.Module2.module2func()  # 원래는 불가했으나 3.3부터는 가능
