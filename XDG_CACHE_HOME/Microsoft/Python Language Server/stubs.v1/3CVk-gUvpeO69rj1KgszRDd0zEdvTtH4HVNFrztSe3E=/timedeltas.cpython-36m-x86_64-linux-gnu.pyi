import builtins as _mod_builtins
import datetime as _mod_datetime
import importlib._bootstrap as _mod_importlib__bootstrap
import pandas._libs.tslibs.nattype as _mod_pandas__libs_tslibs_nattype

Components = _mod_importlib__bootstrap.Components
NaT = _mod_pandas__libs_tslibs_nattype.NaTType()
class Timedelta(_Timedelta):
    "\n    Represents a duration, the difference between two dates or times.\n\n    Timedelta is the pandas equivalent of python's ``datetime.timedelta``\n    and is interchangeable with it in most cases.\n\n    Parameters\n    ----------\n    value : Timedelta, timedelta, np.timedelta64, string, or integer\n    unit : string, {'ns', 'us', 'ms', 's', 'm', 'h', 'D'}, optional\n        Denote the unit of the input, if input is an integer. Default 'ns'.\n    days, seconds, microseconds,\n    milliseconds, minutes, hours, weeks : numeric, optional\n        Values for construction in compat with datetime.timedelta.\n        np ints and floats will be coereced to python ints and floats.\n\n    Notes\n    -----\n    The ``.value`` attribute is always in ns.\n\n    "
    def __abs__(self):
        return Timedelta()
    
    def __add__(self, other):
        return Timedelta()
    
    __class__ = Timedelta
    __dict__ = {}
    def __divmod__(self, other):
        return (0, 0)
    
    def __floordiv__(self, other):
        return 0
    
    def __init__(self, *args, **kwargs):
        "\n    Represents a duration, the difference between two dates or times.\n\n    Timedelta is the pandas equivalent of python's ``datetime.timedelta``\n    and is interchangeable with it in most cases.\n\n    Parameters\n    ----------\n    value : Timedelta, timedelta, np.timedelta64, string, or integer\n    unit : string, {'ns', 'us', 'ms', 's', 'm', 'h', 'D'}, optional\n        Denote the unit of the input, if input is an integer. Default 'ns'.\n    days, seconds, microseconds,\n    milliseconds, minutes, hours, weeks : numeric, optional\n        Values for construction in compat with datetime.timedelta.\n        np ints and floats will be coereced to python ints and floats.\n\n    Notes\n    -----\n    The ``.value`` attribute is always in ns.\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __inv__(self):
        pass
    
    def __mod__(self, other):
        return Timedelta()
    
    def __mul__(self, other):
        return Timedelta()
    
    def __neg__(self):
        return Timedelta()
    
    def __pos__(self):
        return Timedelta()
    
    def __radd__(self, other):
        return Timedelta()
    
    def __rdivmod__(self, other):
        return (0, 0)
    
    def __reduce__(self):
        return ''; return ()
    
    def __rfloordiv__(self, other):
        return Timedelta()
    
    def __rmod__(self, other):
        return Timedelta()
    
    def __rmul__(self, other):
        return Timedelta()
    
    def __rsub__(self, other):
        return Timedelta()
    
    def __rtruediv__(self, other):
        return Timedelta()
    
    def __setstate__(self, state):
        return None
    
    def __sub__(self, other):
        return Timedelta()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, other):
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _round(self, freq, rounder):
        pass
    
    def ceil(self, freq):
        '\n        return a new Timedelta ceiled to this resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the ceiling resolution\n        '
        pass
    
    def floor(self, freq):
        '\n        return a new Timedelta floored to this resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the flooring resolution\n        '
        pass
    
    max = Timedelta()
    min = Timedelta()
    def round(self, freq):
        '\n        Round the Timedelta to the specified resolution\n\n        Returns\n        -------\n        a new Timedelta rounded to the given resolution of `freq`\n\n        Parameters\n        ----------\n        freq : a freq string indicating the rounding resolution\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        '
        pass
    

