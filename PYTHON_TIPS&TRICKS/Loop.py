odd_square = []
for k in range(50):
    if k % 2 == 1:
      odd_square.append(k**2)
print(odd_square)


odd_squares = [k**2 for k in range(51) if k % 2 == 1]
print(odd_squares)