str = "tester"
# 해당 문자 포함 개수
print(str.count('e'))

# 처음 만나는 해당 문자의 위치(인덱스) 찾기
print(str.find('e'))  # 1
print(str.find('j'))  # -1

# 문자열 삽입
print(','.join("abcdc"))

# 대문자로 바꾸기
print(str.upper())

# 소문자로 바꾸기
uppercase = "TEST"
print(uppercase.lower())

# 특정문자 지우기
blankStr = "    test     "
print("left")
print(blankStr.lstrip())
print("right")
print(blankStr.rstrip())
print("left right both")
print(blankStr.strip())

#문자열 바꾸기
str2 = "Life is Too Short"
print(str2.replace("Short", "Long"))

#문자열 나누기
str3 = "This is Long Time"
print(str3.split())