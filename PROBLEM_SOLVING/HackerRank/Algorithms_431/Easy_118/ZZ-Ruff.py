def chars_mix_up(a, b):
  new_a = a[0] + b[1] + a[2:]
  new_b = b[0] + a[1] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('123', '789'))


l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1]+(100,) for t in l])

x= [10,20,30,40]
for i in range(len(x)):
  print(x[i], end=' ')
print()
for i in x:
  print(str(i), end= ' ')