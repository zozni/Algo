# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input())
for i in range(0,n):
    print(" "*(n-1-i) + "*"*(i+1))
for k in range(1,n):
    print(" "*k + "*"*(n-k))