numbers = list(map(int, input().split()))


def max_search(numbers):
    n = len(numbers)  # 입력 크기 n
    maxValue = numbers[0]  # 리스트의 첫 번째 값을 최대값으로 초기화
    for i in range(1, n):  # 1부터 n까지 반복 실행
        if numbers[i] > maxValue:  # 만약 이번 값이 최대값보다 크다면
            maxValue = numbers[i]  # 최대값을 i번째 값으로 변경
    return maxValue  # 설정된 최대값을 반환


print(max_search(numbers))
