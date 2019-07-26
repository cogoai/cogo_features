import tensorflow_hub as hub
import tensorflow as tf
import os

class LocalEncoder:
    def __init__(self):
        print('****************')
        print('****************')
        print('loading local encoding modules')
        self.pretrained_encoder = hub.Module(os.environ['TFHUB_URL'])
        self.input_string = tf.placeholder(tf.string, shape=[None])
        self.encoding = self.pretrained_encoder(self.input_string)
        self.session = tf.Session()
        self.session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        print('****************')
        print('****************')


    def encode(self, text):
        print('local encoding.......')
        return self.session.run(self.encoding, {self.input_string: [text]})[0]
