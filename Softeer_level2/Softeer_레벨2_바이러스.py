# Softeer_레벨2_바이러스
import sys

K, P, N = map(int, sys.stdin.readline().split())

for i in range(N):
    K *= P
    K %= 1000000007
print(K)
