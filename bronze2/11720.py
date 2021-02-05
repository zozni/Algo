# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

a = int(input())
n = list(input())
sum = 0
for i in n:
    sum += int(i)
print(sum)