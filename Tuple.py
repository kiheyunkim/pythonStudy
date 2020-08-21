# 튜플은 리스트와 다르게 1개의 요소만을 가질때는 콤마를 붙이고, 괄호를 생략해도 된다
# 투플은 변경이 안됨 (삭제, 변경)

# 튜플 선언
tuple1 = ()
tuple2 = (1,)
tuple3 = (1, 2, 3)
tuple4 = 1, 2, 3
tuple5 = ('a', 'b', ('ab', 'cd'))

# 삭제 편집은 불가
# del tuple3[3] # 삭제 불가
# tuple3[3] = 5 # 편집 불가

# 인덱싱
print(tuple4[2])

# 슬라이싱
print(tuple5[1:3])

# 투플 더하기
print(tuple3 + tuple4)

# 투플 곱하기
print(tuple5 * 3)

# 투플 길이 구하기
print(len(tuple2))
