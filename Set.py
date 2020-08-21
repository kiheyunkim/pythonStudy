# SET 중복을 허용하지 않음, 순서가 없음
set1 = set([1, 2, 3])
print(set1)
set2 = set("HELLO")
print(set2)
set3 = {1, 3, 5, 7}

# print(set1[0])  #불가능
list = list(set1)
print(list[0])  # 변환하면 가능

print(set3)

# 집합 연산
# 교집합
print(set1 & set3)
print(set1.intersection(set3))

# 합집합
print(set1 | set3)
print(set1.union(set3))

# 차집합
print(set1 - set3)
print(set3 - set1)
print(set1.difference(set3))
print(set3.difference(set1))

# 값추가
print(set1)
set1.add(10);
print(set1)

# 값 여러개 추가
print(set2)
set2.update([1, 2, 3, 4, 5, 6, 7, 8, 9]);
print(set2)

# 특정값 제거
print(set3)
set3.remove(5)
print(set3)