class _Timedelta(_mod_datetime.timedelta):
    __array_priority__ = 100
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = _Timedelta
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce_cython__(self):
        pass
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate_cython__(self):
        pass
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _d(self):
        pass
    
    def _ensure_components(self):
        '\n        compute the components\n        '
        pass
    
    @property
    def _h(self):
        pass
    
    def _has_ns(self):
        pass
    
    @property
    def _m(self):
        pass
    
    @property
    def _ms(self):
        pass
    
    @property
    def _ns(self):
        pass
    
    def _repr_base(self):
        '\n\n        Parameters\n        ----------\n        format : None|all|sub_day|long\n\n        Returns\n        -------\n        converted : string of a Timedelta\n\n        '
        pass
    
    @property
    def _s(self):
        pass
    
    @property
    def _us(self):
        pass
    
    @property
    def asm8(self):
        ' return a numpy timedelta64 array view of myself '
        pass
    
    @property
    def components(self):
        ' Return a Components NamedTuple-like '
        pass
    
    @property
    def delta(self):
        "\n        Return the timedelta in nanoseconds (ns), for internal compatibility.\n\n        Returns\n        -------\n        int\n            Timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 42 ns')\n        >>> td.delta\n        86400000000042\n\n        >>> td = pd.Timedelta('3 s')\n        >>> td.delta\n        3000000000\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.delta\n        3005000\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.delta\n        42\n        "
        pass
    
    @property
    def freq(self):
        pass
    
    @property
    def is_populated(self):
        pass
    
    def isoformat(self):
        "\n        Format Timedelta as ISO 8601 Duration like\n        ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the\n        values. See https://en.wikipedia.org/wiki/ISO_8601#Durations\n\n        .. versionadded:: 0.20.0\n\n        Returns\n        -------\n        formatted : str\n\n        Notes\n        -----\n        The longest component is days, whose value may be larger than\n        365.\n        Every component is always included, even if its value is 0.\n        Pandas uses nanosecond precision, so up to 9 decimal places may\n        be included in the seconds component.\n        Trailing 0's are removed from the seconds component after the decimal.\n        We do not 0 pad components, so it's `...T5H...`, not `...T05H...`\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,\n        ...                   milliseconds=10, microseconds=10, nanoseconds=12)\n        >>> td.isoformat()\n        'P6DT0H50M3.010010012S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(days=500.5).isoformat()\n        'P500DT12H0MS'\n\n        See Also\n        --------\n        Timestamp.isoformat\n        "
        pass
    
    @property
    def nanoseconds(self):
        "\n        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.\n       \n        Returns\n        -------\n        int\n            Number of nanoseconds.\n\n        See Also\n        --------\n        Timedelta.components : Return all attributes with assigned values\n            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,\n            nanoseconds).\n\n        Examples\n        --------\n        **Using string input**\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.nanoseconds\n        42\n\n        **Using integer input**\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.nanoseconds\n        42\n        "
        pass
    
    @property
    def resolution(self):
        ' return a string representing the lowest resolution that we have '
        pass
    
    def to_pytimedelta(self):
        '\n        return an actual datetime.timedelta object\n        note: we lose nanosecond resolution if any\n        '
        pass
    
    def to_timedelta64(self):
        " Returns a numpy.timedelta64 object with 'ns' precision "
        pass
    
    def total_seconds(self):
        '\n        Total duration of timedelta in seconds (to ns precision)\n        '
        pass
    
    @property
    def value(self):
        pass
    
    def view(self):
        ' array view compat '
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/enliai/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/_libs/tslibs/timedeltas.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.timedeltas'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle__Timedelta():
    pass

__test__ = _mod_builtins.dict()
def _binary_op_method_timedeltalike():
    pass

_no_input = _mod_builtins.object()
def _op_unary_method():
    pass

def array_to_timedelta64():
    "\n    Convert an ndarray to an array of timedeltas. If errors == 'coerce',\n    coerce non-convertible objects to NaT. Otherwise, raise.\n    "
    pass

def cast_from_unit():
    ' return a casting of the unit represented to nanoseconds\n        round the fractional part of a float to our precision, p '
    pass

def convert_to_timedelta64():
    '\n    Convert an incoming object to a timedelta64 if possible\n\n    Handle these types of objects:\n        - timedelta/Timedelta\n        - timedelta64\n        - an offset\n        - np.int64 (with unit providing a possible modifier)\n        - None/NaT\n\n    Return an ns based int64\n\n    # kludgy here until we have a timedelta scalar\n    # handle the numpy < 1.7 case\n    '
    pass

def delta_to_nanoseconds():
    pass

nat_strings = _mod_builtins.set()
