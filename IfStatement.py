isSick = True
if isSick:
    print("병원에 가야한다")
else:
    print("평소처럼 한다")

# 연산자 종류
# x < y 연산자
print(1 < 2)
print(2 < 1)

# x > y 연산자
print(1 > 2)
print(2 > 1)

# x == y 연산자
print(2 == 2)
print(2 == 1)

# x != y 연산자
print(2 != 2)
print(2 != 1)

# x <= y 연산자
print(1 <= 1)
print(1 <= 2)
print(2 <= 1)

# x >= y 연산자
print(1 >= 1)
print(2 >= 1)
print(1 >= 2)

# and, or, not, 조건의 연결
condition1 = True
condition2 = False

# and C의 &&와 동일
print(condition1 and condition1)
print(condition1 and condition2)
print(condition2 and condition1)
print(condition2 and condition2)

# or C의 ||와 동일
print(condition1 or condition1)
print(condition1 or condition2)
print(condition2 or condition1)
print(condition2 or condition2)

# not C의 !와 동일
print(not condition1)
print(not condition2)

# x in s, x not in s
# 리스트, 튜플, 문자열에서 쓸 수 있음
testList = [1, 3, 5, 7, 9]
testTuple = (2, 4, 6, 8, 10,)
testString = "testString"

print(1 in testList)
print(2 in testList)
print(4 in testTuple)
print(3 in testTuple)
print('t' in testString)
print('a' in testString)

# pass 조건문의 내용을 뛰어넘는 것
if 3 in testList:
    pass  # 없다는 것을 명시한다. 만약 pass가 없으면 else는 불가능하다.
    # 밑에 만약 내용이 있으면 실행된다. 뛰어 넘을 것이면 다른걸 써야한다.
else:
    print("출력이 안되었어요")

# elif #다른 언어의 else if와 같음

if 4 in testList:
    print("4가 있습니다")
elif 6 in testList:
    print("6이 있습니다")
else:
    print("아무 것도 없습니다.")

# 조건부 표현식 : ?연산자와 유사
score = 55
message = "success" if score >= 60 else "failure"
print(message)
