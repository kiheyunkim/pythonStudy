# 숫자형
num1 = 123
# 실수형
num2 = 1.2
num3 = 4.24E10
# 8진수
num4 = 0o177
# 16진수
num5 = 0xABC

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

# 사칙연산
num1 = 5
num2 = 7
print(num1 + num2)  # +
print(num1 - num2)  # -
print(num1 * num2)  # *
print(num1 / num2)  # /

# 제곱 연산
print(num1 ** num2)

# 나머지 연산
print(num1 % num2)

# 몫 반환 연산자
print(num1 // num2)

# 문자열 만들기
"Hello World"
'Hello World'
"""Hello World"""
'''Hello World'''

# 문자열에 작은 따옴표 표시
print("Hello 'my' World")
print('Hello "my" World')
print("Hello \"my\" World")
print('Hello \'my\' World')

# 문자열 줄바꿈 처리
print("Hello \n World")
print("""Hello 
 World""")

# 문자열 연산하기
front = "HELLO "
back = "WORLD"
number = 3
print(front + back)
print(front * number)

# 문자열 길이
print(len(back))

# 문자열 인덱스
print(back[0])  # 0번부터 시작
print(back[2])  # 양수는 앞에서 부터
print(back[-4])  # 음수는 뒤에서 부터

# 문자열 슬라이싱
print(back[0] + back[1] + back[2])
print(back[0:3])  # 0<= index < 3
print(back[1:])  # 2<= index < len(back)
print(back[:])
print(back[-4: -1])

# 문자열 변경
string = "1234567890"
# string[3] = '2' #immutable
# print(string)
print(string[:3] + '2' + string[4:])

# 문자열 포메팅
print("Hello %s's World" % "python")

# format함수를 통한 포메팅
print("Hello {0}'s World".format("Java"))
print("Hello {lang}'s World".format(lang="C++"))

# 왼쪽 정렬 오른쪽 정렬 가운데 정렬
print("{0:<10}".format("hi"))  # 왼쪽 정렬      # 10 글자 할당해서 hi를 넣고 왼쪽 정렬
print("{0:^10}".format("hi"))  # 가운데 정렬    # 10 글자 할당해서 hi를 넣고 가운데 정렬
print("{0:>10}".format("hi"))  # 오른쪽 정렬    # 10 글자 할당해서 hi를 넣고 오른쪽 정렬

# 공백 채우기
print("{0:=^10}".format("test"))  # 0번째 인자인데 =로 나머지를 채우고 가운데 정렬을 하며 총 10글자를
print("{0:!^10}".format("test"))  # 0번째 인자인데 !로 나머지를 채우고 가운데 정렬을 하며 총 10글자를

# f문자열 포매팅(python 3.6 부터)

name = 'kim'
age = 300
print(f'my name is {name}. my age is {age}')

# f문자열 포매팅 with Dictionary(python 3.6 부터)
d = {'name': 'kim', 'age': 3000}
print(f'my name is {d["name"]}. my age is {d["age"]}')
