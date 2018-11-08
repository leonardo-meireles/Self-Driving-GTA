from cv2 import cv2
import numpy as np
import utils
import image
import mss
import os
import time
from keys import KeyController
import logging


keys = KeyController()
keys.start()


filename = 'data/raw/training_data_%s.npy'

def collect(filename):
    """Uses mss to printscreen doing like 30FPS
    """
    # 800x600 windowed mode
    mon = {"top": 60, "left": 0, "width": 800, "height": 600}

    print('Collecting...')
    if os.path.isfile(filename):
        logging.info('File already exists, loading file...')
        training_data = list(np.load(filename))
    else:
        logging.info("File doesn't exists, creating a new one...")
        training_data = []

    # Screenshot object
    sct = mss.mss()
    utils.timer(5)
    while True:
        image = np.asarray(sct.grab(mon))
        # Converting to grayscale, reason much smaller then RGB(minus 2 D)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # Resizing image to 80x60waw
        image = cv2.resize(image, (160, 120))

        if keys.output:
            output = keys.output
            keys.output = None
            training_data.append([image, output])

        length_data = len(training_data)
        print(length_data)
        if not length_data % 500:
            print("Saving...")
            print(length_data)
            np.save(filename, training_data)
            print("Done Saving")


def show(file):
    data = np.load(file)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for d in data:
        output = np.zeros((90, 90), dtype=int)
        print('IMAGE: %s ==> OUTPUT %s' % (d[0], d[1]))

        d[0] = cv2.resize(d[0], (800, 600))

        if d[1][0]:
            cv2.putText(d[0], 'OUTPUT = A', (10, 550), font,
                        0.9, [0, 0, 0], 2, cv2.LINE_AA)
        elif d[1][1]:
            cv2.putText(d[0], 'OUTPUT = W', (10, 550), font,
                        0.9, [0, 0, 0], 2, cv2.LINE_AA)
        elif d[1][2]:
            cv2.putText(d[0], 'OUTPUT = D', (10, 550), font,
                        0.9, [0, 0, 0], 2, cv2.LINE_AA)

        cv2.imshow('window', d[0])
        
        time.sleep(0.03)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()


def main(version):
    #for i in range(3):
    #    show("training_data_%s.npy" % i)
    #show('data/balanced/balanced_data_mix_big.npy')
    collect(filename % version)


if __name__ == '__main__':
    main(os.sys.argv[1])
