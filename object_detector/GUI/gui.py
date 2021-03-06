import sys

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import cv2
from threadgui import ThreadGUI

from Net.network import Detection_Network
from Net.threadnetwork import ThreadNetwork


class GUI(QtWidgets.QWidget):

    updGUI = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        
        self.network = Detection_Network()

        self.t_network = ThreadNetwork(self.network)
        self.t_network.start()
            
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("JdeRobot-TensorFlow detector")
        self.resize(1800, 1200)
        self.move(450, 150)
        self.setWindowIcon(QtGui.QIcon('resources/jderobot.png'))
        self.updGUI.connect(self.update)

        # Original image label.
        self.im_label = QtWidgets.QLabel(self)
        self.im_label.resize(800, 600)
        self.im_label.move(50, 100)
        self.im_label.show()

        # Predicted image label.
        self.im_pred_label = QtWidgets.QLabel(self)
        self.im_pred_label.resize(800, 600)
        self.im_pred_label.move(950,100)
        self.im_pred_label.show()

        # Button for configuring detection flow
        button = QtWidgets.QPushButton(self)
        button.move(850, 800)   
        button.setText('Toggle\nDetection')
        button.clicked.connect(self.toggleNetwork)
    
    def setCamera(self,cam):
        self.cam=cam
    
    def update(self):

        im_prev=self.cam.getImage()        
        self.network.input_image=im_prev
        im_predicted=self.network.output_image
        im = QtGui.QImage(im_prev.data, im_prev.shape[1], im_prev.shape[0],
                          QtGui.QImage.Format_RGB888)
        im_scaled = im.scaled(self.im_label.size())

        self.im_label.setPixmap(QtGui.QPixmap.fromImage(im_scaled))
        
        im_predicted = QtGui.QImage(im_predicted.data, im_predicted.shape[1], im_prev.shape[0],
                                    QtGui.QImage.Format_RGB888)
        im_predicted_scaled = im_predicted.scaled(self.im_pred_label.size())

        self.im_pred_label.setPixmap(QtGui.QPixmap.fromImage(im_predicted_scaled))

    def toggleNetwork(self):
        self.t_network.activated = not self.t_network.activated
        print('Now is: {}'.format(self.t_network.activated))



