def valid(A, B):
    if A > B:
        A, B = B, A
    for i in range(A, B + 1):
        for c in str(i):
            if c not in "13489":
                break
        else:
            print(i, end=" ")

a = int(input("A: "))
b = int(input("B: "))
valid(a, b)
