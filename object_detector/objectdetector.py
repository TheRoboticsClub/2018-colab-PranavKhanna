

import sys
import signal

from PyQt5 import QtWidgets

from Camera.camera import Camera
from Camera.threadcamera import ThreadCamera
from GUI.gui import GUI
from GUI.threadgui import ThreadGUI

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
     
    cam = Camera()
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.setCamera(cam)
    window.show()
    
    # Threading camera
    t_cam = ThreadCamera(cam)
    t_cam.start()
    
    # Threading GUI
    t_gui = ThreadGUI(window)
    t_gui.start()
    
    sys.exit(app.exec_())
    
