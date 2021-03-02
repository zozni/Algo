# 자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.
s = input()
if s[1] == '0':
    print(10 + int(s[2:]))
else:
    print(int(s[0]) + int(s[1:]))
