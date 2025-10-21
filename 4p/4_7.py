K, A, S = map(int, input().split())

winner = K

if A > winner:
  winner = A

if S > winner:
  winner = S

print(winner)
