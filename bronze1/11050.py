# 자연수 N과 정수 K가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)
