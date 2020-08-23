# While 문
"""
while 조건문:
    실행내용
"""

# while문은 조건문이 true 이상 계속 반복함
counter = 10
while counter > 0:
    print("예시 1번: " + str(counter))
    counter -= 1

# while문에서 조선에 상관없이 빠져나올떄는 break를 쓴다

counter = 10
while counter > 0:
    print("예시 2번: " + str(counter))
    counter -= 1
    if counter == 4:
        break

# while문은

counter = 10
while counter > 0:
    counter -= 1
    if counter > 4:
        continue
    print("예시 3번: " + str(counter))

# 조건문에 True를 주면 무한대로 루프를 돈다.
