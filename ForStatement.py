# for문
"""
for 변수 in (리스트, 튜플, 문자열):
    실행 문장
"""

# for문의 사용
listArray = ['one', 'two', 'three', 'four', 'five']
for element in listArray:
    print(element)

# for문의 사용2
pairListArray = [('one', 'two'), ('two', 'three'), ('three', 'four')]
for (first, second) in pairListArray:
    print(first)
    print(second)

# for문에서 continue를 만나면 for문의 가장 처음으로 이동한다.
studentNum = 0
scores = [100, 34, 70, 10, 80, 99]
for score in scores:
    studentNum += 1
    if score < 70:
        print(str(studentNum) + "번 학생은 탈락입니다")
    else:
        continue

# for문에서 range를 사용하여 순차적으로 사용할 수 있게 해준다.
print(range(0, 10))
for number in range(0, 10):
    print(number)

# 리스트 내포
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)


