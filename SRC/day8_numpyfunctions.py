#Task 1

import numpy as np

np.random.seed(42)

scores = np.random.randint(50, 101, size=(5, 3))
means = scores.mean(axis=0)
centered_scores = scores - means

print(scores)
print(centered_scores)

#Task 2

import numpy as np

data = np.arange(24)
reshaped = data.reshape(4, 3, 2)
transposed = reshaped.transpose(0, 2, 1)

print(transposed.shape)
print(transposed)
