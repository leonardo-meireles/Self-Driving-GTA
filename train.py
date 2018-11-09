import numpy as np
from models import alexnetAdam, alexnet
import sys
from utils import load_data
import tensorflow as tf

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
BATCH_SIZE = 64


config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allocator_type = 'BFC'
config.gpu_options.per_process_gpu_memory_fraction = 0.80
config.gpu_options.allow_growth = True

def main(id, n_files):
    n_files = int(n_files)
    model = alexnet(WIDTH, HEIGHT, LR, BATCH_SIZE)
    train_data = load_data('data/balanced/balanced_data_%s.npy', 0)
    
    for i in range(EPOCHS):
        
        size_test = int(0.1*len(train_data))
        train = train_data[:-size_test]
        test = train_data[-size_test:]

        X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0]
                           for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
                      snapshot_step=500, show_metric=True, run_id='model_%s_%s_%s' % ('alexnetAdam', EPOCHS, id))

        model.save('model/model.tflearn')

        # tensorboard --logdir=foo:C:/path/to/log


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
