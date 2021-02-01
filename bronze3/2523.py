# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n=int(input())
for i in range(1,n+1):
    print("*"*i)
for k in range(n-1,0,-1):
    print("*"*k)