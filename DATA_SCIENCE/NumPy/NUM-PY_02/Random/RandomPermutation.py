from numpy import random
import numpy as np

x = np.array([1, 2, 3, 4, 5])
random.shuffle(x)                # Shuffle = অদলবদল ata original array ar element gulo k positionally change kore dey
print(x)
print(random.permutation(x))     # permutation ber kore but original array k kono change kore na

k = np.arange(1,6)
print(random.permutation(k))