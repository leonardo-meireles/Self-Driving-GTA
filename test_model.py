import numpy as np
import cv2
import time
from models import alexnet
from utils import timer
import mss
import random
from keys import KeyController, right, straight, dk_straight, left, stop
import sys

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
BATCH_SIZE = 128
MODEL_NAME = 'gta_model_%s_%s_%s.tflearn'


keys = KeyController()
keys.start()

def main():
	model = alexnet(WIDTH, HEIGHT, LR)
	#model.load('trained_models/' + MODEL_NAME % ('alexnet', EPOCHS, DATA_TYPE))
	model.load('model/model.tflearn')    
	timer(5)

	# 800x600 windowed mode
	mon = {"top": 60, "left": 0, "width": 800, "height": 600}

	# Screenshot object
	sct = mss.mss()

	paused = False
	count_dk = 0
	count_st = 0
	
	while True:

		if not paused:
			image = np.asarray(sct.grab(mon))
			# Converting to grayscale, reason much smaller then RGB(minus 2 D)
			image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			# Resizing image to 80x60waw
			image = cv2.resize(image, (160, 120))

			prediction = model.predict([image.reshape(160, 120, 1)])[0]
			#print(prediction)
			#print(np.argmax(prediction))

		
			turn_thresh = .7
			fwd_thresh = 0.7

			if prediction[1] > fwd_thresh:
				count_dk = 0
				count_st += 1
				if count_st > 2:
					print('STOP ST')
					stop()
					count_st = 0

				print('STRAIGHT : %s' % (prediction[1]*100.0))
				straight()
			elif prediction[0] > turn_thresh:
				count_dk = 0
				count_st = 0
				
				print('LEFT : %s' % (prediction[0]*100.0))
				left()
			elif prediction[2] > turn_thresh:
				count_dk = 0
				count_st = 0
				
				print('RIGHT : %s' % (prediction[2]*100.0))
				right()
			else:
				count_dk += 1
				count_st = 0
				
				if count_dk > 4:
					print('STOP DK')
					stop()
					count_dk = 0

				print('DK : STRAIGHT')
				
				dk_straight()
			

			
		# p pauses game and can get annoying.
		if keys.output == 'pause':
			if paused:
				paused = False
			else:
				paused = True
				stop()
				#time.sleep(0.2)
		elif keys.output == 'quit':
			return True

if __name__ == '__main__':
	main()
