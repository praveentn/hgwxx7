'''
extract classes from a module
for eg. consider numpy
'''

# load libraries
import inspect
import numpy as np

# prints class name and object definition
for name, obj in inspect.getmembers(np):
    if inspect.isclass(obj):
        print(name, obj)

'''
AxisError <class 'numpy.core._internal.AxisError'>
ComplexWarning <class 'numpy.core.numeric.ComplexWarning'>
DataSource <class 'numpy.lib._datasource.DataSource'>
MachAr <class 'numpy.core.machar.MachAr'>
ModuleDeprecationWarning <class 'numpy._globals.ModuleDeprecationWarning'>
PackageLoader <class 'numpy._import_tools.PackageLoader'>
RankWarning <class 'numpy.lib.polynomial.RankWarning'>
Tester <class 'numpy.testing.nose_tools.nosetester.NoseTester'>
TooHardError <class 'numpy.core._internal.TooHardError'>
VisibleDeprecationWarning <class 'numpy._globals.VisibleDeprecationWarning'>
_NoValue <class 'numpy._globals._NoValue'>
bool <class 'bool'>
bool8 <class 'numpy.bool_'>
bool_ <class 'numpy.bool_'>
broadcast <class 'numpy.broadcast'>
busdaycalendar <class 'numpy.busdaycalendar'>
byte <class 'numpy.int8'>
bytes0 <class 'numpy.bytes_'>
bytes_ <class 'numpy.bytes_'>
cdouble <class 'numpy.complex128'>
cfloat <class 'numpy.complex128'>
character <class 'numpy.character'>
chararray <class 'numpy.core.defchararray.chararray'>
clongdouble <class 'numpy.complex128'>
clongfloat <class 'numpy.complex128'>
complex <class 'complex'>
complex128 <class 'numpy.complex128'>
complex64 <class 'numpy.complex64'>
complex_ <class 'numpy.complex128'>
complexfloating <class 'numpy.complexfloating'>
csingle <class 'numpy.complex64'>
datetime64 <class 'numpy.datetime64'>
double <class 'numpy.float64'>
dtype <class 'numpy.dtype'>
errstate <class 'numpy.core.numeric.errstate'>
finfo <class 'numpy.core.getlimits.finfo'>
flatiter <class 'numpy.flatiter'>
flexible <class 'numpy.flexible'>
float <class 'float'>
float16 <class 'numpy.float16'>
float32 <class 'numpy.float32'>
float64 <class 'numpy.float64'>
float_ <class 'numpy.float64'>
floating <class 'numpy.floating'>
format_parser <class 'numpy.core.records.format_parser'>
generic <class 'numpy.generic'>
half <class 'numpy.float16'>
iinfo <class 'numpy.core.getlimits.iinfo'>
inexact <class 'numpy.inexact'>
int <class 'int'>
int0 <class 'numpy.int64'>
int16 <class 'numpy.int16'>
int32 <class 'numpy.int32'>
int64 <class 'numpy.int64'>
int8 <class 'numpy.int8'>
int_ <class 'numpy.int32'>
intc <class 'numpy.int32'>
integer <class 'numpy.integer'>
intp <class 'numpy.int64'>
long <class 'int'>
longcomplex <class 'numpy.complex128'>
longdouble <class 'numpy.float64'>
longfloat <class 'numpy.float64'>
longlong <class 'numpy.int64'>
matrix <class 'numpy.matrixlib.defmatrix.matrix'>
memmap <class 'numpy.core.memmap.memmap'>
ndarray <class 'numpy.ndarray'>
ndenumerate <class 'numpy.lib.index_tricks.ndenumerate'>
ndindex <class 'numpy.lib.index_tricks.ndindex'>
nditer <class 'numpy.nditer'>
number <class 'numpy.number'>
object <class 'object'>
object0 <class 'numpy.object_'>
object_ <class 'numpy.object_'>
poly1d <class 'numpy.lib.polynomial.poly1d'>
recarray <class 'numpy.recarray'>
record <class 'numpy.record'>
short <class 'numpy.int16'>
signedinteger <class 'numpy.signedinteger'>
single <class 'numpy.float32'>
singlecomplex <class 'numpy.complex64'>
str <class 'str'>
str0 <class 'numpy.str_'>
str_ <class 'numpy.str_'>
string_ <class 'numpy.bytes_'>
timedelta64 <class 'numpy.timedelta64'>
ubyte <class 'numpy.uint8'>
ufunc <class 'numpy.ufunc'>
uint <class 'numpy.uint32'>
uint0 <class 'numpy.uint64'>
uint16 <class 'numpy.uint16'>
uint32 <class 'numpy.uint32'>
uint64 <class 'numpy.uint64'>
uint8 <class 'numpy.uint8'>
uintc <class 'numpy.uint32'>
uintp <class 'numpy.uint64'>
ulonglong <class 'numpy.uint64'>
unicode <class 'str'>
unicode_ <class 'numpy.str_'>
unsignedinteger <class 'numpy.unsignedinteger'>
ushort <class 'numpy.uint16'>
vectorize <class 'numpy.lib.function_base.vectorize'>
void <class 'numpy.void'>
void0 <class 'numpy.void'>
'''


# get all classes of current module
import sys

# set current module to sys modules
current_module = sys.modules[__name__]

# get all classes
def get_classes(mod):
    '''
	pass required module as param
	returns/prints the classes
	'''
    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj):
            print(name, obj)


# call the function
get_classes(current_module)
# __loader__ <class '_frozen_importlib.BuiltinImporter'>

# set current module to pandas DataFrame
import pandas as pd
current_module = pd.DataFrame

# call the function
get_classes(current_module)

'''
>>> current_module
<class 'pandas.core.frame.DataFrame'>
>>> get_classes(current_module)
__class__ <class 'type'>
_constructor_sliced <class 'pandas.core.series.Series'>
plot <class 'pandas.plotting._core.FramePlotMethods'>
>>>
'''
