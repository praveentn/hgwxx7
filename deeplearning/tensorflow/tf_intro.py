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

# placeholder
>>> x = tf.placeholder(tf.float32, shape=[2,2])
>>> x
<tf.Tensor 'Placeholder:0' shape=(2, 2) dtype=float32>
>>>

# identity
>>> y = tf.identity(x)
>>> y
<tf.Tensor 'Identity:0' shape=(2, 2) dtype=float32>
>>>

# load numpy
>>> import numpy as np

>>> x_vals = np.random.rand(2,2)
>>> x_vals
array([[0.97882811, 0.60712575],
       [0.18916714, 0.35782924]])
>>>

# tf run
>>> s.run(y, feed_dict={x: x_vals})
array([[0.97882813, 0.60712576],
       [0.18916714, 0.35782924]], dtype=float32)
>>>


