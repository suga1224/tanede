# -*- coding: utf-8 -*-

import os

def text_read(text):
    os.system('./AquesTalkPi ' +'*'+ text + '| aplay')
    print("calltext")

if __name__ == "__main__":
    text = "寒いのにアイスクリームを食べて温まる"
    text_read(text)