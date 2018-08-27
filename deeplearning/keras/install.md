# Installing Keras on Windows

### E:\Python>python -V

Python 3.6.3

---

### E:\Python>python -m pip install keras

Collecting keras

  Downloading https://files.pythonhosted.org/packages/34/7d/b1dedde8af99bd82f20ed7e9697aac0597de3049b1f786aa2aac3b9bd4da/Keras-2.2.2-py2.py3-none-any.whl (299kB)
    
Collecting keras-preprocessing==1.0.2 (from keras)

  Downloading https://files.pythonhosted.org/packages/71/26/1e778ebd737032749824d5cba7dbd3b0cf9234b87ab5ec79f5f0403ca7e9/Keras_Preprocessing-1.0.2-py2.py3-none-any.whl

Collecting pyyaml (from keras)

  Downloading https://files.pythonhosted.org/packages/4f/ca/5fad249c5032270540c24d2189b0ddf1396aac49b0bdc548162edcf14131/PyYAML-3.13-cp36-cp36m-win_amd64.whl (206kB)

Requirement already satisfied: six>=1.9.0 in e:\python\lib\site-packages (from keras) (1.11.0)

Requirement already satisfied: scipy>=0.14 in e:\python\lib\site-packages (from keras) (1.0.1)

Collecting keras-applications==1.0.4 (from keras)

  Downloading https://files.pythonhosted.org/packages/54/90/8f327deaa37a71caddb59b7b4aaa9d4b3e90c0e76f8c2d1572005278ddc5/Keras_Applications-1.0.4-py2.py3-none-any.whl (43kB)

Collecting h5py (from keras)

  Downloading https://files.pythonhosted.org/packages/12/6c/00c38c5ce9322f1cc421d93217c44739646a106c61859622eccc297a5c05/h5py-2.8.0-cp36-cp36m-win_amd64.whl (2.3MB)

Requirement already satisfied: numpy>=1.9.1 in e:\python\lib\site-packages (from keras) (1.14.2)

Installing collected packages: keras-preprocessing, pyyaml, h5py, keras-applications, keras

Successfully installed h5py-2.8.0 keras-2.2.2 keras-applications-1.0.4 keras-preprocessing-1.0.2 pyyaml-3.13

---

### E:\Python>python -c "import keras; print(keras.__version__)"

Using TensorFlow backend.

2.2.2

---

## Using Theano & Tensorflow backends for Keras

Ensure that you've theano and tensorflow installed.

### E:\Python>python -m pip install theano

Collecting theano

  Downloading https://files.pythonhosted.org/packages/99/dd/e43e3da5dd52f1468def552ed3e752bfd6958369478cc906ff07b21af92e/Theano-1.0.2.tar.gz (2.8MB)

Requirement already satisfied: numpy>=1.9.1 in e:\python\lib\site-packages (from theano) (1.14.2)

Requirement already satisfied: scipy>=0.14 in e:\python\lib\site-packages (from theano) (1.0.1)

Requirement already satisfied: six>=1.9.0 in e:\python\lib\site-packages (from theano) (1.11.0)

Building wheels for collected packages: theano

  Running setup.py bdist_wheel for theano ... done
  
  Stored in directory: C:\Users\praveen\AppData\Local\pip\Cache\wheels\87\1e\28\4a63195927452fb42d4ea6d1e5b3b1690409d66802cc9e1e6e
  
Successfully built theano

Installing collected packages: theano

Successfully installed theano-1.0.2

---

### E:\Python>python

Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.

>>> import keras

Using TensorFlow backend.

---

