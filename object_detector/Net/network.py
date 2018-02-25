import tensorflow as tf
import numpy as np
from cprint import *

import six.moves.urllib as urllib
import sys
import tarfile
import zipfile
import os
import time

from utils import label_map_util

from utils import visualization_utils as vis_util

import cv2

class Detection_Network(object):

	def __init__(self):

		MODEL_NAME = 'Net/' + 'ssd_mobilenet_v1_coco_2017_11_17'
		# the class is called from the root dir of the project!
		MODEL_FILE = MODEL_NAME + '.tar.gz'

		# path to the frozen graph (inside the model).
 		PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'


		# path to the labels (id-name association).
		PATH_TO_LABELS = os.path.join('Net/data', 'mscoco_label_map.pbtxt')
		NUM_CLASSES = 90

		label_map = label_map_util.load_labelmap(PATH_TO_LABELS) # loads the labels map.
		categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES)
		self.category_index = label_map_util.create_category_index(categories)
		print(self.category_index)

		detection_graph=tf.Graph()
		with detection_graph.as_default():
			od_graph_def = tf.GraphDef()
			with open(PATH_TO_CKPT, 'rb') 	as fid:
				serialized_graph = fid.read()
				od_graph_def.ParseFromString(serialized_graph)
				tf.import_graph_def(od_graph_def, name='')

		self.sess = tf.Session(graph=detection_graph)
		self.image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
		self.detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
		self.detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
		self.detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
		self.num_detections = detection_graph.get_tensor_by_name('num_detections:0')
		print("Network Created")
        
		self.input_image=None
		print(self.input_image)
		self.output_image=None
	
	def predict(self):
		image=self.input_image
		if image is not None:
			sess=self.sess
			boxes,detection_scores,detection_classes,num_detections=sess.run([self.detection_boxes,self.detection_scores,self.detection_classes,self.num_detections],feed_dict={image_tensor:image})
			# visualization of the results.
			vis_util.visualize_boxes_and_labels_on_image_array(
				image_np,
				np.squeeze(detection_boxes),
				np.squeeze(detection_classes).astype(np.int32),
				np.squeeze(detection_scores),
				self.category_index,
				use_normalized_coordinates=True,
				line_thickness=8)
		self.output_image=image
	





	
		
