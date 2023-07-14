from PIL import ImageGrab
import os
import time

x_pad = 740
y_pad = 288

def screenGrab():
    box = (x_pad, y_pad, 1166, 716)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' +str(int(time.time())) + '.png', 'PNG')
    return im

def main():
    im = screenGrab()

if __name__ == '__main__':
    main()
