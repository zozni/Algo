# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 이 방법은 PyPy3으로 제출해야함.

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums = sorted(nums)

for i in range(N):
    print(nums[i])
