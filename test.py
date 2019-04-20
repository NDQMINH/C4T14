# n1, n2 = map(int, input().split())
s1, s2 = input().split()
t = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i, x1 in enumerate(s1, 1):
    for j, x2 in enumerate(s2, 1):
        if x1 == x2:
            t[i][j] = t[i - 1][j - 1] + 1
        else:
            t[i][j] = max(t[i][j - 1], t[i - 1][j])

print(t[-1][-1])
