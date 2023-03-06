# Softeer_레벨1_근무 시간
import sys

ans = 0
for i in range(5):
    T = str(sys.stdin.readline())
    h1 = int(T.split(' ')[0].split(":")[0])
    m1 = int(T.split(' ')[0].split(":")[1])
    h2 = int(T.split(' ')[1].split(":")[0])
    m2 = int(T.split(' ')[1].split(":")[1])

    ans += (h2 - h1)*60
    ans += (m2 - m1)

print(ans)
