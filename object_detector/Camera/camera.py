import os
import sys
import random
import traceback
import threading

import cv2
import numpy as np
import tensorflow as tf
from Net.network import Detection_Network
import config
import comm 


class Camera(object):

    def __init__(self):
        try:
            cfg = config.load(sys.argv[1])
        except IndexError:
            raise SystemExit('Missing YML file. Usage: python2 objectdetector.py objectdetector.yml')
        self.lock = threading.Lock()
        try:
            jdrc = comm.init(cfg,'ObjectDetector')
            self.cam=jdrc.getCameraClient('ObjectDetector.Camera')
            if(self.cam.hasproxy()):
                self.im = self.cam.getImage()
                self.im_height = self.im.height
                self.im_width = self.im.width
                print(str(self.im_height)+" "+str(self.im_width))
            else:
                print("No camera interface is connected")
                exit()

        except:
            traceback.print_exc()
            exit()
            status = 1
    def getImage(self):
        if self.cam:
            self.lock.acquire()
            im = np.zeros((self.im_height,self.im_width,3),dtype=np.uint8)
            im = np.frombuffer(self.im.data,dtype=np.uint8)
            im = np.reshape(im,(self.im_height,self.im_width,3))
            self.lock.release()

            return im
    def update(self):
        if self.cam:
            self.lock.acquire()
            self.im = self.cam.getImage()
            self.im_height = self.im.height
            self.im_width = self.im.width
            self.lock.release()
    

    













