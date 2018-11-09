import numpy as np
from collections import Counter
from random import shuffle
import sys
from cv2 import cv2
from utils import load_data

def main():
    train_data = load_data('data/raw/training_data_%s.npy', 0)
    train_data += load_data('data/gta5/training_data-%s-balanced.npy', 1)
    
    print(len(train_data))

    A = []
    D = []
    W = []

    # Shuffling for decreasing the bias
    shuffle(train_data)

    for data in train_data:
        image = cv2.resize(data[0], (160, 120))
        choice = data[1]

        if choice == [1, 0, 0]:
            A.append([image, choice])
        elif choice == [0, 1, 0]:
            W.append([image, choice])
        elif choice == [0, 0, 1]:
            D.append([image, choice])
        else:
            print('No matches')

    W = W[:len(A)][:len(D)]
    A = A[:len(W)]
    D = D[:len(W)]

    print(len(W), len(A), len(D))

    final_data = W + A + D
    shuffle(final_data)

    total_size = len(final_data)
    size_partition = int(0.2*total_size)

    part = 0
    while (total_size > 0) and part*size_partition <= total_size:
        np.save('data/balanced/balanced_data_%s.npy' % part,
                final_data[part*size_partition: (part*size_partition) + size_partition])
        part += 1


if __name__ == '__main__':
    main()
