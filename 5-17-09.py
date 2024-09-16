n = int(input(''))
a = []

for i in range(n):
	a.append(i % 4 + 1)

print(*a)