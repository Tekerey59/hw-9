num1 = input()
num2 = input()
sys = int(input())

a = ''.join([chr(__) for __ in range(48, 58)] + [chr(_) for _ in range(65, 91)] + [chr(___) for ___ in range(97, 123)])

n1 = []
n2 = []
res = []
add = 0
final = ''

if len(num1) > len(num2):
    num2 = '0' * (len(num1) - len(num2)) + num2
else:
    num1 = '0' * (len(num2) - len(num1)) + num1

for i in num1:
    n1.append(a.index(i))

for i in num2:
    n2.append(a.index(i))

for i in range(len(n1)):
    tmp = n1[len(n1) - i - 1] + n2[len(n1) - i - 1] + add
    add = tmp // sys
    tmp = tmp % sys
    res.append(a[int(tmp)])
if add != 0:
    res.append(a[int(add)])

for u in res:
    final = u + final

print(final)