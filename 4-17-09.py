n = int(input(''))
a = []

for i in range(n):
	a.append(i % 2 * -2 + 1)

print(*a)