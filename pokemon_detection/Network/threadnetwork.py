import tensorflow as tf
import numpy as np 
from network import Detection_Network
import threading


t_cycle = 400  # ms

class Thread_Network(object):

	def __init__(self,network):

		self.network = network
        threading.Thread.__init__(self)
    
    def run(self):
  
        while(True):
            start_time = datetime.now()
           	self.predicted_image = self.network.predict()

            end_time = datetime.now()

            dt = end_time - start_time
            dtms = ((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 +
                    dt.microseconds / 1000.0)

            if(dtms < t_cycle):
                time.sleep((t_cycle - dtms) / 1000.0)


