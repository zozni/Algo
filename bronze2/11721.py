# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
# 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

s = input()
for i in range(0, len(s), 10):
    print(s[i:i+10])
