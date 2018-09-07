# Python type
# Metaclass

>>> type(object)
<class 'type'>

>>> type(type)
<class 'type'>

>>> type.__class__
<class 'type'>

>>> type.__new__
<built-in method __new__ of type object at 0x5074BDC0>

>>> isinstance(object, object)
True

>>> isinstance(type, object)
True

>>> type(1)
<class 'int'>

>>> type(type(1))
<class 'type'>

>>> type(list())
<class 'list'>

>>> type(list)
<class 'type'>
