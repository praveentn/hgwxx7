# using iter basics

>>> iter('vanautu')
<str_iterator object at 0x02E27030>
>>> _ = iter('vanautu')
>>> next(_)
'v'
>>> next(_)
'a'
>>> next(_)
'n'
>>> next(_)
'a'
>>> next(_)
'u'
>>> next(_)
't'
>>> next(_)
'u'
>>> next(_)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
