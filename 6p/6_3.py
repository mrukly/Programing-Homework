n, m = map(int, input().split('x'))
k = int(input())

if k % m == 0 and k // m < n:
    print('да')
elif k % n == 0 and k // n < m:
    print('да')
else:
    print('нет')
