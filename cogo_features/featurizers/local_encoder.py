import tensorflow_hub as hub
import tensorflow as tf
import os

class LocalEncoder:
    def __init__(self):
        self.pretrained_encoder = hub.Module(os.environ['TFHUB_URL'])
        self.input_string = tf.placeholder(tf.string, shape=[None])
        self.encoding = self.pretrained_encoder(self.input_string)
        self.session = tf.Session()
        self.session.run([tf.global_variables_initializer(), tf.tables_initializer()])


    def encode(self, text):
        return self.session.run(self.encoding, {self.input_string: [text]})[0]
