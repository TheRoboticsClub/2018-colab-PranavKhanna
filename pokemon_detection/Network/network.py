import tensorflow as tf
import numpy as np

class Detection_Network(object):

	def __init__(self):
		GRAPH_PATH = ' '  #to be filled later
		
        detection_graph=tf.Graph()
		with detection_graph.as_default():
			od_graph_def = tf.GraphDef()
			with open(GRAPH_PATH, 'rb') 	as fid:
				serialized_graph = fid.read()
				od_graph_def.ParseFromString(serialized_graph)
				tf.import_graph_def(od_graph_def, name='')

		self.sess = tf.Session(graph=detection_graph)
		self.detection_boxes = detection_graph.get_tensor_by_name("detection_boxes:0")
		self.detection_scores = detection_graph.get_tensor_by_name("detection_scores:0")
		self.detection_classes = detection_graph.get_tensor_by_name("detection_classes:0")
		self.image_tensor = detection_graph.get_tensor_by_name("image_tensor:0")
		

    def predict(self,image):
        
        image_np = image
        image_np = np.expand_dims(image_np,axis=0)
        sess = self.sess
        detection_boxes,detection_scores,detection_classes=sess.run([self.detection_boxes,self.detection_scores,self.detection_classes] , feed_dict={self.image_tensor:image_np})

        vis_util.visualize_boxes_and_labels_on_image_array(
				image_np,
				np.squeeze(detection_boxes),
				np.squeeze(detection_scores),
				use_normalized_coordinates=True,
				line_thickness=12)

        return image_np

        
 