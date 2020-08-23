"""
Q1
주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
"""


def is_odd(number):
    return "짝수" if number % 2 == 0 else "홀수"


print(is_odd(5))
print(is_odd(8))

"""
Q2
입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

※ 평균 값을 구할 때 len 함수를 사용해 보자.
"""


def average(*args):
    sum = 0
    for number in args:
        sum += number
    return sum / len(args)


print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

"""
Q3
다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
이 프로그램을 수행해 보자.

첫번째 숫자를 입력하세요:3
두번째 숫자를 입력하세요:6
두 수의 합은 36 입니다
3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

※ int 함수를 사용해 보자.
"""
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = str(int(input1) + int(input2))
print("두 수의 합은 %s 입니다" % total)

"""
Q4
다음 중 출력 결과가 다른 것 한 개를 골라 보자.

1 print("you" "need" "python")
2 print("you"+"need"+"python")
3 print("you", "need", "python")
4 print("".join(["you", "need", "python"]))
"""

"""
정답은 3번 문자열에 콤마를 쓰면 띄어 쓰기가 됨
"""

"""
Q5
다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())
이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
"""

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

"""
Q6
사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
"""

f3 = open("test2.txt", 'a', encoding="UTF-8")
while True:
    line = input()
    if not line:
        break
    f3.write(line + '\n')

"""
Q7
다음과 같은 내용을 지닌 파일 test3.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

Life is too short
you need java
※ replace 함수를 사용해 보자.
"""

f4 = open("test3.txt", 'w', encoding="UTF-8")
f4.write("Life is too short\n")
f4.write("you need java\n")
f4.close()

f4 = open("test3.txt", 'r', encoding="UTF-8")
lines = f4.readlines()
f4.close()
newLines = [line.replace('java', 'python') for line in lines]

f4 = open("test3.txt", 'w', encoding="UTF-8")
for line in newLines:
    f4.write(line)
f4.close()
