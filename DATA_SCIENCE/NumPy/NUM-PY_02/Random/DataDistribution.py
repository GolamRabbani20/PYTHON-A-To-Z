from numpy import random
x = random.choice([3,5,7,9],p=[0.1, 0.3, 0.4, 0.2], size=(100))
print(x)

print("\n2DDD....................................................")
m = random.choice([3,5,7,9],p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(m)