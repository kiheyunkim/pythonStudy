# 함수
"""
def 함수명(매개변수):
    실행문장

"""


# 함수의 선언
def add(a, b):
    return a + b


print(add(1, 5))
a = 3
b = 5
print(add(a, b))

result = add(a=10, b=8)
print(result)


# 값을 여러개를 받는 함수
def addMany(*args):
    result = 0
    for number in args:
        result += number
    return result


print(addMany(2, 4, 6, 8, 10))
print(addMany(1, 3, 5, 7, 9))
print(addMany(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 키워드 파라메터
def printkwargs(**args):
    print(args)


printkwargs(a=3, b=4, c=7, d=10)


# 함수는 결과값을 오직 하나만 갖는다
def addAndMultiply(a, b):
    return a + b, a * b


print(addAndMultiply(10, 33))


# 함수의 매개변수 기본 값을 지정할 수 있음.
# 매개변수 기본값은 뒤에서 부터 채워가면서 지정해야함
# 중간만 하는건 불가
def defaultFunction(a, b, c=50):
    return a + b + c


# 전부 전달
print(defaultFunction(10, 20, 30))
# 일부만 전달
print(defaultFunction(10, 20))
# 만약 중간에만 전달은 불가


# 함수 안에서 함수 밖의 변수를 변경하는 방법
a = 1


def globalChange(a):
    a = a + 1
    return a;


print(a)
a = globalChange(a)
print(a)

b = 1


def globalChange2():
    global b
    b = b + 1


print(b)
globalChange2()
print(b)

# 람다식
lambdaFunction = lambda a, b: a + b
print(lambdaFunction(10, 126))
