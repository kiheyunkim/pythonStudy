# 입력
a = input()
print(a)

# 프롬프트와 함께 입력
b = input("숫자를 입력하세요: ")
print(b)

# 큰 따옴표(")로 둘러싸인 문자열은 + 연산과 동일
print("Hello" "my" "World")
print("Hello" + "my" + "World")

# 콤마를 쓰면 띄어쓰기가 됨.
print("Hello", "my", "World")

# 한줄에 출력
for i in range(0, 10):
    print(i, end=' ')
