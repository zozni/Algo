# 세연이네 학교 운동장은 아래와 같다.
# 위의 그림에서 영역 A와 B는 반원이며, 영역 C는 직사각형이다.
# 영역 C의 가로의 길이를 d1, 영역 A의 반지름의 길이 d2의 값이 주어지면 운동장의
# 한 바퀴 둘레를 알아내는 프로그램을 작성하시오.
# (단, 이 문제에서는 π (원주율)의 값을 3.141592라고 한다.)
d1, d2 = int(input()), int(input())
print((d1+d2*3.141592)*2)
