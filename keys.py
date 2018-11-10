import logging
from pykeyboard import PyKeyboard, PyKeyboardEvent
import time

class KeyController(PyKeyboardEvent):
    output = None

    def tap(self, keycode, character, press):
        if press:
            if character == 'a':
                self.output = [1, 0, 0]
            elif character == 'w':
                self.output = [0, 1, 0]
            elif character == 'd':
                self.output = [0, 0, 1]
            elif character == 'T':
                self.output = 'pause'
            elif character == 'Q':
                self.output = 'quit'


t_time = 0.065

key = PyKeyboard()


def cheats():
    key.press_keys(['I', 'C', 'I', 'K', 'P', 'Y', 'H'])

def straight():
    key.press_key(character='w')
    key.release_key(character='a')
    key.release_key(character='d')
    time.sleep(t_time/2)
    key.release_key(character='w')


def dk_straight():
    key.press_key(character='w')
    key.release_key(character='a')
    key.release_key(character='d')
    time.sleep(t_time/4)
    key.release_key(character='w')


def left():
    
    key.press_key(character='a')
    key.release_key(character='d')
    
    time.sleep(t_time)
    key.release_key(character='a')
    
    key.press_key(character='w')
    time.sleep(t_time/3.5)
    key.release_key(character='w')
    
    #key.release_key(character='w')
    

def right():
    key.press_key(character='d')
    key.release_key(character='a')
    
    time.sleep(t_time)
    key.release_key(character='d')
    key.press_key(character='w')
    time.sleep(t_time/3.5)
    key.release_key(character='w')
    

def stop():
    key.release_key(character='w')
    key.release_key(character='d')
    key.release_key(character='a')
    key.press_key(character='s')
    time.sleep(t_time/4)
    key.release_key(character='s')
