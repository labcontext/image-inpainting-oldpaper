import builtins as _mod_builtins

class Factorizer(_mod_builtins.object):
    __class__ = Factorizer
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def count(self):
        pass
    
    def factorize(self):
        "\n        Factorize values with nans replaced by na_sentinel\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        "
        pass
    
    def get_count(self):
        pass
    
    @property
    def table(self):
        pass
    
    def unique(self):
        pass
    
    @property
    def uniques(self):
        pass
    

class Float64HashTable(HashTable):
    __class__ = Float64HashTable
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def factorize(self):
        pass
    
    def get_item(self):
        pass
    
    def get_labels(self):
        pass
    
    def get_labels_groupby(self):
        pass
    
    def lookup(self):
        pass
    
    def map(self):
        pass
    
    def map_locations(self):
        pass
    
    def set_item(self):
        pass
    
    def sizeof(self):
        ' return the size of my table in bytes '
        pass
    
    def unique(self):
        pass
    
    def unique_memview(self):
        pass
    

class Float64Vector(_mod_builtins.object):
    __class__ = Float64Vector
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def to_array(self):
        pass
    

class HashTable(_mod_builtins.object):
    __class__ = HashTable
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Int64Factorizer(_mod_builtins.object):
    __class__ = Int64Factorizer
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def count(self):
        pass
    
    def factorize(self):
        "\n        Factorize values with nans replaced by na_sentinel\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        "
        pass
    
    def get_count(self):
        pass
    
    @property
    def table(self):
        pass
    
    @property
    def uniques(self):
        pass
    

class Int64HashTable(HashTable):
    __class__ = Int64HashTable
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def factorize(self):
        pass
    
    def get_item(self):
        pass
    
    def get_labels(self):
        pass
    
    def get_labels_groupby(self):
        pass
    
    def lookup(self):
        pass
    
    def map(self):
        pass
    
    def map_locations(self):
        pass
    
    def set_item(self):
        pass
    
    def sizeof(self):
        ' return the size of my table in bytes '
        pass
    
    def unique(self):
        pass
    
    def unique_memview(self):
        pass
    

class Int64Vector(_mod_builtins.object):
    __class__ = Int64Vector
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def to_array(self):
        pass
    

class ObjectVector(_mod_builtins.object):
    __class__ = ObjectVector
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def to_array(self):
        pass
    

class PyObjectHashTable(HashTable):
    __class__ = PyObjectHashTable
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_item(self):
        pass
    
    def get_labels(self):
        pass
    
    def lookup(self):
        pass
    
    def map_locations(self):
        pass
    
    def set_item(self):
        pass
    
    def sizeof(self):
        ' return the size of my table in bytes '
        pass
    
    def unique(self):
        pass
    

class StringHashTable(HashTable):
    __class__ = StringHashTable
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def factorize(self):
        pass
    
    def get_indexer(self):
        pass
    
    def get_item(self):
        pass
    
    def get_labels(self):
        pass
    
    def lookup(self):
        pass
    
    def map_locations(self):
        pass
    
    na_string_sentinel = '__nan__'
    def set_item(self):
        pass
    
    def sizeof(self):
        ' return the size of my table in bytes '
        pass
    
    def unique(self):
        pass
    

class StringVector(_mod_builtins.object):
    __class__ = StringVector
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def to_array(self):
        pass
    

class UInt64HashTable(HashTable):
    __class__ = UInt64HashTable
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def factorize(self):
        pass
    
    def get_item(self):
        pass
    
    def get_labels(self):
        pass
    
    def get_labels_groupby(self):
        pass
    
    def lookup(self):
        pass
    
    def map(self):
        pass
    
    def map_locations(self):
        pass
    
    def set_item(self):
        pass
    
    def sizeof(self):
        ' return the size of my table in bytes '
        pass
    
    def unique(self):
        pass
    
    def unique_memview(self):
        pass
    

class UInt64Vector(_mod_builtins.object):
    __class__ = UInt64Vector
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def to_array(self):
        pass
    

_SIZE_HINT_LIMIT = 1048583
__builtins__ = {}
__doc__ = None
__file__ = '/home/enliai/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/_libs/hashtable.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.hashtable'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Factorizer():
    pass

def __pyx_unpickle_HashTable():
    pass

def __pyx_unpickle_Int64Factorizer():
    pass

__test__ = _mod_builtins.dict()
def duplicated_float64():
    pass

def duplicated_int64():
    pass

def duplicated_object():
    pass

def duplicated_uint64():
    pass

def ismember_float64():
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : float64 ndarray\n    values : float64 ndarray\n    hasnans : bint, optional\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    pass

def ismember_int64():
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : int64 ndarray\n    values : int64 ndarray\n    hasnans : bint, optional\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    pass

def ismember_object():
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : object ndarray\n    values : object ndarray\n    hasnans : bint, optional\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    pass

def ismember_uint64():
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : uint64 ndarray\n    values : uint64 ndarray\n    hasnans : bint, optional\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    pass

def mode_int64():
    pass

def mode_object():
    pass

def mode_uint64():
    pass

na_sentinel = _mod_builtins.object
nan = float('nan')
def unique_label_indices():
    '\n    indices of the first occurrences of the unique labels\n    *excluding* -1. equivalent to:\n        np.unique(labels, return_index=True)[1]\n    '
    pass

def value_count_float64():
    pass

def value_count_int64():
    pass

def value_count_object():
    pass

def value_count_uint64():
    pass

