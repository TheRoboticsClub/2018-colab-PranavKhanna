class GUI(QtWidgets.QWidget):

    updGUI = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        ''' GUI class creates the GUI that we're going to use to
        preview the live video as well as the results of the real-time
        classification.
        '''

        self.network = Detection_Network()

        self.t_network = ThreadNetwork(self.network)
        self.t_network.start()

        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("JdeRobot-TensorFlow detector")
        self.resize(1000, 600)
        self.move(150, 50)
        self.setWindowIcon(QtGui.QIcon('resources/jderobot.png'))
        self.updGUI.connect(self.update)

        # Original image label.
        self.im_label = QtWidgets.QLabel(self)
        self.im_label.resize(450, 350)
        self.im_label.move(25, 90)
        self.im_label.show()

        # Predicted image label.
        self.im_pred_label = QtWidgets.QLabel(self)
        self.im_pred_label.resize(450, 350)
        self.im_pred_label.move(525, 90)
        self.im_pred_label.show()

        # Button for configuring detection flow
        button = QtWidgets.QPushButton(self)
        button.move(450, 500)
        button.setText('Toggle\nDetection')
        button.clicked.connect(self.toggleNetwork)