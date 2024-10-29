def sys(num, sys1, sys2):
	num10 = 0
	sys1 = int(sys1)
	sys2 = int(sys2)
	a = ''.join([chr(__) for __ in range(48, 58)] + [chr(_) for _ in range(65, 91)] + [chr(___) for ___ in range(97, 123)])
	if sys1 != 10:
		for i in range(len(num)):
			num10 += a.index(num[i]) * sys1 ** (len(num) - i - 1)
		num = num10
	else:
		num = int(num)
	if num < sys2:
	    return a[num]
	else:
	    return sys(num // sys2, 10, sys2) + a[num % sys2]


print(sys(input(), input(), input()))
