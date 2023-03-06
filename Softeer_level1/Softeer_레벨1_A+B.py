# Softeer_레벨1_A+B
import sys

T = int(sys.stdin.readline())

li = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    ans = a+b
    li.append(ans)
    
for i in range(T):
    print('Case #'+(str(i+1))+': '+(str(li[i])))
