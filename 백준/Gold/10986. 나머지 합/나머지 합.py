n, m = map(int, input().split())
numbers = list(map(int, input().split()))
S = [0] * n
C = [0] * m # 모듈러 연산
answer = 0
S[0] = numbers[0]

for i in range(1, n):
  S[i] = S[i - 1] + numbers[i]
  
for i in range(n):
  if S[i] % m == 0:
    answer += 1
  C[S[i] % m] += 1
  
for i in range(m):
  if C[i] != 0:
    answer += C[i] * (C[i] - 1) / 2

print(int(answer))