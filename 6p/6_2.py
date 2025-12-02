a, b = map(float, input().split('x'))
c, d, e = map(float, input().split('x'))

if c <= a and d <= b:
    print('да')
elif c <= a and e <= b:
    print('да')
elif d <= a and c <= b:
    print('да')
elif d <= a and e <= b:
    print('да')
elif e <= a and c <= b:
    print('да')
elif e <= a and d <= b:
    print('да')
else:
    print('нет')
