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


def rom(num):
	num = int(num)

	e = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
	d = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
	s = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
	t = ['', 'M', 'MM', 'MMM', 'MMMM']
	
	rt, num = t[num // 1000], num % 1000
	rs, num = s[num // 100], num % 100
	rd, num = d[num // 10], num % 10
	re = e[num]

	return rt + rs + rd + re

def result(num, sys1, sys2):
	if sys2 == 'r':
		return rom(sys(num, sys1, 10))
	else:
		return sys(num, sys1, sys2)

print('Перевод чисел, больших 4999 в римские не поддерживается. Отрицательные системы счисления тоже. Поддерживаются только заглавные и строчные латинские буквы, и цифры. Отсутвует проверка корректности ввода ')
print(result(input('Число '), input('Его система счисления '), input('Итоговая система счисления. r для римских цифр ')))
