# 파일 생성
f = open("newFile.txt", "w", encoding="UTF-8")  # w는 쓰기 r는 읽기 a는 이어쓰기

for i in range(1, 111):
    # 파일에 쓰기
    f.write("{0}번째 입력.\n".format(i))
f.close()

# 파일 줄 단위로 읽기
f = open("newFile.txt", "r", encoding="UTF-8")  # w는 쓰기 r는 읽기 a는 이어쓰기
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# 파일 전체를 읽어서 가져옴
f = open("newFile.txt", "r", encoding="UTF-8")  # w는 쓰기 r는 읽기 a는 이어쓰기
print(f.readlines())
f.close()


# with 문을 쓰면 조금더 줄일 수 있음
with open("newFile.txt", "r", encoding="UTF-8") as f:
    print(f.readlines())