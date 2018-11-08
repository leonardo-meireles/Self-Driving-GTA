import numpy as np
from models.alexnet import alexnet
import sys
from utils import load_data

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 15


def main(id):
    model = alexnet(WIDTH, HEIGHT, LR)
    train_data = load_data('data/balanced/balanced_data_%s.npy')
        
    for i in range(EPOCHS):
        
        size_test = int(0.1*len(train_data)) 
        print('TEST SIZE : %s' % size_test)
        train = train_data[:-size_test]
        test = train_data[-size_test:]

        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=500, show_metric=True, run_id='gta_%s_%s_%s' % ('alexnet',EPOCHS, id))
        
        model.save('trained_models/model.tflearn')

        # tensorboard --logdir=foo:C:/path/to/log

if __name__ == '__main__':
    main(sys.argv[1])
