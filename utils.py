import numpy as np
import time


def timer(secs):
	for i in range(1, secs + 1):
		print('%s...' % i)
		time.sleep(1)


def load_data(filename, count):
	"""Filename example: 'data/raw/training_data_%s.npy'
	Arguments:
		filename str

	Returns:
		data - np data
	"""
	data = []

	while True:
		try:
			print(filename % count)
			cur_data = list(np.load(filename % count))
			data.extend(cur_data)
			count += 1
		except Exception as e:
			print('No more files to load, returning...')
			break

	return data
