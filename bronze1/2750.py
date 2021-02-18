# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())
m = []

for i in range(n):
    m.append(int(input()))

# 버블정렬
for i in range(len(m)):
    for j in range(len(m)):
        if m[i] < m[j]:
            m[i], m[j] = m[j], m[i]

for n in m:
    print(n)
