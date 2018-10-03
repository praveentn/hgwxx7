E:\Python>python.exe
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> tf.session()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'tensorflow' has no attribute 'session'
>>> tf.Session()
2018-10-03 10:21:40.779195: I T:\src\github\tensorflow\tensorflow\core\platform\cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
<tensorflow.python.client.session.Session object at 0x0000020816B24DA0>

>>> s = tf.Session()
>>> s
<tensorflow.python.client.session.Session object at 0x0000020816B24DA0>

