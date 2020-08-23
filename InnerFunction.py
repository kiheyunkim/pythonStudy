"""
abs
all
any
chr
dir
divmod
enumerate
eval
filter
hex
id
input
int
isinstance
len
list
map
max
min
oct
open
ord
pow
range
round
sorted
str
sum
tuple
type
zip
"""

# 1 abs()   절대값으로 변환
print(abs(3))
print(abs(-3))
print(abs(-3.2))

# 2 all()   모두 참이라면 TRUE
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))

# 3 any() 하나라도 참이면 TRUE
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))
print(any([]))

# 4 chr() ASCII코드를 입력받아 해당하는 문자를 출력
print(chr(100))
print(chr(130))

# 5 dir() 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
print(dir([1, 2, 3]))

# 6 divmod() 숫자 2개를 입력받고 몫과 나머지는 튜플로 돌려줌
print(divmod(103, 6))

# 7 enumerate() - 열거하다라는 뜻, 인덱스 값을 포함하는 enumerate 객체를 돌려줌
for i, name in enumerate(['one', 'two', 'three', 'four']):
    print(i, name)

# 8 eval() 실행가능한 문자열을 입력받아서 문자열을 실행한 결과값을 돌려주는 함수
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(5,2)'))


# 9 filter 걸러낸다.
def filterFunc(x):
    return x < 0


print(list(filter(filterFunc, [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])))

print(list(filter(lambda x: x > 0, [1, -2, 3, -4, 5, -6, -7, 8])))

# 10 hex()
print(hex(234))
print(hex(40))

# 11 id() 입력받은 객체의 고유 주소값을 돌려주는 함수
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))

# 12 input() 입력받는 함수
a = input()
print(a)
b = input("input: ")
print(b)

# 13 int 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수 형태로 돌려줌
print(int('3'))
print(int(3.14))

# 2진수를 10진수 정수로 변환
print(int('11', 2))
# 16진수를 10진수 정수로 변환
print(int('1A', 16))


# 14 isinstance(a,b) 입력된 a가 b로 만들어진 인스턴스인지 판단한다
class A:
    pass


class B:
    pass


a = A()
b = B()
print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, A))
print(isinstance(b, B))

# 15 len 요소 개수, 길이

print(len("python"))
print(len([1, 2, 3, 4]))
print(len(["python", 1, 'a', {1: 3, 4: 2}]))
