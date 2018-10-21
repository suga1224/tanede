#!/usr/bin/env python3
# -*= coding:utf-8 -*-

import mpu6050
import record
import watson
import learn
import echo
import sound

import time

#from multiprocessing import Pool
#from multiprocessing import Process

def tree_axis():
    t = mpu6050.set_xyz()
    return t

def reco():
    record.record_start()
    
def watson_start():
    w = watson.watson_request()
    return w

def tane():
    auto_text = learn.main()
    print(type(auto_text))
    text = str(auto_text)
    print(text)
    echo.text_read(auto_text)
    
if __name__ == "__main__":
    while True:
        n = tree_axis()
        print(n)
        if n == "ok":
            sound.sound_play("sound/move.wav")
            reco()
            word = watson_start()
            if "冬" in word:
                tane()
                time.sleep(1)
            else:
                sound.sound_play("sound/err.wav")
            