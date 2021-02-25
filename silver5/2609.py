# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

n, m = map(int, input().split())


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def lcm(n, m):
    g = gcd(n, m)
    return int(g*(n/g)*(m/g))


print(gcd(n, m))
print(lcm(n, m))
