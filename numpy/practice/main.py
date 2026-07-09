import numpy as np


def random_arrray(shape, start, end):
	return np.random.randint(start, end, shape)


print(random_arrray((2, 3), 1, 100))