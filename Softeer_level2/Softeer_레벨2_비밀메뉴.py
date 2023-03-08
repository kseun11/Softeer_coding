# Softeer_레벨2_비밀 메뉴
M, N, K = map(int, input().split())
S1 = ''.join(list(input().split()))
S2 = ''.join(list(input().split()))

if S1 in S2:
    print('secret')
else:
    print('normal')
