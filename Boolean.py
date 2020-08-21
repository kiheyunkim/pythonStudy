a = True
b = False
print(a)
print(b)

# 자료 형 별 참 거짓

print(bool("python"))  # 참
print(bool(""))  # 거짓
print(bool([1, 2, 3]))  # 참
print(bool([]))  # 거짓
print(bool(()))  # 거짓
print(bool({}))  # 거짓
print(bool(1))  # 참
print(bool(0))  # 거짓
print(bool(None))  # 거짓

# 예시
list = [1, 2, 3, 4, 5, 6, 7]
while list:
    print(list.pop())

from copy import copy

a = copy(a)
print(a is b)
