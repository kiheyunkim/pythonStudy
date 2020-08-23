# python 3.3 아래 버젼에서 __init__가 없으면 패키지로 인식하지 못하는 상황을
# 방지하기 위해서 만드는 파일 __init__.py

# import * 을 했을 때 Module1과 2를 모두 가져오겠다는 의미.
__all__ = ['module1.py', 'module2.py']
