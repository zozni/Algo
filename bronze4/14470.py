# JOI 군은 식사 준비를 위해 A℃의 고기를 전자레인지로 B℃까지 데우려고 한다.
# 고기는 온도가 0℃보다 낮을 때 얼어 있고, 0℃보다 높을 때는 얼어 있지 않다.
# 온도가 정확히 0℃일 때 고기는 얼어 있을 수도, 얼어 있지 않을 수도 있다.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    print(abs(a)*c+d+b*e)
else:
    print((b-a)*e)
