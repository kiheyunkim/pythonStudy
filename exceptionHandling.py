# 예외처리 try except 문
# 아래는 모두 오류가 나는 문장들

"""open("1.txt", "r", encoding="UTF-8")

print(4 / 0)

array = [1, 2, 3, 4]
print(array[10])"""

# try except 를 이용해서 오류처리
try:
    open("1.txt", "r", encoding="UTF-8")
except:
    print("오류 발생1")

# try except 를 이용하면서 Exception 타입으로 지정
try:
    print(4 / 0)
except ZeroDivisionError:
    print("오류 발생2")

# try except 를 이용하면서 Exception 타입으로 지정해서 출력을 위해 익셉션을 변수로 바꿔줌
try:
    array = [1, 2, 3, 4]
    print(array[10])
except IndexError as e:
    print(e)
    print("오류 발생3")

# try except finally 를 이용해서 오류처리 finally는 오류가 나든 말든 실행
try:
    open("1.txt", "r", encoding="UTF-8")
except:
    print("오류 발생4")
finally:
    print("무조건 실행")

# pass를 통해서 exception을 회피할 수 있음.
try:
    open("1.txt", "r", encoding="UTF-8")
except:
    pass

#오류 발생 시키기

raise NotADirectoryError
