# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

N = int(input())
multi = 1

if N == 0:
    print("1")
else:
    for i in range(1, N+1):
        multi = multi * i
    print(multi)
