import builtins as _mod_builtins
import pybind11_builtins as _mod_pybind11_builtins
import torch as _mod_torch

_EngineBase = _mod_builtins.type
AVG = AggregationType()
class AggregationType(_mod_pybind11_builtins.pybind11_object):
    'Members:\n\n  SUM\n\n  AVG'
    AVG = AggregationType()
    SUM = AggregationType()
    __class__ = AggregationType
    __entries = _mod_builtins.dict()
    def __eq__(self):
        '(self: object, arg0: object) -> bool\n'
        return False
    
    def __getstate__(self):
        '(self: object) -> int_\n'
        return 1
    
    def __hash__(self):
        '(self: object) -> int_\n'
        return 0
    
    def __init__(self: torch._C.AggregationType, arg0: int):
        '__init__(self: torch._C.AggregationType, arg0: int) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self: torch._C.AggregationType):
        '__int__(self: torch._C.AggregationType) -> int\n'
        return 0
    
    __members__ = _mod_builtins.dict()
    __module__ = 'torch._C'
    def __ne__(self):
        '(self: object, arg0: object) -> bool\n'
        return False
    
    def __repr__(self):
        '(self: handle) -> str\n'
        return ''
    
    def __setstate__(self, state):
        '(self: torch._C.AggregationType, arg0: int) -> None\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    name = _mod_builtins.property()

class Argument(_mod_pybind11_builtins.pybind11_object):
    N = _mod_builtins.property()
    __class__ = Argument
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    default_value = _mod_builtins.property()
    name = _mod_builtins.property()
    type = _mod_builtins.property()

class ArgumentSpec(_mod_pybind11_builtins.pybind11_object):
    __class__ = ArgumentSpec
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Block(_mod_pybind11_builtins.pybind11_object):
    __class__ = Block
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def findAllNodes(self: torch._C.Block, kind: str, recurse: bool=True):
        'findAllNodes(self: torch._C.Block, kind: str, recurse: bool = True) -> List[torch::jit::Node]\n\nFind all nodes\n'
        pass
    
    def findNode(self: torch._C.Block, kind: str, recurse: bool=True):
        'findNode(self: torch._C.Block, kind: str, recurse: bool = True) -> torch::jit::Node\n\nFind Node\n'
        pass
    
    def inputs(self: torch._C.Block):
        'inputs(self: torch._C.Block) -> iterator\n'
        pass
    
    def nodes(self: torch._C.Block):
        'nodes(self: torch._C.Block) -> iterator\n'
        pass
    
    def outputs(self: torch._C.Block):
        'outputs(self: torch._C.Block) -> iterator\n'
        pass
    
    def paramNode(self: torch._C.Block):
        'paramNode(self: torch._C.Block) -> torch::jit::Node\n'
        pass
    
    def returnNode(self: torch._C.Block):
        'returnNode(self: torch._C.Block) -> torch::jit::Node\n'
        pass
    

class BoolStorageBase(_mod_builtins.object):
    __class__ = BoolStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class BoolType(Type):
    __class__ = BoolType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def get(cls):
        'get() -> torch._C.BoolType\n'
        pass
    

class ByteStorageBase(_mod_builtins.object):
    __class__ = ByteStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CharStorageBase(_mod_builtins.object):
    __class__ = CharStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class Code(_mod_pybind11_builtins.pybind11_object):
    __class__ = Code
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def grad_executor_states(self: torch._C.Code):
        'grad_executor_states(self: torch._C.Code) -> List[torch::jit::GraphExecutorState]\n'
        pass
    

class CompilationUnit(_mod_pybind11_builtins.pybind11_object):
    __class__ = CompilationUnit
    def __init__(self: torch._C.CompilationUnit):
        '__init__(self: torch._C.CompilationUnit) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def define(self: torch._C.CompilationUnit, arg0: str, arg1: Callable[[str],function]):
        'define(self: torch._C.CompilationUnit, arg0: str, arg1: Callable[[str], function]) -> None\n'
        pass
    
    def find_function(self: torch._C.CompilationUnit, arg0: str):
        'find_function(self: torch._C.CompilationUnit, arg0: str) -> torch::jit::script::Function\n'
        pass
    
    def set_optimized(self: torch._C.CompilationUnit, arg0: bool):
        'set_optimized(self: torch._C.CompilationUnit, arg0: bool) -> None\n'
        pass
    

class CompleteArgumentSpec(_mod_pybind11_builtins.pybind11_object):
    __class__ = CompleteArgumentSpec
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __repr__(self: torch._C.CompleteArgumentSpec):
        '__repr__(self: torch._C.CompleteArgumentSpec) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class CudaBoolStorageBase(_mod_builtins.object):
    __class__ = CudaBoolStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaByteStorageBase(_mod_builtins.object):
    __class__ = CudaByteStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaCharStorageBase(_mod_builtins.object):
    __class__ = CudaCharStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaDoubleStorageBase(_mod_builtins.object):
    __class__ = CudaDoubleStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaFloatStorageBase(_mod_builtins.object):
    __class__ = CudaFloatStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaHalfStorageBase(_mod_builtins.object):
    __class__ = CudaHalfStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaIntStorageBase(_mod_builtins.object):
    __class__ = CudaIntStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaLongStorageBase(_mod_builtins.object):
    __class__ = CudaLongStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class CudaShortStorageBase(_mod_builtins.object):
    __class__ = CudaShortStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_cuda(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    @classmethod
    def _release_ipc_counter(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_cuda_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def get_device(self):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class DictType(Type):
    __class__ = DictType
    def __init__(self: torch._C.DictType, arg0: torch._C.Type, arg1: torch._C.Type):
        '__init__(self: torch._C.DictType, arg0: torch._C.Type, arg1: torch._C.Type) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DoubleStorageBase(_mod_builtins.object):
    __class__ = DoubleStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class ExecutionPlanState(_mod_pybind11_builtins.pybind11_object):
    __class__ = ExecutionPlanState
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    code = _mod_builtins.property()
    graph = _mod_builtins.property()

class ExtraFilesMap(_mod_pybind11_builtins.pybind11_object):
    def __bool__(self: torch._C.ExtraFilesMap):
        '__bool__(self: torch._C.ExtraFilesMap) -> bool\n\nCheck whether the map is nonempty\n'
        return False
    
    __class__ = ExtraFilesMap
    def __delitem__(self: torch._C.ExtraFilesMap, arg0: str):
        '__delitem__(self: torch._C.ExtraFilesMap, arg0: str) -> None\n'
        return None
    
    def __getitem__(self, index):
        '__getitem__(self: torch._C.ExtraFilesMap, arg0: str) -> str\n'
        pass
    
    def __init__(self: torch._C.ExtraFilesMap):
        '__init__(self: torch._C.ExtraFilesMap) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self: torch._C.ExtraFilesMap):
        '__iter__(self: torch._C.ExtraFilesMap) -> iterator\n'
        return ExtraFilesMap()
    
    def __len__(self: torch._C.ExtraFilesMap):
        '__len__(self: torch._C.ExtraFilesMap) -> int\n'
        return 0
    
    __module__ = 'torch._C'
    __pybind11_module_local_v3__ = _mod_builtins.PyCapsule()
    def __repr__(self: torch._C.ExtraFilesMap):
        '__repr__(self: torch._C.ExtraFilesMap) -> str\n\nReturn the canonical string representation of this map.\n'
        return ''
    
    def __setitem__(self, index, value):
        '__setitem__(self: torch._C.ExtraFilesMap, arg0: str, arg1: str) -> None\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def items(self: torch._C.ExtraFilesMap):
        'items(self: torch._C.ExtraFilesMap) -> iterator\n'
        pass
    

FatalError = _mod_torch.FatalError
class FileCheck(_mod_pybind11_builtins.pybind11_object):
    __class__ = FileCheck
    def __init__(self: torch._C.FileCheck):
        '__init__(self: torch._C.FileCheck) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def check(self: torch._C.FileCheck, arg0: str):
        'check(self: torch._C.FileCheck, arg0: str) -> torch._C.FileCheck\n'
        pass
    
    def check_count(self, *args, **kwargs):
        'check_count(*args, **kwargs)\nOverloaded function.\n\n1. check_count(self: torch._C.FileCheck, arg0: str, arg1: int, arg2: bool) -> torch._C.FileCheck\n\n2. check_count(self: torch._C.FileCheck, arg0: str, arg1: int, arg2: bool) -> torch._C.FileCheck\n\n3. check_count(self: torch._C.FileCheck, str: str, count: int, exactly: bool = False) -> torch._C.FileCheck\n\nCheck Count\n'
        pass
    
    def check_dag(self: torch._C.FileCheck, arg0: str):
        'check_dag(self: torch._C.FileCheck, arg0: str) -> torch._C.FileCheck\n'
        pass
    
    def check_next(self: torch._C.FileCheck, arg0: str):
        'check_next(self: torch._C.FileCheck, arg0: str) -> torch._C.FileCheck\n'
        pass
    
    def check_not(self: torch._C.FileCheck, arg0: str):
        'check_not(self: torch._C.FileCheck, arg0: str) -> torch._C.FileCheck\n'
        pass
    
    def check_same(self: torch._C.FileCheck, arg0: str):
        'check_same(self: torch._C.FileCheck, arg0: str) -> torch._C.FileCheck\n'
        pass
    
    def run(self, *args, **kwargs):
        'run(*args, **kwargs)\nOverloaded function.\n\n1. run(self: torch._C.FileCheck, arg0: str) -> None\n\n2. run(self: torch._C.FileCheck, arg0: torch._C.Graph) -> None\n\n3. run(self: torch._C.FileCheck, checks_file: str, test_file: str) -> None\n\nRun\n\n4. run(self: torch._C.FileCheck, checks_file: str, graph: torch._C.Graph) -> None\n\nRun\n'
        pass
    

class FloatStorageBase(_mod_builtins.object):
    __class__ = FloatStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class FloatType(Type):
    __class__ = FloatType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def get(cls):
        'get() -> torch._C.FloatType\n'
        pass
    

class Function(_mod_pybind11_builtins.pybind11_object):
    def __call__(self, *args, **kwargs):
        '__call__(*args, **kwargs) -> object\n'
        pass
    
    __class__ = Function
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    code = _mod_builtins.property()
    def get_debug_state(self: torch._C.Function):
        'get_debug_state(self: torch._C.Function) -> torch._C.GraphExecutorState\n'
        pass
    
    graph = _mod_builtins.property()
    def graph_for(self, *args, **kwargs):
        pass
    
    name = _mod_builtins.property()
    schema = _mod_builtins.property()

class FunctionSchema(_mod_pybind11_builtins.pybind11_object):
    __class__ = FunctionSchema
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __str__(self: torch._C.FunctionSchema):
        '__str__(self: torch._C.FunctionSchema) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    arguments = _mod_builtins.property()
    name = _mod_builtins.property()
    overload_name = _mod_builtins.property()
    returns = _mod_builtins.property()

class Future(_mod_pybind11_builtins.pybind11_object):
    __class__ = Future
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Generator(_mod_builtins.object):
    __class__ = Generator
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    def get_state(self):
        pass
    
    def initial_seed(self):
        pass
    
    def manual_seed(self):
        pass
    
    def seed(self):
        pass
    
    def set_state(self):
        pass
    

class Gradient(_mod_pybind11_builtins.pybind11_object):
    __class__ = Gradient
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    df = _mod_builtins.property()
    df_input_captured_inputs = _mod_builtins.property()
    df_input_captured_outputs = _mod_builtins.property()
    df_input_vjps = _mod_builtins.property()
    df_output_vjps = _mod_builtins.property()
    f = _mod_builtins.property()
    f_real_outputs = _mod_builtins.property()

class Graph(_mod_pybind11_builtins.pybind11_object):
    __class__ = Graph
    def __init__(self: torch._C.Graph):
        '__init__(self: torch._C.Graph) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __repr__(self: torch._C.Graph):
        '__repr__(self: torch._C.Graph) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _export_onnx(self: torch._C.Graph, initializers: Dict[str,at::Tensor], onnx_opset_version: int=0, defer_weight_export: bool=False, operator_export_type: torch._C._onnx.OperatorExportTypes=OperatorExportTypes.ONNX, strip_doc_string: bool=True):
        '_export_onnx(self: torch._C.Graph, initializers: Dict[str, at::Tensor], onnx_opset_version: int = 0, defer_weight_export: bool = False, operator_export_type: torch._C._onnx.OperatorExportTypes = OperatorExportTypes.ONNX, strip_doc_string: bool = True) -> Tuple[bytes, Dict[str, bytes]]\n'
        pass
    
    def _pretty_print_onnx(self: torch._C.Graph, initializers: Dict[str,at::Tensor], onnx_opset_version: int=0, defer_weight_export: bool=False, operator_export_type: torch._C._onnx.OperatorExportTypes=OperatorExportTypes.ONNX, google_printer: bool=False):
        '_pretty_print_onnx(self: torch._C.Graph, initializers: Dict[str, at::Tensor], onnx_opset_version: int = 0, defer_weight_export: bool = False, operator_export_type: torch._C._onnx.OperatorExportTypes = OperatorExportTypes.ONNX, google_printer: bool = False) -> str\n'
        return ''
    
    def addInput(self: torch._C.Graph):
        'addInput(self: torch._C.Graph) -> torch::jit::Value\n'
        pass
    
    def appendNode(self: torch._C.Graph, arg0):
        'appendNode(self: torch._C.Graph, arg0: torch::jit::Node) -> torch::jit::Node\n'
        pass
    
    def copy(self: torch._C.Graph):
        'copy(self: torch._C.Graph) -> torch._C.Graph\n'
        pass
    
    def create(self, *args, **kwargs):
        'create(*args, **kwargs)\nOverloaded function.\n\n1. create(self: torch._C.Graph, arg0: str) -> torch::jit::Node\n\n2. create(self: torch._C.Graph, arg0: str, arg1: int) -> torch::jit::Node\n\n3. create(self: torch._C.Graph, arg0: str, arg1: List[torch::jit::Value]) -> torch::jit::Node\n\n4. create(self: torch._C.Graph, arg0: str, arg1: List[torch::jit::Value], arg2: int) -> torch::jit::Node\n'
        pass
    
    def createClone(self: torch._C.Graph, arg0, arg1: object):
        'createClone(self: torch._C.Graph, arg0: torch::jit::Node, arg1: object) -> torch::jit::Node\n'
        pass
    
    def createFusionGroup(self: torch._C.Graph):
        'createFusionGroup(self: torch._C.Graph) -> torch::jit::Node\n'
        pass
    
    def dump_alias_db(self: torch._C.Graph):
        'dump_alias_db(self: torch._C.Graph) -> None\n'
        pass
    
    def eraseInput(self: torch._C.Graph, arg0: int):
        'eraseInput(self: torch._C.Graph, arg0: int) -> None\n'
        pass
    
    def findAllNodes(self: torch._C.Graph, kind: str, recurse: bool=True):
        'findAllNodes(self: torch._C.Graph, kind: str, recurse: bool = True) -> List[torch::jit::Node]\n\nFind all nodes\n'
        pass
    
    def findNode(self: torch._C.Graph, kind: str, recurse: bool=True):
        'findNode(self: torch._C.Graph, kind: str, recurse: bool = True) -> torch::jit::Node\n\nFind Node\n'
        pass
    
    def inputs(self: torch._C.Graph):
        'inputs(self: torch._C.Graph) -> iterator\n'
        pass
    
    def insertNode(self: torch._C.Graph, arg0):
        'insertNode(self: torch._C.Graph, arg0: torch::jit::Node) -> torch::jit::Node\n'
        pass
    
    def lint(self: torch._C.Graph):
        'lint(self: torch._C.Graph) -> None\n'
        pass
    
    def nodes(self: torch._C.Graph):
        'nodes(self: torch._C.Graph) -> iterator\n'
        pass
    
    def outputs(self: torch._C.Graph):
        'outputs(self: torch._C.Graph) -> iterator\n'
        pass
    
    def param_node(self: torch._C.Graph):
        'param_node(self: torch._C.Graph) -> torch::jit::Node\n'
        pass
    
    def prependNode(self: torch._C.Graph, arg0):
        'prependNode(self: torch._C.Graph, arg0: torch::jit::Node) -> torch::jit::Node\n'
        pass
    
    def registerOutput(self: torch._C.Graph, arg0):
        'registerOutput(self: torch._C.Graph, arg0: torch::jit::Value) -> int\n'
        return 1
    
    def return_node(self: torch._C.Graph):
        'return_node(self: torch._C.Graph) -> torch::jit::Node\n'
        pass
    

class GraphExecutorState(_mod_pybind11_builtins.pybind11_object):
    __class__ = GraphExecutorState
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    execution_plans = _mod_builtins.property()
    fallback = _mod_builtins.property()
    graph = _mod_builtins.property()

class HalfStorageBase(_mod_builtins.object):
    __class__ = HalfStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class IODescriptor(_mod_pybind11_builtins.pybind11_object):
    __class__ = IODescriptor
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class IntStorageBase(_mod_builtins.object):
    __class__ = IntStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class IntType(Type):
    __class__ = IntType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def get(cls):
        'get() -> torch._C.IntType\n'
        pass
    

class JITException(_mod_builtins.Exception):
    __class__ = JITException
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class ListType(Type):
    __class__ = ListType
    def __init__(self: torch._C.ListType, arg0: torch._C.Type):
        '__init__(self: torch._C.ListType, arg0: torch._C.Type) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def getElementType(self: torch._C.ListType):
        'getElementType(self: torch._C.ListType) -> torch._C.Type\n'
        pass
    
    @classmethod
    def ofInts(cls):
        'ofInts() -> torch._C.ListType\n'
        pass
    
    @classmethod
    def ofTensors(cls):
        'ofTensors() -> torch._C.ListType\n'
        pass
    

class LockingLogger(LoggerBase):
    __class__ = LockingLogger
    def __init__(self: torch._C.LockingLogger):
        '__init__(self: torch._C.LockingLogger) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_counter_val(self: torch._C.LockingLogger, arg0: str):
        'get_counter_val(self: torch._C.LockingLogger, arg0: str) -> int\n'
        return 1
    
    def set_aggregation_type(self: torch._C.LockingLogger, arg0: str, arg1: torch._C.AggregationType):
        'set_aggregation_type(self: torch._C.LockingLogger, arg0: str, arg1: torch._C.AggregationType) -> None\n'
        pass
    

class LoggerBase(_mod_pybind11_builtins.pybind11_object):
    __class__ = LoggerBase
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class LongStorageBase(_mod_builtins.object):
    __class__ = LongStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

class Node(_mod_pybind11_builtins.pybind11_object):
    __class__ = Node
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __repr__(self: torch._C.Node):
        '__repr__(self: torch._C.Node) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addBlock(self: torch._C.Node):
        'addBlock(self: torch._C.Node) -> torch._C.Block\n'
        pass
    
    def addInput(self: torch._C.Node, arg0: torch._C.Value):
        'addInput(self: torch._C.Node, arg0: torch._C.Value) -> torch._C.Value\n'
        pass
    
    def addOutput(self: torch._C.Node):
        'addOutput(self: torch._C.Node) -> torch._C.Value\n'
        pass
    
    def attributeNames(self: torch._C.Node):
        'attributeNames(self: torch._C.Node) -> List[str]\n'
        pass
    
    def blocks(self: torch._C.Node):
        'blocks(self: torch._C.Node) -> iterator\n'
        pass
    
    def cconv(self: torch._C.Node):
        'cconv(self: torch._C.Node) -> str\n'
        return ''
    
    def copyAttributes(self: torch._C.Node, arg0: torch._C.Node):
        'copyAttributes(self: torch._C.Node, arg0: torch._C.Node) -> None\n'
        pass
    
    def destroy(self: torch._C.Node):
        'destroy(self: torch._C.Node) -> None\n'
        pass
    
    def eraseOutput(self: torch._C.Node, arg0: int):
        'eraseOutput(self: torch._C.Node, arg0: int) -> None\n'
        pass
    
    def f(self: torch._C.Node, arg0: str):
        'f(self: torch._C.Node, arg0: str) -> float\n'
        return 1.0
    
    def f_(self: torch._C.Node, arg0: str, arg1: float):
        'f_(self: torch._C.Node, arg0: str, arg1: float) -> torch._C.Node\n'
        pass
    
    def findAllNodes(self: torch._C.Node, kind: str, recurse: bool=True):
        'findAllNodes(self: torch._C.Node, kind: str, recurse: bool = True) -> List[torch._C.Node]\n\nFind all nodes\n'
        pass
    
    def findNode(self: torch._C.Node, kind: str, recurse: bool=True):
        'findNode(self: torch._C.Node, kind: str, recurse: bool = True) -> torch._C.Node\n\nFind Node\n'
        pass
    
    def fs(self: torch._C.Node, arg0: str):
        'fs(self: torch._C.Node, arg0: str) -> List[float]\n'
        pass
    
    def fs_(self: torch._C.Node, arg0: str, arg1: List[float]):
        'fs_(self: torch._C.Node, arg0: str, arg1: List[float]) -> torch._C.Node\n'
        pass
    
    def g(self: torch._C.Node, arg0: str):
        'g(self: torch._C.Node, arg0: str) -> torch._C.Graph\n'
        pass
    
    def g_(self: torch._C.Node, arg0: str, arg1: torch._C.Graph):
        'g_(self: torch._C.Node, arg0: str, arg1: torch._C.Graph) -> torch._C.Node\n'
        pass
    
    def getSourceLocation(self: torch._C.Node):
        'getSourceLocation(self: torch._C.Node) -> object\n'
        pass
    
    def gs(self: torch._C.Node, arg0: str):
        'gs(self: torch._C.Node, arg0: str) -> List[torch._C.Graph]\n'
        pass
    
    def gs_(self: torch._C.Node, arg0: str, arg1: List[torch._C.Graph]):
        'gs_(self: torch._C.Node, arg0: str, arg1: List[torch._C.Graph]) -> torch._C.Node\n'
        pass
    
    def hasAttribute(self: torch._C.Node, arg0: str):
        'hasAttribute(self: torch._C.Node, arg0: str) -> bool\n'
        return True
    
    def hasAttributes(self: torch._C.Node):
        'hasAttributes(self: torch._C.Node) -> bool\n'
        return True
    
    def hasMultipleOutputs(self: torch._C.Node):
        'hasMultipleOutputs(self: torch._C.Node) -> bool\n'
        return True
    
    def hasUses(self: torch._C.Node):
        'hasUses(self: torch._C.Node) -> bool\n'
        return True
    
    def i(self: torch._C.Node, arg0: str):
        'i(self: torch._C.Node, arg0: str) -> int\n'
        return 1
    
    def i_(self: torch._C.Node, arg0: str, arg1: int):
        'i_(self: torch._C.Node, arg0: str, arg1: int) -> torch._C.Node\n'
        pass
    
    def input(self: torch._C.Node):
        'input(self: torch._C.Node) -> torch._C.Value\n'
        pass
    
    def inputs(self: torch._C.Node):
        'inputs(self: torch._C.Node) -> iterator\n'
        pass
    
    def inputsAt(self: torch._C.Node, arg0: int):
        'inputsAt(self: torch._C.Node, arg0: int) -> torch._C.Value\n'
        pass
    
    def insertAfter(self: torch._C.Node, arg0: torch._C.Node):
        'insertAfter(self: torch._C.Node, arg0: torch._C.Node) -> torch._C.Node\n'
        pass
    
    def insertBefore(self: torch._C.Node, arg0: torch._C.Node):
        'insertBefore(self: torch._C.Node, arg0: torch._C.Node) -> torch._C.Node\n'
        pass
    
    def isNondeterministic(self: torch._C.Node):
        'isNondeterministic(self: torch._C.Node) -> bool\n'
        return True
    
    def is_(self: torch._C.Node, arg0: str, arg1: List[int]):
        'is_(self: torch._C.Node, arg0: str, arg1: List[int]) -> torch._C.Node\n'
        pass
    
    def kind(self: torch._C.Node):
        'kind(self: torch._C.Node) -> Symbol\n'
        pass
    
    def kindOf(self: torch._C.Node, arg0: str):
        'kindOf(self: torch._C.Node, arg0: str) -> AttributeKind\n'
        pass
    
    def moveAfter(self: torch._C.Node, arg0: torch._C.Node):
        'moveAfter(self: torch._C.Node, arg0: torch._C.Node) -> None\n'
        pass
    
    def moveBefore(self: torch._C.Node, arg0: torch._C.Node):
        'moveBefore(self: torch._C.Node, arg0: torch._C.Node) -> None\n'
        pass
    
    def mustBeNone(self: torch._C.Node):
        'mustBeNone(self: torch._C.Node) -> bool\n'
        return True
    
    def output(self: torch._C.Node):
        'output(self: torch._C.Node) -> torch._C.Value\n'
        pass
    
    def outputs(self: torch._C.Node):
        'outputs(self: torch._C.Node) -> iterator\n'
        pass
    
    def outputsAt(self: torch._C.Node, arg0: int):
        'outputsAt(self: torch._C.Node, arg0: int) -> torch._C.Value\n'
        pass
    
    def outputsSize(self: torch._C.Node):
        'outputsSize(self: torch._C.Node) -> int\n'
        return 1
    
    def pyname(self: torch._C.Node):
        'pyname(self: torch._C.Node) -> str\n'
        return ''
    
    def pyobj(self: torch._C.Node):
        'pyobj(self: torch._C.Node) -> object\n'
        pass
    
    def removeAllInputs(self: torch._C.Node):
        'removeAllInputs(self: torch._C.Node) -> None\n'
        pass
    
    def removeAttribute(self: torch._C.Node, arg0: str):
        'removeAttribute(self: torch._C.Node, arg0: str) -> torch._C.Node\n'
        pass
    
    def removeInput(self: torch._C.Node, arg0: int):
        'removeInput(self: torch._C.Node, arg0: int) -> None\n'
        pass
    
    def replaceAllUsesWith(self: torch._C.Node, arg0: torch._C.Node):
        'replaceAllUsesWith(self: torch._C.Node, arg0: torch._C.Node) -> None\n'
        pass
    
    def replaceInput(self: torch._C.Node, arg0: int, arg1: torch._C.Value):
        'replaceInput(self: torch._C.Node, arg0: int, arg1: torch._C.Value) -> torch._C.Value\n'
        pass
    
    def replaceInputWith(self: torch._C.Node, arg0: torch._C.Value, arg1: torch._C.Value):
        'replaceInputWith(self: torch._C.Node, arg0: torch._C.Value, arg1: torch._C.Value) -> None\n'
        pass
    
    def s(self: torch._C.Node, arg0: str):
        's(self: torch._C.Node, arg0: str) -> str\n'
        return ''
    
    def s_(self: torch._C.Node, arg0: str, arg1: str):
        's_(self: torch._C.Node, arg0: str, arg1: str) -> torch._C.Node\n'
        pass
    
    def scalar_args(self: torch._C.Node):
        'scalar_args(self: torch._C.Node) -> list\n'
        return list()
    
    def scopeName(self: torch._C.Node):
        'scopeName(self: torch._C.Node) -> str\n'
        return ''
    
    def ss(self: torch._C.Node, arg0: str):
        'ss(self: torch._C.Node, arg0: str) -> List[str]\n'
        pass
    
    def ss_(self: torch._C.Node, arg0: str, arg1: List[str]):
        'ss_(self: torch._C.Node, arg0: str, arg1: List[str]) -> torch._C.Node\n'
        pass
    
    def t(self: torch._C.Node, arg0: str):
        't(self: torch._C.Node, arg0: str) -> at::Tensor\n'
        pass
    
    def t_(self: torch._C.Node, arg0: str, arg1):
        't_(self: torch._C.Node, arg0: str, arg1: torch::autograd::Variable) -> torch._C.Node\n'
        pass
    
    def ts(self: torch._C.Node, arg0: str):
        'ts(self: torch._C.Node, arg0: str) -> List[torch::autograd::Variable]\n'
        pass
    
    def ts_(self: torch._C.Node, arg0: str, arg1):
        'ts_(self: torch._C.Node, arg0: str, arg1: List[torch::autograd::Variable]) -> torch._C.Node\n'
        pass
    
    def z(self: torch._C.Node, arg0: str):
        'z(self: torch._C.Node, arg0: str) -> at::Tensor\n'
        pass
    
    def z_(self: torch._C.Node, arg0: str, arg1):
        'z_(self: torch._C.Node, arg0: str, arg1: at::Tensor) -> torch._C.Node\n'
        pass
    
    def zs(self: torch._C.Node, arg0: str):
        'zs(self: torch._C.Node, arg0: str) -> List[at::Tensor]\n'
        pass
    
    def zs_(self: torch._C.Node, arg0: str, arg1: List[at::Tensor]):
        'zs_(self: torch._C.Node, arg0: str, arg1: List[at::Tensor]) -> torch._C.Node\n'
        pass
    

class NoopLogger(LoggerBase):
    __class__ = NoopLogger
    def __init__(self: torch._C.NoopLogger):
        '__init__(self: torch._C.NoopLogger) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class NumberType(Type):
    __class__ = NumberType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def get(cls):
        'get() -> torch._C.NumberType\n'
        pass
    

class OptionalType(Type):
    __class__ = OptionalType
    def __init__(self: torch._C.OptionalType, arg0: torch._C.Type):
        '__init__(self: torch._C.OptionalType, arg0: torch._C.Type) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def getElementType(self: torch._C.OptionalType):
        'getElementType(self: torch._C.OptionalType) -> torch._C.Type\n'
        pass
    
    @classmethod
    def ofTensor(cls):
        'ofTensor() -> torch._C.OptionalType\n'
        pass
    

class PyTorchFileReader(_mod_pybind11_builtins.pybind11_object):
    __class__ = PyTorchFileReader
    def __init__(self: torch._C.PyTorchFileReader, arg0: str):
        '__init__(self: torch._C.PyTorchFileReader, arg0: str) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_record(self: torch._C.PyTorchFileReader, arg0: str):
        'get_record(self: torch._C.PyTorchFileReader, arg0: str) -> bytes\n'
        pass
    

class PyTorchFileWriter(_mod_pybind11_builtins.pybind11_object):
    __class__ = PyTorchFileWriter
    def __init__(self: torch._C.PyTorchFileWriter, arg0: str):
        '__init__(self: torch._C.PyTorchFileWriter, arg0: str) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def write_end_of_file(self: torch._C.PyTorchFileWriter):
        'write_end_of_file(self: torch._C.PyTorchFileWriter) -> None\n'
        pass
    
    def write_record(self: torch._C.PyTorchFileWriter, arg0: str, arg1: str, arg2: int):
        'write_record(self: torch._C.PyTorchFileWriter, arg0: str, arg1: str, arg2: int) -> None\n'
        pass
    

SUM = AggregationType()
class ScriptMethod(_mod_pybind11_builtins.pybind11_object):
    def __call__(self, *args, **kwargs):
        '__call__(*args, **kwargs) -> object\n'
        pass
    
    __class__ = ScriptMethod
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    code = _mod_builtins.property()
    graph = _mod_builtins.property()
    def graph_for(self, *args, **kwargs):
        pass
    
    def initial_ivalues(self: torch._C.ScriptMethod):
        'initial_ivalues(self: torch._C.ScriptMethod) -> List[at::Tensor]\n'
        pass
    
    schema = _mod_builtins.property()

class ScriptModule(_mod_pybind11_builtins.pybind11_object):
    __class__ = ScriptModule
    def __init__(self: torch._C.ScriptModule):
        '__init__(self: torch._C.ScriptModule) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _copy_into(self: torch._C.ScriptModule, arg0: Callable[[List[str]],torch._C.ScriptModule], arg1: Dict[torch._C.Type,torch._C.Type], arg2: List[str]):
        '_copy_into(self: torch._C.ScriptModule, arg0: Callable[[List[str]], torch._C.ScriptModule], arg1: Dict[torch._C.Type, torch._C.Type], arg2: List[str]) -> None\n'
        pass
    
    def _create_method_from_trace(self: torch._C.ScriptModule, arg0: str, arg1: function, arg2: tuple, arg3: function, arg4: bool):
        '_create_method_from_trace(self: torch._C.ScriptModule, arg0: str, arg1: function, arg2: tuple, arg3: function, arg4: bool) -> None\n'
        pass
    
    def _create_methods(self: torch._C.ScriptModule, arg0: object, arg1: List[torch._C._jit_tree_views.Def], arg2: List[Callable[[str],function]], arg3: List[Dict[str,object]]):
        '_create_methods(self: torch._C.ScriptModule, arg0: object, arg1: List[torch._C._jit_tree_views.Def], arg2: List[Callable[[str], function]], arg3: List[Dict[str, object]]) -> None\n'
        pass
    
    def _define(self: torch._C.ScriptModule, arg0: object, arg1: str, arg2: Callable[[str],function]):
        '_define(self: torch._C.ScriptModule, arg0: object, arg1: str, arg2: Callable[[str], function]) -> None\n'
        pass
    
    def _get_attribute(self: torch._C.ScriptModule, arg0: str):
        '_get_attribute(self: torch._C.ScriptModule, arg0: str) -> IValue\n'
        pass
    
    def _get_attributes(self: torch._C.ScriptModule):
        '_get_attributes(self: torch._C.ScriptModule) -> tuple\n'
        pass
    
    def _get_buffer(self: torch._C.ScriptModule, arg0: str):
        '_get_buffer(self: torch._C.ScriptModule, arg0: str) -> torch::autograd::Variable\n'
        pass
    
    def _get_method(self: torch._C.ScriptModule, arg0: str):
        '_get_method(self: torch._C.ScriptModule, arg0: str) -> torch::jit::script::Method\n'
        pass
    
    def _get_module(self: torch._C.ScriptModule, arg0: str):
        '_get_module(self: torch._C.ScriptModule, arg0: str) -> torch._C.ScriptModule\n'
        pass
    
    def _get_modules(self: torch._C.ScriptModule):
        '_get_modules(self: torch._C.ScriptModule) -> tuple\n'
        pass
    
    def _get_parameter(self: torch._C.ScriptModule, arg0: str):
        '_get_parameter(self: torch._C.ScriptModule, arg0: str) -> torch::autograd::Variable\n'
        pass
    
    def _get_parameters(self: torch._C.ScriptModule):
        '_get_parameters(self: torch._C.ScriptModule) -> tuple\n'
        pass
    
    def _has_attribute(self: torch._C.ScriptModule, arg0: str):
        '_has_attribute(self: torch._C.ScriptModule, arg0: str) -> bool\n'
        return True
    
    def _has_buffer(self: torch._C.ScriptModule, arg0: str):
        '_has_buffer(self: torch._C.ScriptModule, arg0: str) -> bool\n'
        return True
    
    def _has_method(self: torch._C.ScriptModule, arg0: str):
        '_has_method(self: torch._C.ScriptModule, arg0: str) -> bool\n'
        return True
    
    def _has_module(self: torch._C.ScriptModule, arg0: str):
        '_has_module(self: torch._C.ScriptModule, arg0: str) -> bool\n'
        return True
    
    def _has_parameter(self: torch._C.ScriptModule, arg0: str):
        '_has_parameter(self: torch._C.ScriptModule, arg0: str) -> bool\n'
        return True
    
    def _method_names(self: torch._C.ScriptModule):
        '_method_names(self: torch._C.ScriptModule) -> List[str]\n'
        pass
    
    def _register_attribute(self: torch._C.ScriptModule, arg0: str, arg1: torch._C.Type, arg2: object):
        '_register_attribute(self: torch._C.ScriptModule, arg0: str, arg1: torch._C.Type, arg2: object) -> None\n'
        pass
    
    def _register_buffer(self: torch._C.ScriptModule, arg0: str, arg1):
        '_register_buffer(self: torch._C.ScriptModule, arg0: str, arg1: torch::autograd::Variable) -> None\n'
        pass
    
    def _register_module(self: torch._C.ScriptModule, arg0: str, arg1: torch._C.ScriptModule):
        '_register_module(self: torch._C.ScriptModule, arg0: str, arg1: torch._C.ScriptModule) -> None\n'
        pass
    
    def _register_parameter(self: torch._C.ScriptModule, arg0: str, arg1, arg2: bool):
        '_register_parameter(self: torch._C.ScriptModule, arg0: str, arg1: torch::autograd::Variable, arg2: bool) -> None\n'
        pass
    
    def _set_optimized(self: torch._C.ScriptModule, arg0: bool):
        '_set_optimized(self: torch._C.ScriptModule, arg0: bool) -> None\n'
        pass
    
    def _set_parameter(self: torch._C.ScriptModule, arg0: str, arg1):
        '_set_parameter(self: torch._C.ScriptModule, arg0: str, arg1: at::Tensor) -> None\n'
        pass
    
    def apply(self: torch._C.ScriptModule, arg0: Callable[[torch._C.ScriptModule],None]):
        'apply(self: torch._C.ScriptModule, arg0: Callable[[torch._C.ScriptModule], None]) -> None\n'
        pass
    
    def clone_method(self: torch._C.ScriptModule, arg0: torch._C.ScriptModule, arg1: str):
        'clone_method(self: torch._C.ScriptModule, arg0: torch._C.ScriptModule, arg1: str) -> None\n'
        pass
    
    code = _mod_builtins.property()
    def get_debug_state(self: torch._C.ScriptModule):
        'get_debug_state(self: torch._C.ScriptModule) -> torch._C.GraphExecutorState\n'
        pass
    
    def save(self: torch._C.ScriptModule, filename: str, _extra_files: torch._C.ExtraFilesMap):
        'save(self: torch._C.ScriptModule, filename: str, _extra_files: torch._C.ExtraFilesMap = ExtraFilesMap{}) -> None\n'
        pass
    
    def save_to_buffer(self: torch._C.ScriptModule, _extra_files: torch._C.ExtraFilesMap):
        'save_to_buffer(self: torch._C.ScriptModule, _extra_files: torch._C.ExtraFilesMap = ExtraFilesMap{}) -> bytes\n'
        pass
    

class ShortStorageBase(_mod_builtins.object):
    __class__ = ShortStorageBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @classmethod
    def _expired(cls):
        pass
    
    @classmethod
    def _free_weak_ref(cls):
        pass
    
    def _get_shared_fd(self):
        pass
    
    @classmethod
    def _new_shared_fd(cls):
        pass
    
    @classmethod
    def _new_shared_filename(cls):
        pass
    
    @classmethod
    def _new_using_fd(cls):
        pass
    
    @classmethod
    def _new_using_filename(cls):
        pass
    
    @classmethod
    def _new_with_file(cls):
        pass
    
    @classmethod
    def _new_with_weak_ptr(cls):
        pass
    
    def _set_cdata(self):
        pass
    
    def _set_from_file(self):
        pass
    
    def _share_fd_(self):
        pass
    
    def _share_filename_(self):
        pass
    
    def _shared_decref(self):
        pass
    
    def _shared_incref(self):
        pass
    
    def _weak_ref(self):
        pass
    
    def _write_file(self):
        pass
    
    def copy_(self):
        pass
    
    def data_ptr(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def element_size(self):
        pass
    
    def fill_(self):
        pass
    
    @classmethod
    def from_buffer(cls):
        pass
    
    @classmethod
    def from_file(cls):
        '\nfrom_file(filename, shared=False, size=0) -> Storage\n\nIf `shared` is `True`, then memory is shared between all processes.\nAll changes are written to the file. If `shared` is `False`, then the changes on\nthe storage do not affect the file.\n\n`size` is the number of elements in the storage. If `shared` is `False`,\nthen the file must contain at least `size * sizeof(Type)` bytes\n(`Type` is the type of storage). If `shared` is `True` the file will be\ncreated if needed.\n\nArgs:\n    filename (str): file name to map\n    shared (bool): whether to share memory\n    size (int): number of elements in the storage\n'
        pass
    
    def is_pinned(self):
        pass
    
    def is_shared(self):
        pass
    
    def new(self):
        pass
    
    def resize_(self):
        pass
    
    def size(self):
        pass
    

Size = _mod_torch.Size
class StringType(Type):
    __class__ = StringType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def get(cls):
        'get() -> torch._C.StringType\n'
        pass
    

class TensorType(Type):
    __class__ = TensorType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def get(cls):
        'get() -> torch._C.TensorType\n'
        pass
    

class TracingState(_mod_pybind11_builtins.pybind11_object):
    __class__ = TracingState
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __repr__(self: torch._C.TracingState):
        '__repr__(self: torch._C.TracingState) -> str\n'
        return ''
    
    def __str__(self: torch._C.TracingState):
        '__str__(self: torch._C.TracingState) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def graph(self: torch._C.TracingState):
        'graph(self: torch._C.TracingState) -> torch._C.Graph\n'
        pass
    
    def pop_scope(self: torch._C.TracingState):
        'pop_scope(self: torch._C.TracingState) -> None\n'
        pass
    
    def push_scope(self: torch._C.TracingState, arg0: str):
        'push_scope(self: torch._C.TracingState, arg0: str) -> None\n'
        pass
    
    def set_graph(self: torch._C.TracingState, arg0: torch._C.Graph):
        'set_graph(self: torch._C.TracingState, arg0: torch._C.Graph) -> None\n'
        pass
    

class TupleType(Type):
    __class__ = TupleType
    def __init__(self: torch._C.TupleType, arg0: List[torch._C.Type]):
        '__init__(self: torch._C.TupleType, arg0: List[torch._C.Type]) -> None\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def elements(self: torch._C.TupleType):
        'elements(self: torch._C.TupleType) -> List[torch._C.Type]\n'
        pass
    

class Type(_mod_pybind11_builtins.pybind11_object):
    __class__ = Type
    def __eq__(self: torch._C.Type, arg0: torch._C.Type):
        '__eq__(self: torch._C.Type, arg0: torch._C.Type) -> bool\n'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __repr__(self: torch._C.Type):
        '__repr__(self: torch._C.Type) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def contiguous(self: torch._C.Type):
        'contiguous(self: torch._C.Type) -> torch._C.Type\n'
        pass
    
    def dim(self: torch._C.Type):
        'dim(self: torch._C.Type) -> int\n'
        return 1
    
    def isSubtypeOf(self: torch._C.Type, arg0: torch._C.Type):
        'isSubtypeOf(self: torch._C.Type, arg0: torch._C.Type) -> bool\n'
        return True
    
    def kind(self: torch._C.Type):
        'kind(self: torch._C.Type) -> str\n'
        return ''
    
    def scalarType(self: torch._C.Type):
        'scalarType(self: torch._C.Type) -> str\n'
        return ''
    
    def sizes(self: torch._C.Type):
        'sizes(self: torch._C.Type) -> List[int]\n'
        pass
    
    def str(self: torch._C.Type):
        'str(self: torch._C.Type) -> str\n'
        return ''
    
    def strides(self: torch._C.Type):
        'strides(self: torch._C.Type) -> List[int]\n'
        pass
    

class Use(_mod_pybind11_builtins.pybind11_object):
    __class__ = Use
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    offset = _mod_builtins.property()
    user = _mod_builtins.property()

class Value(_mod_pybind11_builtins.pybind11_object):
    __class__ = Value
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'torch._C'
    def __repr__(self: torch._C.Value):
        '__repr__(self: torch._C.Value) -> str\n'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def copyMetadata(self: torch._C.Value, arg0: torch._C.Value):
        'copyMetadata(self: torch._C.Value, arg0: torch._C.Value) -> torch._C.Value\n'
        pass
    
    def inferTypeFrom(self: torch._C.Value, arg0):
        'inferTypeFrom(self: torch._C.Value, arg0: at::Tensor) -> None\n'
        pass
    
    def isCompleteTensor(self: torch._C.Value):
        'isCompleteTensor(self: torch._C.Value) -> bool\n'
        return True
    
    def node(self: torch._C.Value):
        'node(self: torch._C.Value) -> torch::jit::Node\n'
        pass
    
    def offset(self: torch._C.Value):
        'offset(self: torch._C.Value) -> int\n'
        return 1
    
    def replaceAllUsesWith(self: torch._C.Value, arg0: torch._C.Value):
        'replaceAllUsesWith(self: torch._C.Value, arg0: torch._C.Value) -> None\n'
        pass
    
    def requires_grad(self: torch._C.Value):
        'requires_grad(self: torch._C.Value) -> bool\n'
        return True
    
    def setType(self: torch._C.Value, arg0):
        'setType(self: torch._C.Value, arg0: c10::Type) -> torch._C.Value\n'
        pass
    
    def setTypeAs(self: torch._C.Value, arg0: torch._C.Value):
        'setTypeAs(self: torch._C.Value, arg0: torch._C.Value) -> torch._C.Value\n'
        pass
    
    def setUniqueName(self: torch._C.Value, arg0: str):
        'setUniqueName(self: torch._C.Value, arg0: str) -> torch._C.Value\n'
        pass
    
    def toIValue(self: torch._C.Value):
        'toIValue(self: torch._C.Value) -> Optional[IValue]\n'
        pass
    
    def type(self, *args, **kwargs):
        'type(*args, **kwargs)\nOverloaded function.\n\n1. type(self: torch._C.Value) -> c10::Type\n\n2. type(self: torch._C.Value) -> c10::Type\n'
        pass
    
    def unique(self: torch._C.Value):
        'unique(self: torch._C.Value) -> int\n'
        return 1
    
    def uniqueName(self: torch._C.Value):
        'uniqueName(self: torch._C.Value) -> str\n'
        return ''
    
    def uses(self: torch._C.Value):
        'uses(self: torch._C.Value) -> List[torch::jit::Use]\n'
        pass
    

class _CudaEventBase(_mod_builtins.object):
    __class__ = _CudaEventBase
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def cuda_event(self):
        pass
    
    @property
    def device(self):
        pass
    
    def elapsed_time(self):
        pass
    
    @classmethod
    def from_ipc_handle(cls):
        pass
    
    def ipc_handle(self):
        pass
    
    def query(self):
        pass
    
    def record(self):
        pass
    
    def synchronize(self):
        pass
    
    def wait(self):
        pass
    

class _CudaStreamBase(_mod_builtins.object):
    __class__ = _CudaStreamBase
    def __eq__(self):
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _cdata(self):
        pass
    
    @property
    def cuda_stream(self):
        pass
    
    @property
    def device(self):
        pass
    
    @property
    def priority(self):
        pass
    
    @classmethod
    def priority_range(cls):
        pass
    
    def query(self):
        pass
    
    def synchronize(self):
        pass
    

class _FunctionBase(_mod_builtins.object):
    __class__ = _FunctionBase
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _do_backward(self):
        pass
    
    def _do_forward(self):
        pass
    
    def _register_hook_dict(self):
        pass
    
    @classmethod
    def apply(cls):
        pass
    
    @property
    def dirty_tensors(self):
        pass
    
    @property
    def metadata(self):
        pass
    
    @property
    def needs_input_grad(self):
        pass
    
    @property
    def next_functions(self):
        pass
    
    @property
    def non_differentiable(self):
        pass
    
    def register_hook(self):
        pass
    
    @property
    def requires_grad(self):
        pass
    
    @property
    def saved_tensors(self):
        pass
    
    @property
    def saved_variables(self):
        pass
    
    @property
    def to_save(self):
        pass
    

_GLIBCXX_USE_CXX11_ABI = False
_ImperativeEngine = _EngineBase()
class _LegacyVariableBase(_mod_builtins.object):
    __class__ = _LegacyVariableBase
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _THCUNN(_mod_builtins.object):
    @classmethod
    def CudaAbsCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaAbsCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaAbs_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaAbs_updateOutput(cls):
        pass
    
    @classmethod
    def CudaBCECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaBCECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaCol2Im_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaCol2Im_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDistKLDivCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDistKLDivCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleAbsCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleAbsCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleAbs_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleAbs_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleBCECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleBCECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleCol2Im_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleCol2Im_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleDistKLDivCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleDistKLDivCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleELU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleELU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleFeatureLPPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleFeatureLPPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleGatedLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleGatedLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleHardTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleHardTanh_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleIm2Col_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleIm2Col_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleIndexLinear_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleIndexLinear_accUpdateGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleIndexLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleIndexLinear_updateParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleL1Cost_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleL1Cost_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleLeakyReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleLeakyReLU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleLogSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleLogSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleLookupTableBag_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleLookupTableBag_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleLookupTable_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleLookupTable_renorm(cls):
        pass
    
    @classmethod
    def CudaDoubleMSECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleMSECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleMultiLabelMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleMultiLabelMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleMultiMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleMultiMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleRReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleRReLU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSmoothL1Criterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSmoothL1Criterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSoftMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSoftMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSoftPlus_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSoftPlus_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSoftShrink_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSoftShrink_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialConvolutionLocal_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialConvolutionLocal_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialConvolutionLocal_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialCrossMapLRN_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialCrossMapLRN_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDepthwiseConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDepthwiseConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDepthwiseConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialFullConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialFullConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialFullConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialSubSampling_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialSubSampling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialSubSampling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialUpSamplingBicubic_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialUpSamplingBicubic_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialUpSamplingBilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialUpSamplingBilinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSpatialUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSqrt_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSqrt_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleSquare_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleSquare_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleTanh_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalRowConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalRowConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalRowConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalUpSamplingLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalUpSamplingLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleTemporalUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricAdaptiveAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricAdaptiveAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricFullConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricFullConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricFullConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricUpSamplingTrilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaDoubleVolumetricUpSamplingTrilinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaELU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaELU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaFeatureLPPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaFeatureLPPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaGatedLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaGatedLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfAbsCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfAbsCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfAbs_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfAbs_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfBCECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfBCECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfCol2Im_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfCol2Im_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfDistKLDivCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfDistKLDivCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfELU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfELU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfFeatureLPPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfFeatureLPPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfGatedLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfGatedLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfHardTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfHardTanh_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfIm2Col_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfIm2Col_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfIndexLinear_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfIndexLinear_accUpdateGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfIndexLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfIndexLinear_updateParameters(cls):
        pass
    
    @classmethod
    def CudaHalfL1Cost_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfL1Cost_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfLeakyReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfLeakyReLU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfLogSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfLogSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfLookupTableBag_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfLookupTableBag_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfLookupTable_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfLookupTable_renorm(cls):
        pass
    
    @classmethod
    def CudaHalfMSECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfMSECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfMultiLabelMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfMultiLabelMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfMultiMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfMultiMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfRReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfRReLU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSmoothL1Criterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSmoothL1Criterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSoftMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSoftMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSoftPlus_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSoftPlus_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSoftShrink_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSoftShrink_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialConvolutionLocal_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialConvolutionLocal_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialConvolutionLocal_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialCrossMapLRN_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialCrossMapLRN_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDepthwiseConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDepthwiseConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDepthwiseConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialFullConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialFullConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialFullConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialSubSampling_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialSubSampling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialSubSampling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialUpSamplingBicubic_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialUpSamplingBicubic_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialUpSamplingBilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialUpSamplingBilinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSpatialUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSqrt_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSqrt_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfSquare_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfSquare_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfTanh_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalRowConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalRowConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalRowConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalUpSamplingLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalUpSamplingLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfTemporalUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricAdaptiveAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricAdaptiveAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricFullConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricFullConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricFullConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricUpSamplingTrilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHalfVolumetricUpSamplingTrilinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaHardTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaHardTanh_updateOutput(cls):
        pass
    
    @classmethod
    def CudaIm2Col_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaIm2Col_updateOutput(cls):
        pass
    
    @classmethod
    def CudaIndexLinear_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaIndexLinear_accUpdateGradParameters(cls):
        pass
    
    @classmethod
    def CudaIndexLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaIndexLinear_updateParameters(cls):
        pass
    
    @classmethod
    def CudaL1Cost_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaL1Cost_updateOutput(cls):
        pass
    
    @classmethod
    def CudaLeakyReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaLeakyReLU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaLogSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaLogSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def CudaLookupTableBag_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaLookupTableBag_updateOutput(cls):
        pass
    
    @classmethod
    def CudaLookupTable_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaLookupTable_renorm(cls):
        pass
    
    @classmethod
    def CudaMSECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaMSECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaMultiLabelMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaMultiLabelMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaMultiMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaMultiMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaRReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaRReLU_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSmoothL1Criterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSmoothL1Criterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSoftMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSoftMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSoftPlus_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSoftPlus_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSoftShrink_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSoftShrink_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialConvolutionLocal_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialConvolutionLocal_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialConvolutionLocal_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialCrossMapLRN_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialCrossMapLRN_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialDepthwiseConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialDepthwiseConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialDepthwiseConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialFullConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialFullConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialFullConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialSubSampling_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaSpatialSubSampling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialSubSampling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialUpSamplingBicubic_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialUpSamplingBicubic_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialUpSamplingBilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialUpSamplingBilinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSpatialUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSpatialUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSqrt_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSqrt_updateOutput(cls):
        pass
    
    @classmethod
    def CudaSquare_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaSquare_updateOutput(cls):
        pass
    
    @classmethod
    def CudaTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaTanh_updateOutput(cls):
        pass
    
    @classmethod
    def CudaTemporalConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaTemporalConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaTemporalConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaTemporalMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaTemporalMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaTemporalRowConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaTemporalRowConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaTemporalRowConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaTemporalUpSamplingLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaTemporalUpSamplingLinear_updateOutput(cls):
        pass
    
    @classmethod
    def CudaTemporalUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaTemporalUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricAdaptiveAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricAdaptiveAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaVolumetricConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaVolumetricDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricFullConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaVolumetricFullConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricFullConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def CudaVolumetricFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def CudaVolumetricUpSamplingTrilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def CudaVolumetricUpSamplingTrilinear_updateOutput(cls):
        pass
    
    __class__ = _THCUNN
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _THNN(_mod_builtins.object):
    @classmethod
    def DoubleAbsCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleAbsCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleBCECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleBCECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleCol2Im_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleCol2Im_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleELU_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleELU_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleFeatureLPPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleFeatureLPPooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleGatedLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleGatedLinear_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleHardTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleHardTanh_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleIm2Col_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleIm2Col_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleIndexLinear_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleIndexLinear_accUpdateGradParameters(cls):
        pass
    
    @classmethod
    def DoubleIndexLinear_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleIndexLinear_updateParameters(cls):
        pass
    
    @classmethod
    def DoubleLeakyReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleLeakyReLU_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleLogSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleLogSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleMSECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleMSECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleMultiLabelMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleMultiLabelMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleMultiMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleMultiMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleRReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleRReLU_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSmoothL1Criterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSmoothL1Criterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSoftMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSoftMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSoftPlus_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSoftPlus_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSoftShrink_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSoftShrink_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleSpatialConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleSpatialDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleSpatialFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialUpSamplingBicubic_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialUpSamplingBicubic_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialUpSamplingBilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialUpSamplingBilinear_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleSpatialUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleSpatialUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleTanh_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleTemporalRowConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleTemporalRowConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleTemporalRowConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleTemporalUpSamplingLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleTemporalUpSamplingLinear_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleTemporalUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleTemporalUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricAdaptiveAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricAdaptiveAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleVolumetricConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleVolumetricDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def DoubleVolumetricFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricUpSamplingTrilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def DoubleVolumetricUpSamplingTrilinear_updateOutput(cls):
        pass
    
    @classmethod
    def Doubleunfolded_acc(cls):
        pass
    
    @classmethod
    def Doubleunfolded_copy(cls):
        pass
    
    @classmethod
    def FloatAbsCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatAbsCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatBCECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatBCECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatCol2Im_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatCol2Im_updateOutput(cls):
        pass
    
    @classmethod
    def FloatELU_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatELU_updateOutput(cls):
        pass
    
    @classmethod
    def FloatFeatureLPPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatFeatureLPPooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatGatedLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatGatedLinear_updateOutput(cls):
        pass
    
    @classmethod
    def FloatHardTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatHardTanh_updateOutput(cls):
        pass
    
    @classmethod
    def FloatIm2Col_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatIm2Col_updateOutput(cls):
        pass
    
    @classmethod
    def FloatIndexLinear_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatIndexLinear_accUpdateGradParameters(cls):
        pass
    
    @classmethod
    def FloatIndexLinear_updateOutput(cls):
        pass
    
    @classmethod
    def FloatIndexLinear_updateParameters(cls):
        pass
    
    @classmethod
    def FloatLeakyReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatLeakyReLU_updateOutput(cls):
        pass
    
    @classmethod
    def FloatLogSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatLogSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def FloatMSECriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatMSECriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatMultiLabelMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatMultiLabelMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatMultiMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatMultiMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatRReLU_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatRReLU_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSigmoid_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSigmoid_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSmoothL1Criterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSmoothL1Criterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSoftMarginCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSoftMarginCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSoftPlus_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSoftPlus_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSoftShrink_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSoftShrink_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialClassNLLCriterion_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialClassNLLCriterion_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatSpatialConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatSpatialDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatSpatialFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialUpSamplingBicubic_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialUpSamplingBicubic_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialUpSamplingBilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialUpSamplingBilinear_updateOutput(cls):
        pass
    
    @classmethod
    def FloatSpatialUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatSpatialUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def FloatTanh_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatTanh_updateOutput(cls):
        pass
    
    @classmethod
    def FloatTemporalRowConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatTemporalRowConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatTemporalRowConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def FloatTemporalUpSamplingLinear_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatTemporalUpSamplingLinear_updateOutput(cls):
        pass
    
    @classmethod
    def FloatTemporalUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatTemporalUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricAdaptiveAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricAdaptiveAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricAveragePooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricAveragePooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricConvolutionMM_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatVolumetricConvolutionMM_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricConvolutionMM_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatVolumetricDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricDilatedMaxPooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricDilatedMaxPooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricFullDilatedConvolution_accGradParameters(cls):
        pass
    
    @classmethod
    def FloatVolumetricFullDilatedConvolution_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricFullDilatedConvolution_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricMaxUnpooling_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricMaxUnpooling_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricUpSamplingNearest_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricUpSamplingNearest_updateOutput(cls):
        pass
    
    @classmethod
    def FloatVolumetricUpSamplingTrilinear_updateGradInput(cls):
        pass
    
    @classmethod
    def FloatVolumetricUpSamplingTrilinear_updateOutput(cls):
        pass
    
    @classmethod
    def Floatunfolded_acc(cls):
        pass
    
    @classmethod
    def Floatunfolded_copy(cls):
        pass
    
    __class__ = _THNN
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _TensorBase(_mod_builtins.object):
    def __add__(self):
        return _TensorBase()
    
    def __and__(self):
        return _TensorBase()
    
    def __bool__(self):
        return False
    
    __class__ = _TensorBase
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __div__(self):
        pass
    
    def __float__(self):
        return 0.0
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __iadd__(self):
        return None
    
    def __iand__(self):
        return None
    
    def __idiv__(self):
        pass
    
    def __ilshift__(self):
        pass
    
    def __imul__(self):
        return None
    
    def __index__(self):
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        return 0
    
    def __invert__(self):
        return _TensorBase()
    
    def __ior__(self):
        return None
    
    def __irshift__(self):
        pass
    
    def __isub__(self):
        return None
    
    def __ixor__(self):
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __long__(self):
        pass
    
    def __lshift__(self):
        return _TensorBase()
    
    def __matmul__(self):
        pass
    
    def __mod__(self):
        return _TensorBase()
    
    def __mul__(self):
        return _TensorBase()
    
    def __nonzero__(self):
        pass
    
    def __or__(self):
        return _TensorBase()
    
    def __radd__(self):
        return _TensorBase()
    
    def __rmul__(self):
        return _TensorBase()
    
    def __rshift__(self):
        return _TensorBase()
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __sub__(self):
        return _TensorBase()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self):
        return 0.0
    
    def __xor__(self):
        return _TensorBase()
    
    @property
    def _backward_hooks(self):
        pass
    
    @property
    def _base(self):
        pass
    
    @property
    def _cdata(self):
        pass
    
    def _coalesced_(self):
        pass
    
    def _dimI(self):
        pass
    
    def _dimV(self):
        pass
    
    @property
    def _grad(self):
        pass
    
    @property
    def _grad_fn(self):
        pass
    
    def _indices(self):
        pass
    
    def _is_view(self):
        pass
    
    @classmethod
    def _make_subclass(cls):
        pass
    
    def _nnz(self):
        pass
    
    def _values(self):
        pass
    
    @property
    def _version(self):
        pass
    
    def abs(self):
        '\nabs() -> Tensor\n\nSee :func:`torch.abs`\n'
        pass
    
    def abs_(self):
        '\nabs_() -> Tensor\n\nIn-place version of :meth:`~Tensor.abs`\n'
        pass
    
    def acos(self):
        '\nacos() -> Tensor\n\nSee :func:`torch.acos`\n'
        pass
    
    def acos_(self):
        '\nacos_() -> Tensor\n\nIn-place version of :meth:`~Tensor.acos`\n'
        pass
    
    def add(self):
        '\nadd(value) -> Tensor\nadd(value=1, other) -> Tensor\n\nSee :func:`torch.add`\n'
        pass
    
    def add_(self):
        '\nadd_(value) -> Tensor\nadd_(value=1, other) -> Tensor\n\nIn-place version of :meth:`~Tensor.add`\n'
        pass
    
    def addbmm(self):
        '\naddbmm(beta=1, alpha=1, batch1, batch2) -> Tensor\n\nSee :func:`torch.addbmm`\n'
        pass
    
    def addbmm_(self):
        '\naddbmm_(beta=1, alpha=1, batch1, batch2) -> Tensor\n\nIn-place version of :meth:`~Tensor.addbmm`\n'
        pass
    
    def addcdiv(self):
        '\naddcdiv(value=1, tensor1, tensor2) -> Tensor\n\nSee :func:`torch.addcdiv`\n'
        pass
    
    def addcdiv_(self):
        '\naddcdiv_(value=1, tensor1, tensor2) -> Tensor\n\nIn-place version of :meth:`~Tensor.addcdiv`\n'
        pass
    
    def addcmul(self):
        '\naddcmul(value=1, tensor1, tensor2) -> Tensor\n\nSee :func:`torch.addcmul`\n'
        pass
    
    def addcmul_(self):
        '\naddcmul_(value=1, tensor1, tensor2) -> Tensor\n\nIn-place version of :meth:`~Tensor.addcmul`\n'
        pass
    
    def addmm(self):
        '\naddmm(beta=1, alpha=1, mat1, mat2) -> Tensor\n\nSee :func:`torch.addmm`\n'
        pass
    
    def addmm_(self):
        '\naddmm_(beta=1, alpha=1, mat1, mat2) -> Tensor\n\nIn-place version of :meth:`~Tensor.addmm`\n'
        pass
    
    def addmv(self):
        '\naddmv(beta=1, alpha=1, mat, vec) -> Tensor\n\nSee :func:`torch.addmv`\n'
        pass
    
    def addmv_(self):
        '\naddmv_(beta=1, alpha=1, mat, vec) -> Tensor\n\nIn-place version of :meth:`~Tensor.addmv`\n'
        pass
    
    def addr(self):
        '\naddr(beta=1, alpha=1, vec1, vec2) -> Tensor\n\nSee :func:`torch.addr`\n'
        pass
    
    def addr_(self):
        '\naddr_(beta=1, alpha=1, vec1, vec2) -> Tensor\n\nIn-place version of :meth:`~Tensor.addr`\n'
        pass
    
    def all(self):
        '\n.. function:: all() -> bool\n\nReturns True if all elements in the tensor are non-zero, False otherwise.\n\nExample::\n\n    >>> a = torch.randn(1, 3).byte() % 2\n    >>> a\n    tensor([[1, 0, 0]], dtype=torch.uint8)\n    >>> a.all()\n    tensor(0, dtype=torch.uint8)\n\n.. function:: all(dim, keepdim=False, out=None) -> Tensor\n\nReturns True if all elements in each row of the tensor in the given\ndimension :attr:`dim` are non-zero, False otherwise.\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size as\n:attr:`input` except in the dimension :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting\nin the output tensor having 1 fewer dimension than :attr:`input`.\n\nArgs:\n    dim (int): the dimension to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 2).byte() % 2\n    >>> a\n    tensor([[0, 0],\n            [0, 0],\n            [0, 1],\n            [1, 1]], dtype=torch.uint8)\n    >>> a.all(dim=1)\n    tensor([0, 0, 0, 1], dtype=torch.uint8)\n\n'
        pass
    
    def allclose(self):
        '\nallclose(other, rtol=1e-05, atol=1e-08, equal_nan=False) -> Tensor\n\nSee :func:`torch.allclose`\n'
        pass
    
    def any(self):
        '\n.. function:: any() -> bool\n\nReturns True if any elements in the tensor are non-zero, False otherwise.\n\nExample::\n\n    >>> a = torch.randn(1, 3).byte() % 2\n    >>> a\n    tensor([[0, 0, 1]], dtype=torch.uint8)\n    >>> a.any()\n    tensor(1, dtype=torch.uint8)\n\n.. function:: any(dim, keepdim=False, out=None) -> Tensor\n\nReturns True if any elements in each row of the tensor in the given\ndimension :attr:`dim` are non-zero, False otherwise.\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size as\n:attr:`input` except in the dimension :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting\nin the output tensor having 1 fewer dimension than :attr:`input`.\n\nArgs:\n    dim (int): the dimension to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 2).byte() % 2\n    >>> a\n    tensor([[1, 0],\n            [0, 0],\n            [0, 1],\n            [0, 0]], dtype=torch.uint8)\n    >>> a.any(dim=1)\n    tensor([1, 0, 1, 0], dtype=torch.uint8)\n\n'
        pass
    
    def apply_(self):
        '\napply_(callable) -> Tensor\n\nApplies the function :attr:`callable` to each element in the tensor, replacing\neach element with the value returned by :attr:`callable`.\n\n.. note::\n\n    This function only works with CPU tensors and should not be used in code\n    sections that require high performance.\n'
        pass
    
    def argmax(self):
        '\nargmax(dim=None, keepdim=False) -> LongTensor\n\nSee :func:`torch.argmax`\n'
        pass
    
    def argmin(self):
        '\nargmin(dim=None, keepdim=False) -> LongTensor\n\nSee :func:`torch.argmin`\n'
        pass
    
    def argsort(self):
        '\nargsort(dim=-1, descending=False) -> LongTensor\n\nSee :func: `torch.argsort`\n'
        pass
    
    def as_strided(self):
        pass
    
    def as_strided_(self):
        pass
    
    def asin(self):
        '\nasin() -> Tensor\n\nSee :func:`torch.asin`\n'
        pass
    
    def asin_(self):
        '\nasin_() -> Tensor\n\nIn-place version of :meth:`~Tensor.asin`\n'
        pass
    
    def atan(self):
        '\natan() -> Tensor\n\nSee :func:`torch.atan`\n'
        pass
    
    def atan2(self):
        '\natan2(other) -> Tensor\n\nSee :func:`torch.atan2`\n'
        pass
    
    def atan2_(self):
        '\natan2_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.atan2`\n'
        pass
    
    def atan_(self):
        '\natan_() -> Tensor\n\nIn-place version of :meth:`~Tensor.atan`\n'
        pass
    
    def baddbmm(self):
        '\nbaddbmm(beta=1, alpha=1, batch1, batch2) -> Tensor\n\nSee :func:`torch.baddbmm`\n'
        pass
    
    def baddbmm_(self):
        '\nbaddbmm_(beta=1, alpha=1, batch1, batch2) -> Tensor\n\nIn-place version of :meth:`~Tensor.baddbmm`\n'
        pass
    
    def bernoulli(self):
        '\nbernoulli(*, generator=None) -> Tensor\n\nReturns a result tensor where each :math:`\\texttt{result[i]}` is independently\nsampled from :math:`\\text{Bernoulli}(\\texttt{self[i]})`. :attr:`self` must have\nfloating point ``dtype``, and the result will have the same ``dtype``.\n\nSee :func:`torch.bernoulli`\n'
        pass
    
    def bernoulli_(self):
        '\n.. function:: bernoulli_(p=0.5, *, generator=None) -> Tensor\n\n    Fills each location of :attr:`self` with an independent sample from\n    :math:`\\text{Bernoulli}(\\texttt{p})`. :attr:`self` can have integral\n    ``dtype``.\n\n.. function:: bernoulli_(p_tensor, *, generator=None) -> Tensor\n\n    :attr:`p_tensor` should be a tensor containing probabilities to be used for\n    drawing the binary random number.\n\n    The :math:`\\text{i}^{th}` element of :attr:`self` tensor will be set to a\n    value sampled from :math:`\\text{Bernoulli}(\\texttt{p\\_tensor[i]})`.\n\n    :attr:`self` can have integral ``dtype``, but :attr:`p_tensor` must have\n    floating point ``dtype``.\n\nSee also :meth:`~Tensor.bernoulli` and :func:`torch.bernoulli`\n'
        pass
    
    def bincount(self):
        '\nbincount(weights=None, minlength=0) -> Tensor\n\nSee :func:`torch.bincount`\n'
        pass
    
    def bmm(self):
        '\nbmm(batch2) -> Tensor\n\nSee :func:`torch.bmm`\n'
        pass
    
    def byte(self):
        '\nbyte() -> Tensor\n\n``self.byte()`` is equivalent to ``self.to(torch.uint8)``. See :func:`to`.\n'
        pass
    
    def cauchy_(self):
        '\ncauchy_(median=0, sigma=1, *, generator=None) -> Tensor\n\nFills the tensor with numbers drawn from the Cauchy distribution:\n\n.. math::\n\n    f(x) = \\dfrac{1}{\\pi} \\dfrac{\\sigma}{(x - \\text{median})^2 + \\sigma^2}\n'
        pass
    
    def ceil(self):
        '\nceil() -> Tensor\n\nSee :func:`torch.ceil`\n'
        pass
    
    def ceil_(self):
        '\nceil_() -> Tensor\n\nIn-place version of :meth:`~Tensor.ceil`\n'
        pass
    
    def char(self):
        '\nchar() -> Tensor\n\n``self.char()`` is equivalent to ``self.to(torch.int8)``. See :func:`to`.\n'
        pass
    
    def cholesky(self):
        '\ncholesky(upper=False) -> Tensor\n\nSee :func:`torch.cholesky`\n'
        pass
    
    def cholesky_inverse(self):
        '\ncholesky_inverse(upper=False) -> Tensor\n\nSee :func:`torch.cholesky_inverse`\n'
        pass
    
    def cholesky_solve(self):
        '\ncholesky_solve(input2, upper=False) -> Tensor\n\nSee :func:`torch.cholesky_solve`\n'
        pass
    
    def chunk(self):
        '\nchunk(chunks, dim=0) -> List of Tensors\n\nSee :func:`torch.chunk`\n'
        pass
    
    def clamp(self):
        '\nclamp(min, max) -> Tensor\n\nSee :func:`torch.clamp`\n'
        pass
    
    def clamp_(self):
        '\nclamp_(min, max) -> Tensor\n\nIn-place version of :meth:`~Tensor.clamp`\n'
        pass
    
    def clamp_max(self):
        pass
    
    def clamp_max_(self):
        pass
    
    def clamp_min(self):
        pass
    
    def clamp_min_(self):
        pass
    
    def clone(self):
        '\nclone() -> Tensor\n\nReturns a copy of the :attr:`self` tensor. The copy has the same size and data\ntype as :attr:`self`.\n\n.. note::\n\n    Unlike `copy_()`, this function is recorded in the computation graph. Gradients\n    propagating to the cloned tensor will propagate to the original tensor.\n'
        pass
    
    def coalesce(self):
        pass
    
    def contiguous(self):
        '\ncontiguous() -> Tensor\n\nReturns a contiguous tensor containing the same data as :attr:`self` tensor. If\n:attr:`self` tensor is contiguous, this function returns the :attr:`self`\ntensor.\n'
        pass
    
    def copy_(self):
        '\ncopy_(src, non_blocking=False) -> Tensor\n\nCopies the elements from :attr:`src` into :attr:`self` tensor and returns\n:attr:`self`.\n\nThe :attr:`src` tensor must be :ref:`broadcastable <broadcasting-semantics>`\nwith the :attr:`self` tensor. It may be of a different data type or reside on a\ndifferent device.\n\nArgs:\n    src (Tensor): the source tensor to copy from\n    non_blocking (bool): if ``True`` and this copy is between CPU and GPU,\n        the copy may occur asynchronously with respect to the host. For other\n        cases, this argument has no effect.\n'
        pass
    
    def cos(self):
        '\ncos() -> Tensor\n\nSee :func:`torch.cos`\n'
        pass
    
    def cos_(self):
        '\ncos_() -> Tensor\n\nIn-place version of :meth:`~Tensor.cos`\n'
        pass
    
    def cosh(self):
        '\ncosh() -> Tensor\n\nSee :func:`torch.cosh`\n'
        pass
    
    def cosh_(self):
        '\ncosh_() -> Tensor\n\nIn-place version of :meth:`~Tensor.cosh`\n'
        pass
    
    def cpu(self):
        '\ncpu() -> Tensor\n\nReturns a copy of this object in CPU memory.\n\nIf this object is already in CPU memory and on the correct device,\nthen no copy is performed and the original object is returned.\n'
        pass
    
    def cross(self):
        '\ncross(other, dim=-1) -> Tensor\n\nSee :func:`torch.cross`\n'
        pass
    
    def cuda(self):
        '\ncuda(device=None, non_blocking=False) -> Tensor\n\nReturns a copy of this object in CUDA memory.\n\nIf this object is already in CUDA memory and on the correct device,\nthen no copy is performed and the original object is returned.\n\nArgs:\n    device (:class:`torch.device`): The destination GPU device.\n        Defaults to the current CUDA device.\n    non_blocking (bool): If ``True`` and the source is in pinned memory,\n        the copy will be asynchronous with respect to the host.\n        Otherwise, the argument has no effect. Default: ``False``.\n'
        pass
    
    def cumprod(self):
        '\ncumprod(dim, dtype=None) -> Tensor\n\nSee :func:`torch.cumprod`\n'
        pass
    
    def cumsum(self):
        '\ncumsum(dim, dtype=None) -> Tensor\n\nSee :func:`torch.cumsum`\n'
        pass
    
    @property
    def data(self):
        pass
    
    def data_ptr(self):
        '\ndata_ptr() -> int\n\nReturns the address of the first element of :attr:`self` tensor.\n'
        pass
    
    def dense_dim(self):
        '\ndense_dim() -> int\n\nIf :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),\nthis returns a the number of dense dimensions. Otherwise, this throws an\nerror.\n\nSee also :meth:`Tensor.sparse_dim`.\n'
        pass
    
    def dequantize(self):
        '\ndequantize() -> Tensor\n\nGiven a quantized Tensor, dequantize it and return the dequantized float Tensor.\n'
        pass
    
    def det(self):
        '\ndet() -> Tensor\n\nSee :func:`torch.det`\n'
        pass
    
    def detach(self):
        '\n    Returns a new Tensor, detached from the current graph.\n\n    The result will never require gradient.\n\n    .. note::\n\n      Returned Tensor shares the same storage with the original one.\n      In-place modifications on either of them will be seen, and may trigger\n      errors in correctness checks.\n      IMPORTANT NOTE: Previously, in-place size / stride / storage changes\n      (such as `resize_` / `resize_as_` / `set_` / `transpose_`) to the returned tensor\n      also update the original tensor. Now, these in-place changes will not update the\n      original tensor anymore, and will instead trigger an error.\n      For sparse tensors:\n      In-place indices / values changes (such as `zero_` / `copy_` / `add_`) to the\n      returned tensor will not update the original tensor anymore, and will instead\n      trigger an error.\n    '
        pass
    
    def detach_(self):
        '\n    Detaches the Tensor from the graph that created it, making it a leaf.\n    Views cannot be detached in-place.\n    '
        pass
    
    @property
    def device(self):
        '\nIs the :class:`torch.device` where this Tensor is.\n'
        pass
    
    def diag(self):
        '\ndiag(diagonal=0) -> Tensor\n\nSee :func:`torch.diag`\n'
        pass
    
    def diag_embed(self):
        '\ndiag_embed(offset=0, dim1=-2, dim2=-1) -> Tensor\n\nSee :func:`torch.diag_embed`\n'
        pass
    
    def diagflat(self):
        '\ndiagflat(diagonal=0) -> Tensor\n\nSee :func:`torch.diagflat`\n'
        pass
    
    def diagonal(self):
        '\ndiagonal(offset=0, dim1=0, dim2=1) -> Tensor\n\nSee :func:`torch.diagonal`\n'
        pass
    
    def digamma(self):
        '\ndigamma() -> Tensor\n\nSee :func:`torch.digamma`\n'
        pass
    
    def digamma_(self):
        '\ndigamma_() -> Tensor\n\nIn-place version of :meth:`~Tensor.digamma`\n'
        pass
    
    def dim(self):
        '\ndim() -> int\n\nReturns the number of dimensions of :attr:`self` tensor.\n'
        pass
    
    def dist(self):
        '\ndist(other, p=2) -> Tensor\n\nSee :func:`torch.dist`\n'
        pass
    
    def div(self):
        '\ndiv(value) -> Tensor\n\nSee :func:`torch.div`\n'
        pass
    
    def div_(self):
        '\ndiv_(value) -> Tensor\n\nIn-place version of :meth:`~Tensor.div`\n'
        pass
    
    def dot(self):
        '\ndot(tensor2) -> Tensor\n\nSee :func:`torch.dot`\n'
        pass
    
    def double(self):
        '\ndouble() -> Tensor\n\n``self.double()`` is equivalent to ``self.to(torch.float64)``. See :func:`to`.\n'
        pass
    
    @property
    def dtype(self):
        pass
    
    def eig(self):
        '\neig(eigenvectors=False) -> (Tensor, Tensor)\n\nSee :func:`torch.eig`\n'
        pass
    
    def element_size(self):
        '\nelement_size() -> int\n\nReturns the size in bytes of an individual element.\n\nExample::\n\n    >>> torch.tensor([]).element_size()\n    4\n    >>> torch.tensor([], dtype=torch.uint8).element_size()\n    1\n\n'
        pass
    
    def eq(self):
        '\neq(other) -> Tensor\n\nSee :func:`torch.eq`\n'
        pass
    
    def eq_(self):
        '\neq_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.eq`\n'
        pass
    
    def equal(self):
        '\nequal(other) -> bool\n\nSee :func:`torch.equal`\n'
        pass
    
    def erf(self):
        '\nerf() -> Tensor\n\nSee :func:`torch.erf`\n'
        pass
    
    def erf_(self):
        '\nerf_() -> Tensor\n\nIn-place version of :meth:`~Tensor.erf`\n'
        pass
    
    def erfc(self):
        '\nerfc() -> Tensor\n\nSee :func:`torch.erfc`\n'
        pass
    
    def erfc_(self):
        '\nerfc_() -> Tensor\n\nIn-place version of :meth:`~Tensor.erfc`\n'
        pass
    
    def erfinv(self):
        '\nerfinv() -> Tensor\n\nSee :func:`torch.erfinv`\n'
        pass
    
    def erfinv_(self):
        '\nerfinv_() -> Tensor\n\nIn-place version of :meth:`~Tensor.erfinv`\n'
        pass
    
    def exp(self):
        '\nexp() -> Tensor\n\nSee :func:`torch.exp`\n'
        pass
    
    def exp_(self):
        '\nexp_() -> Tensor\n\nIn-place version of :meth:`~Tensor.exp`\n'
        pass
    
    def expand(self):
        '\nexpand(*sizes) -> Tensor\n\nReturns a new view of the :attr:`self` tensor with singleton dimensions expanded\nto a larger size.\n\nPassing -1 as the size for a dimension means not changing the size of\nthat dimension.\n\nTensor can be also expanded to a larger number of dimensions, and the\nnew ones will be appended at the front. For the new dimensions, the\nsize cannot be set to -1.\n\nExpanding a tensor does not allocate new memory, but only creates a\nnew view on the existing tensor where a dimension of size one is\nexpanded to a larger size by setting the ``stride`` to 0. Any dimension\nof size 1 can be expanded to an arbitrary value without allocating new\nmemory.\n\nArgs:\n    *sizes (torch.Size or int...): the desired expanded size\n\n.. warning::\n\n    More than one element of an expanded tensor may refer to a single\n    memory location. As a result, in-place operations (especially ones that\n    are vectorized) may result in incorrect behavior. If you need to write\n    to the tensors, please clone them first.\n\nExample::\n\n    >>> x = torch.tensor([[1], [2], [3]])\n    >>> x.size()\n    torch.Size([3, 1])\n    >>> x.expand(3, 4)\n    tensor([[ 1,  1,  1,  1],\n            [ 2,  2,  2,  2],\n            [ 3,  3,  3,  3]])\n    >>> x.expand(-1, 4)   # -1 means not changing the size of that dimension\n    tensor([[ 1,  1,  1,  1],\n            [ 2,  2,  2,  2],\n            [ 3,  3,  3,  3]])\n'
        pass
    
    def expand_as(self):
        '\nexpand_as(other) -> Tensor\n\nExpand this tensor to the same size as :attr:`other`.\n``self.expand_as(other)`` is equivalent to ``self.expand(other.size())``.\n\nPlease see :meth:`~Tensor.expand` for more information about ``expand``.\n\nArgs:\n    other (:class:`torch.Tensor`): The result tensor has the same size\n        as :attr:`other`.\n'
        pass
    
    def expm1(self):
        '\nexpm1() -> Tensor\n\nSee :func:`torch.expm1`\n'
        pass
    
    def expm1_(self):
        '\nexpm1_() -> Tensor\n\nIn-place version of :meth:`~Tensor.expm1`\n'
        pass
    
    def exponential_(self):
        '\nexponential_(lambd=1, *, generator=None) -> Tensor\n\nFills :attr:`self` tensor with elements drawn from the exponential distribution:\n\n.. math::\n\n    f(x) = \\lambda e^{-\\lambda x}\n'
        pass
    
    def fft(self):
        '\nfft(signal_ndim, normalized=False) -> Tensor\n\nSee :func:`torch.fft`\n'
        pass
    
    def fill_(self):
        '\nfill_(value) -> Tensor\n\nFills :attr:`self` tensor with the specified value.\n'
        pass
    
    def flatten(self):
        '\nflatten(input, start_dim=0, end_dim=-1) -> Tensor\n\nsee :func:`torch.flatten`\n'
        pass
    
    def flip(self):
        '\nflip(dims) -> Tensor\n\nSee :func:`torch.flip`\n'
        pass
    
    def float(self):
        '\nfloat() -> Tensor\n\n``self.float()`` is equivalent to ``self.to(torch.float32)``. See :func:`to`.\n'
        pass
    
    def floor(self):
        '\nfloor() -> Tensor\n\nSee :func:`torch.floor`\n'
        pass
    
    def floor_(self):
        '\nfloor_() -> Tensor\n\nIn-place version of :meth:`~Tensor.floor`\n'
        pass
    
    def fmod(self):
        '\nfmod(divisor) -> Tensor\n\nSee :func:`torch.fmod`\n'
        pass
    
    def fmod_(self):
        '\nfmod_(divisor) -> Tensor\n\nIn-place version of :meth:`~Tensor.fmod`\n'
        pass
    
    def frac(self):
        '\nfrac() -> Tensor\n\nSee :func:`torch.frac`\n'
        pass
    
    def frac_(self):
        '\nfrac_() -> Tensor\n\nIn-place version of :meth:`~Tensor.frac`\n'
        pass
    
    def gather(self):
        '\ngather(dim, index) -> Tensor\n\nSee :func:`torch.gather`\n'
        pass
    
    def ge(self):
        '\nge(other) -> Tensor\n\nSee :func:`torch.ge`\n'
        pass
    
    def ge_(self):
        '\nge_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.ge`\n'
        pass
    
    def gels(self):
        '\ngels(A) -> Tensor\n\nSee :func:`torch.gels`\n'
        pass
    
    def geometric_(self):
        '\ngeometric_(p, *, generator=None) -> Tensor\n\nFills :attr:`self` tensor with elements drawn from the geometric distribution:\n\n.. math::\n\n    f(X=k) = (1 - p)^{k - 1} p\n\n'
        pass
    
    def geqrf(self):
        '\ngeqrf() -> (Tensor, Tensor)\n\nSee :func:`torch.geqrf`\n'
        pass
    
    def ger(self):
        '\nger(vec2) -> Tensor\n\nSee :func:`torch.ger`\n'
        pass
    
    def get_device(self):
        "\nget_device() -> Device ordinal (Integer)\n\nFor CUDA tensors, this function returns the device ordinal of the GPU on which the tensor resides.\nFor CPU tensors, an error is thrown.\n\nExample::\n\n    >>> x = torch.randn(3, 4, 5, device='cuda:0')\n    >>> x.get_device()\n    0\n    >>> x.cpu().get_device()  # RuntimeError: get_device is not implemented for type torch.FloatTensor\n"
        pass
    
    @property
    def grad(self):
        '\nThis attribute is ``None`` by default and becomes a Tensor the first time a call to\n:func:`backward` computes gradients for ``self``.\nThe attribute will then contain the gradients computed and future calls to\n:func:`backward` will accumulate (add) gradients into it.\n'
        pass
    
    @property
    def grad_fn(self):
        pass
    
    def gt(self):
        '\ngt(other) -> Tensor\n\nSee :func:`torch.gt`\n'
        pass
    
    def gt_(self):
        '\ngt_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.gt`\n'
        pass
    
    def half(self):
        '\nhalf() -> Tensor\n\n``self.half()`` is equivalent to ``self.to(torch.float16)``. See :func:`to`.\n'
        pass
    
    def hardshrink(self):
        '\nhardshrink(lambd=0.5) -> Tensor\n\nSee :func:`torch.nn.functional.hardshrink`\n'
        pass
    
    def histc(self):
        '\nhistc(bins=100, min=0, max=0) -> Tensor\n\nSee :func:`torch.histc`\n'
        pass
    
    def ifft(self):
        '\nifft(signal_ndim, normalized=False) -> Tensor\n\nSee :func:`torch.ifft`\n'
        pass
    
    def index_add(self):
        '\nindex_add(dim, index, tensor) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.index_add_`\n'
        pass
    
    def index_add_(self):
        '\nindex_add_(dim, index, tensor) -> Tensor\n\nAccumulate the elements of :attr:`tensor` into the :attr:`self` tensor by adding\nto the indices in the order given in :attr:`index`. For example, if ``dim == 0``\nand ``index[i] == j``, then the ``i``\\ th row of :attr:`tensor` is added to the\n``j``\\ th row of :attr:`self`.\n\nThe :attr:`dim`\\ th dimension of :attr:`tensor` must have the same size as the\nlength of :attr:`index` (which must be a vector), and all other dimensions must\nmatch :attr:`self`, or an error will be raised.\n\n.. include:: cuda_deterministic.rst\n\nArgs:\n    dim (int): dimension along which to index\n    index (LongTensor): indices of :attr:`tensor` to select from\n    tensor (Tensor): the tensor containing values to add\n\nExample::\n\n    >>> x = torch.ones(5, 3)\n    >>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)\n    >>> index = torch.tensor([0, 4, 2])\n    >>> x.index_add_(0, index, t)\n    tensor([[  2.,   3.,   4.],\n            [  1.,   1.,   1.],\n            [  8.,   9.,  10.],\n            [  1.,   1.,   1.],\n            [  5.,   6.,   7.]])\n'
        pass
    
    def index_copy(self):
        '\nindex_copy(dim, index, tensor) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.index_copy_`\n'
        pass
    
    def index_copy_(self):
        '\nindex_copy_(dim, index, tensor) -> Tensor\n\nCopies the elements of :attr:`tensor` into the :attr:`self` tensor by selecting\nthe indices in the order given in :attr:`index`. For example, if ``dim == 0``\nand ``index[i] == j``, then the ``i``\\ th row of :attr:`tensor` is copied to the\n``j``\\ th row of :attr:`self`.\n\nThe :attr:`dim`\\ th dimension of :attr:`tensor` must have the same size as the\nlength of :attr:`index` (which must be a vector), and all other dimensions must\nmatch :attr:`self`, or an error will be raised.\n\nArgs:\n    dim (int): dimension along which to index\n    index (LongTensor): indices of :attr:`tensor` to select from\n    tensor (Tensor): the tensor containing values to copy\n\nExample::\n\n    >>> x = torch.zeros(5, 3)\n    >>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)\n    >>> index = torch.tensor([0, 4, 2])\n    >>> x.index_copy_(0, index, t)\n    tensor([[ 1.,  2.,  3.],\n            [ 0.,  0.,  0.],\n            [ 7.,  8.,  9.],\n            [ 0.,  0.,  0.],\n            [ 4.,  5.,  6.]])\n'
        pass
    
    def index_fill(self):
        '\nindex_fill(dim, index, value) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.index_fill_`\n'
        pass
    
    def index_fill_(self):
        '\nindex_fill_(dim, index, val) -> Tensor\n\nFills the elements of the :attr:`self` tensor with value :attr:`val` by\nselecting the indices in the order given in :attr:`index`.\n\nArgs:\n    dim (int): dimension along which to index\n    index (LongTensor): indices of :attr:`self` tensor to fill in\n    val (float): the value to fill with\n\nExample::\n    >>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)\n    >>> index = torch.tensor([0, 2])\n    >>> x.index_fill_(1, index, -1)\n    tensor([[-1.,  2., -1.],\n            [-1.,  5., -1.],\n            [-1.,  8., -1.]])\n'
        pass
    
    def index_put(self):
        '\nindex_put(indices, value, accumulate=False) -> Tensor\n\nOut-place version of :meth:`~Tensor.index_put_`\n'
        pass
    
    def index_put_(self):
        '\nindex_put_(indices, value, accumulate=False) -> Tensor\n\nPuts values from the tensor :attr:`value` into the tensor :attr:`self` using\nthe indices specified in :attr:`indices` (which is a tuple of Tensors). The\nexpression ``tensor.index_put_(indices, value)`` is equivalent to\n``tensor[indices] = value``. Returns :attr:`self`.\n\nIf :attr:`accumulate` is ``True``, the elements in :attr:`tensor` are added to\n:attr:`self`. If accumulate is ``False``, the behavior is undefined if indices\ncontain duplicate elements.\n\nArgs:\n    indices (tuple of LongTensor): tensors used to index into `self`.\n    value (Tensor): tensor of same dtype as `self`.\n    accumulate (bool): whether to accumulate into self\n'
        pass
    
    def index_select(self):
        '\nindex_select(dim, index) -> Tensor\n\nSee :func:`torch.index_select`\n'
        pass
    
    def indices(self):
        '\nindices() -> Tensor\n\nIf :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),\nthis returns a view of the contained indices tensor. Otherwise, this throws an\nerror.\n\nSee also :meth:`Tensor.values`.\n\n.. note::\n  This method can only be called on a coalesced sparse tensor. See\n  :meth:`Tensor.coalesce` for details.\n'
        pass
    
    def int(self):
        '\nint() -> Tensor\n\n``self.int()`` is equivalent to ``self.to(torch.int32)``. See :func:`to`.\n'
        pass
    
    def int_repr(self):
        '\nint_repr() -> Tensor\n\nGiven a quantized Tensor,\n``self.int_repr()`` returns a CPU Tensor with uint8_t as data type that stores the\nunderlying uint8_t values of the given Tensor.\n'
        pass
    
    def inverse(self):
        '\ninverse() -> Tensor\n\nSee :func:`torch.inverse`\n'
        pass
    
    def irfft(self):
        '\nirfft(signal_ndim, normalized=False, onesided=True, signal_sizes=None) -> Tensor\n\nSee :func:`torch.irfft`\n'
        pass
    
    def is_coalesced(self):
        pass
    
    def is_complex(self):
        pass
    
    def is_contiguous(self):
        '\nis_contiguous() -> bool\n\nReturns True if :attr:`self` tensor is contiguous in memory in C order.\n'
        pass
    
    @property
    def is_cuda(self):
        '\nIs ``True`` if the Tensor is stored on the GPU, ``False`` otherwise.\n'
        pass
    
    def is_distributed(self):
        pass
    
    def is_floating_point(self):
        '\nis_floating_point() -> bool\n\nReturns True if the data type of :attr:`self` is a floating point data type.\n'
        pass
    
    @property
    def is_leaf(self):
        '\nAll Tensors that have :attr:`requires_grad` which is ``False`` will be leaf Tensors by convention.\n\nFor Tensors that have :attr:`requires_grad` which is ``True``, they will be leaf Tensors if they were\ncreated by the user. This means that they are not the result of an operation and so\n:attr:`grad_fn` is None.\n\nOnly leaf Tensors will have their :attr:`grad` populated during a call to :func:`backward`.\nTo get :attr:`grad` populated for non-leaf Tensors, you can use :func:`retain_grad`.\n\nExample::\n\n    >>> a = torch.rand(10, requires_grad=True)\n    >>> a.is_leaf\n    True\n    >>> b = torch.rand(10, requires_grad=True).cuda()\n    >>> b.is_leaf\n    False\n    # b was created by the operation that cast a cpu Tensor into a cuda Tensor\n    >>> c = torch.rand(10, requires_grad=True) + 2\n    >>> c.is_leaf\n    False\n    # c was created by the addition operation\n    >>> d = torch.rand(10).cuda()\n    >>> d.is_leaf\n    True\n    # d does not require gradients and so has no operation creating it (that is tracked by the autograd engine)\n    >>> e = torch.rand(10).cuda().requires_grad_()\n    >>> e.is_leaf\n    True\n    # e requires gradients and has no operations creating it\n    >>> f = torch.rand(10, requires_grad=True, device="cuda")\n    >>> f.is_leaf\n    True\n    # f requires grad, has no operation creating it\n\n\n'
        pass
    
    def is_nonzero(self):
        pass
    
    @property
    def is_quantized(self):
        pass
    
    def is_same_size(self):
        pass
    
    def is_set_to(self):
        '\nis_set_to(tensor) -> bool\n\nReturns True if this object refers to the same ``THTensor`` object from the\nTorch C API as the given tensor.\n'
        pass
    
    def is_signed(self):
        '\nis_signed() -> bool\n\nReturns True if the data type of :attr:`self` is a signed data type.\n'
        pass
    
    @property
    def is_sparse(self):
        pass
    
    def isclose(self):
        pass
    
    def item(self):
        '\nitem() -> number\n\nReturns the value of this tensor as a standard Python number. This only works\nfor tensors with one element. For other cases, see :meth:`~Tensor.tolist`.\n\nThis operation is not differentiable.\n\nExample::\n\n    >>> x = torch.tensor([1.0])\n    >>> x.item()\n    1.0\n\n'
        pass
    
    def kthvalue(self):
        '\nkthvalue(k, dim=None, keepdim=False) -> (Tensor, LongTensor)\n\nSee :func:`torch.kthvalue`\n'
        pass
    
    @property
    def layout(self):
        pass
    
    def le(self):
        '\nle(other) -> Tensor\n\nSee :func:`torch.le`\n'
        pass
    
    def le_(self):
        '\nle_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.le`\n'
        pass
    
    def lerp(self):
        '\nlerp(end, weight) -> Tensor\n\nSee :func:`torch.lerp`\n'
        pass
    
    def lerp_(self):
        '\nlerp_(end, weight) -> Tensor\n\nIn-place version of :meth:`~Tensor.lerp`\n'
        pass
    
    def lgamma(self):
        pass
    
    def lgamma_(self):
        pass
    
    def log(self):
        '\nlog() -> Tensor\n\nSee :func:`torch.log`\n'
        pass
    
    def log10(self):
        '\nlog10() -> Tensor\n\nSee :func:`torch.log10`\n'
        pass
    
    def log10_(self):
        '\nlog10_() -> Tensor\n\nIn-place version of :meth:`~Tensor.log10`\n'
        pass
    
    def log1p(self):
        '\nlog1p() -> Tensor\n\nSee :func:`torch.log1p`\n'
        pass
    
    def log1p_(self):
        '\nlog1p_() -> Tensor\n\nIn-place version of :meth:`~Tensor.log1p`\n'
        pass
    
    def log2(self):
        '\nlog2() -> Tensor\n\nSee :func:`torch.log2`\n'
        pass
    
    def log2_(self):
        '\nlog2_() -> Tensor\n\nIn-place version of :meth:`~Tensor.log2`\n'
        pass
    
    def log_(self):
        '\nlog_() -> Tensor\n\nIn-place version of :meth:`~Tensor.log`\n'
        pass
    
    def log_normal_(self):
        '\nlog_normal_(mean=1, std=2, *, generator=None)\n\nFills :attr:`self` tensor with numbers samples from the log-normal distribution\nparameterized by the given mean :math:`\\mu` and standard deviation\n:math:`\\sigma`. Note that :attr:`mean` and :attr:`std` are the mean and\nstandard deviation of the underlying normal distribution, and not of the\nreturned distribution:\n\n.. math::\n\n    f(x) = \\dfrac{1}{x \\sigma \\sqrt{2\\pi}}\\ e^{-\\frac{(\\ln x - \\mu)^2}{2\\sigma^2}}\n'
        pass
    
    def log_softmax(self):
        pass
    
    def logdet(self):
        '\nlogdet() -> Tensor\n\nSee :func:`torch.logdet`\n'
        pass
    
    def logsumexp(self):
        '\nlogsumexp(dim, keepdim=False) -> Tensor\n\nSee :func:`torch.logsumexp`\n'
        pass
    
    def long(self):
        '\nlong() -> Tensor\n\n``self.long()`` is equivalent to ``self.to(torch.int64)``. See :func:`to`.\n'
        pass
    
    def lt(self):
        '\nlt(other) -> Tensor\n\nSee :func:`torch.lt`\n'
        pass
    
    def lt_(self):
        '\nlt_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.lt`\n'
        pass
    
    def lu_solve(self):
        '\nlu_solve(LU_data, LU_pivots) -> Tensor\n\nSee :func:`torch.lu_solve`\n'
        pass
    
    def map2_(self):
        pass
    
    def map_(self):
        '\nmap_(tensor, callable)\n\nApplies :attr:`callable` for each element in :attr:`self` tensor and the given\n:attr:`tensor` and stores the results in :attr:`self` tensor. :attr:`self` tensor and\nthe given :attr:`tensor` must be :ref:`broadcastable <broadcasting-semantics>`.\n\nThe :attr:`callable` should have the signature::\n\n    def callable(a, b) -> number\n'
        pass
    
    def masked_fill(self):
        '\nmasked_fill(mask, value) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.masked_fill_`\n'
        pass
    
    def masked_fill_(self):
        '\nmasked_fill_(mask, value)\n\nFills elements of :attr:`self` tensor with :attr:`value` where :attr:`mask` is\none. The shape of :attr:`mask` must be\n:ref:`broadcastable <broadcasting-semantics>` with the shape of the underlying\ntensor.\n\nArgs:\n    mask (ByteTensor): the binary mask\n    value (float): the value to fill in with\n'
        pass
    
    def masked_scatter(self):
        '\nmasked_scatter(mask, tensor) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.masked_scatter_`\n'
        pass
    
    def masked_scatter_(self):
        '\nmasked_scatter_(mask, source)\n\nCopies elements from :attr:`source` into :attr:`self` tensor at positions where\nthe :attr:`mask` is one.\nThe shape of :attr:`mask` must be :ref:`broadcastable <broadcasting-semantics>`\nwith the shape of the underlying tensor. The :attr:`source` should have at least\nas many elements as the number of ones in :attr:`mask`\n\nArgs:\n    mask (ByteTensor): the binary mask\n    source (Tensor): the tensor to copy from\n\n.. note::\n\n    The :attr:`mask` operates on the :attr:`self` tensor, not on the given\n    :attr:`source` tensor.\n'
        pass
    
    def masked_select(self):
        '\nmasked_select(mask) -> Tensor\n\nSee :func:`torch.masked_select`\n'
        pass
    
    def matmul(self):
        '\nmatmul(tensor2) -> Tensor\n\nSee :func:`torch.matmul`\n'
        pass
    
    def matrix_power(self):
        '\nmatrix_power(n) -> Tensor\n\nSee :func:`torch.matrix_power`\n'
        pass
    
    def max(self):
        '\nmax(dim=None, keepdim=False) -> Tensor or (Tensor, Tensor)\n\nSee :func:`torch.max`\n'
        pass
    
    def mean(self):
        '\nmean(dim=None, keepdim=False) -> Tensor or (Tensor, Tensor)\n\nSee :func:`torch.mean`\n'
        pass
    
    def median(self):
        '\nmedian(dim=None, keepdim=False) -> (Tensor, LongTensor)\n\nSee :func:`torch.median`\n'
        pass
    
    def min(self):
        '\nmin(dim=None, keepdim=False) -> Tensor or (Tensor, Tensor)\n\nSee :func:`torch.min`\n'
        pass
    
    def mm(self):
        '\nmm(mat2) -> Tensor\n\nSee :func:`torch.mm`\n'
        pass
    
    def mode(self):
        '\nmode(dim=None, keepdim=False) -> (Tensor, LongTensor)\n\nSee :func:`torch.mode`\n'
        pass
    
    def mul(self):
        '\nmul(value) -> Tensor\n\nSee :func:`torch.mul`\n'
        pass
    
    def mul_(self):
        '\nmul_(value)\n\nIn-place version of :meth:`~Tensor.mul`\n'
        pass
    
    def multinomial(self):
        '\nmultinomial(num_samples, replacement=False, *, generator=None) -> Tensor\n\nSee :func:`torch.multinomial`\n'
        pass
    
    def mv(self):
        '\nmv(vec) -> Tensor\n\nSee :func:`torch.mv`\n'
        pass
    
    def mvlgamma(self):
        '\nmvlgamma(p) -> Tensor\n\nSee :func:`torch.mvlgamma`\n'
        pass
    
    def mvlgamma_(self):
        '\nmvlgamma_(p) -> Tensor\n\nIn-place version of :meth:`~Tensor.mvlgamma`\n'
        pass
    
    @property
    def name(self):
        pass
    
    def narrow(self):
        '\nnarrow(dimension, start, length) -> Tensor\n\nSee :func:`torch.narrow`\n\nExample::\n\n    >>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n    >>> x.narrow(0, 0, 2)\n    tensor([[ 1,  2,  3],\n            [ 4,  5,  6]])\n    >>> x.narrow(1, 1, 2)\n    tensor([[ 2,  3],\n            [ 5,  6],\n            [ 8,  9]])\n'
        pass
    
    def narrow_copy(self):
        '\nnarrow_copy(dimension, start, length) -> Tensor\n\nSame as :meth:`Tensor.narrow` except returning a copy rather\nthan shared storage.  This is primarily for sparse tensors, which\ndo not have a shared-storage narrow method.  Calling ```narrow_copy``\nwith ```dimemsion > self.sparse_dim()``` will return a copy with the\nrelevant dense dimension narrowed, and ```self.shape``` updated accordingly.\n'
        pass
    
    def ndimension(self):
        '\nndimension() -> int\n\nAlias for :meth:`~Tensor.dim()`\n'
        pass
    
    def ne(self):
        '\nne(other) -> Tensor\n\nSee :func:`torch.ne`\n'
        pass
    
    def ne_(self):
        '\nne_(other) -> Tensor\n\nIn-place version of :meth:`~Tensor.ne`\n'
        pass
    
    def neg(self):
        '\nneg() -> Tensor\n\nSee :func:`torch.neg`\n'
        pass
    
    def neg_(self):
        '\nneg_() -> Tensor\n\nIn-place version of :meth:`~Tensor.neg`\n'
        pass
    
    def nelement(self):
        '\nnelement() -> int\n\nAlias for :meth:`~Tensor.numel`\n'
        pass
    
    def new(self):
        pass
    
    def new_empty(self):
        '\nnew_empty(size, dtype=None, device=None, requires_grad=False) -> Tensor\n\nReturns a Tensor of size :attr:`size` filled with uninitialized data.\nBy default, the returned Tensor has the same :class:`torch.dtype` and\n:class:`torch.device` as this tensor.\n\nArgs:\n    dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.\n        Default: if None, same :class:`torch.dtype` as this tensor.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if None, same :class:`torch.device` as this tensor.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> tensor = torch.ones(())\n    >>> tensor.new_empty((2, 3))\n    tensor([[ 5.8182e-18,  4.5765e-41, -1.0545e+30],\n            [ 3.0949e-41,  4.4842e-44,  0.0000e+00]])\n\n'
        pass
    
    def new_full(self):
        '\nnew_full(size, fill_value, dtype=None, device=None, requires_grad=False) -> Tensor\n\nReturns a Tensor of size :attr:`size` filled with :attr:`fill_value`.\nBy default, the returned Tensor has the same :class:`torch.dtype` and\n:class:`torch.device` as this tensor.\n\nArgs:\n    fill_value (scalar): the number to fill the output tensor with.\n    dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.\n        Default: if None, same :class:`torch.dtype` as this tensor.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if None, same :class:`torch.device` as this tensor.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> tensor = torch.ones((2,), dtype=torch.float64)\n    >>> tensor.new_full((3, 4), 3.141592)\n    tensor([[ 3.1416,  3.1416,  3.1416,  3.1416],\n            [ 3.1416,  3.1416,  3.1416,  3.1416],\n            [ 3.1416,  3.1416,  3.1416,  3.1416]], dtype=torch.float64)\n\n'
        pass
    
    def new_ones(self):
        '\nnew_ones(size, dtype=None, device=None, requires_grad=False) -> Tensor\n\nReturns a Tensor of size :attr:`size` filled with ``1``.\nBy default, the returned Tensor has the same :class:`torch.dtype` and\n:class:`torch.device` as this tensor.\n\nArgs:\n    size (int...): a list, tuple, or :class:`torch.Size` of integers defining the\n        shape of the output tensor.\n    dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.\n        Default: if None, same :class:`torch.dtype` as this tensor.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if None, same :class:`torch.device` as this tensor.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> tensor = torch.tensor((), dtype=torch.int32)\n    >>> tensor.new_ones((2, 3))\n    tensor([[ 1,  1,  1],\n            [ 1,  1,  1]], dtype=torch.int32)\n\n'
        pass
    
    def new_tensor(self):
        "\nnew_tensor(data, dtype=None, device=None, requires_grad=False) -> Tensor\n\nReturns a new Tensor with :attr:`data` as the tensor data.\nBy default, the returned Tensor has the same :class:`torch.dtype` and\n:class:`torch.device` as this tensor.\n\n.. warning::\n\n    :func:`new_tensor` always copies :attr:`data`. If you have a Tensor\n    ``data`` and want to avoid a copy, use :func:`torch.Tensor.requires_grad_`\n    or :func:`torch.Tensor.detach`.\n    If you have a numpy array and want to avoid a copy, use\n    :func:`torch.from_numpy`.\n\n.. warning::\n\n    When data is a tensor `x`, :func:`new_tensor()` reads out 'the data' from whatever it is passed,\n    and constructs a leaf variable. Therefore ``tensor.new_tensor(x)`` is equivalent to ``x.clone().detach()``\n    and ``tensor.new_tensor(x, requires_grad=True)`` is equivalent to ``x.clone().detach().requires_grad_(True)``.\n    The equivalents using ``clone()`` and ``detach()`` are recommended.\n\nArgs:\n    data (array_like): The returned Tensor copies :attr:`data`.\n    dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.\n        Default: if None, same :class:`torch.dtype` as this tensor.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if None, same :class:`torch.device` as this tensor.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> tensor = torch.ones((2,), dtype=torch.int8)\n    >>> data = [[0, 1], [2, 3]]\n    >>> tensor.new_tensor(data)\n    tensor([[ 0,  1],\n            [ 2,  3]], dtype=torch.int8)\n\n"
        pass
    
    def new_zeros(self):
        '\nnew_zeros(size, dtype=None, device=None, requires_grad=False) -> Tensor\n\nReturns a Tensor of size :attr:`size` filled with ``0``.\nBy default, the returned Tensor has the same :class:`torch.dtype` and\n:class:`torch.device` as this tensor.\n\nArgs:\n    size (int...): a list, tuple, or :class:`torch.Size` of integers defining the\n        shape of the output tensor.\n    dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.\n        Default: if None, same :class:`torch.dtype` as this tensor.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if None, same :class:`torch.device` as this tensor.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> tensor = torch.tensor((), dtype=torch.float64)\n    >>> tensor.new_zeros((2, 3))\n    tensor([[ 0.,  0.,  0.],\n            [ 0.,  0.,  0.]], dtype=torch.float64)\n\n'
        pass
    
    def nonzero(self):
        '\nnonzero() -> LongTensor\n\nSee :func:`torch.nonzero`\n'
        pass
    
    def norm(self):
        '\nnorm(p=2, dim=None, keepdim=False) -> Tensor\n\nSee :func:`torch.norm`\n'
        pass
    
    def normal_(self):
        '\nnormal_(mean=0, std=1, *, generator=None) -> Tensor\n\nFills :attr:`self` tensor with elements samples from the normal distribution\nparameterized by :attr:`mean` and :attr:`std`.\n'
        pass
    
    def numel(self):
        '\nnumel() -> int\n\nSee :func:`torch.numel`\n'
        pass
    
    def numpy(self):
        '\nnumpy() -> numpy.ndarray\n\nReturns :attr:`self` tensor as a NumPy :class:`ndarray`. This tensor and the\nreturned :class:`ndarray` share the same underlying storage. Changes to\n:attr:`self` tensor will be reflected in the :class:`ndarray` and vice versa.\n'
        pass
    
    def orgqr(self):
        '\norgqr(input2) -> Tensor\n\nSee :func:`torch.orgqr`\n'
        pass
    
    def ormqr(self):
        '\normqr(input2, input3, left=True, transpose=False) -> Tensor\n\nSee :func:`torch.ormqr`\n'
        pass
    
    @property
    def output_nr(self):
        pass
    
    def permute(self):
        '\npermute(*dims) -> Tensor\n\nPermute the dimensions of this tensor.\n\nArgs:\n    *dims (int...): The desired ordering of dimensions\n\nExample:\n    >>> x = torch.randn(2, 3, 5)\n    >>> x.size()\n    torch.Size([2, 3, 5])\n    >>> x.permute(2, 0, 1).size()\n    torch.Size([5, 2, 3])\n'
        pass
    
    def pin_memory(self):
        "\npin_memory() -> Tensor\n\nCopies the tensor to pinned memory, if it's not already pinned.\n"
        pass
    
    def pinverse(self):
        '\npinverse() -> Tensor\n\nSee :func:`torch.pinverse`\n'
        pass
    
    def polygamma(self):
        pass
    
    def polygamma_(self):
        pass
    
    def pow(self):
        '\npow(exponent) -> Tensor\n\nSee :func:`torch.pow`\n'
        pass
    
    def pow_(self):
        '\npow_(exponent) -> Tensor\n\nIn-place version of :meth:`~Tensor.pow`\n'
        pass
    
    def prelu(self):
        pass
    
    def prod(self):
        '\nprod(dim=None, keepdim=False, dtype=None) -> Tensor\n\nSee :func:`torch.prod`\n'
        pass
    
    def pstrf(self):
        pass
    
    def put_(self):
        '\nput_(indices, tensor, accumulate=False) -> Tensor\n\nCopies the elements from :attr:`tensor` into the positions specified by\nindices. For the purpose of indexing, the :attr:`self` tensor is treated as if\nit were a 1-D tensor.\n\nIf :attr:`accumulate` is ``True``, the elements in :attr:`tensor` are added to\n:attr:`self`. If accumulate is ``False``, the behavior is undefined if indices\ncontain duplicate elements.\n\nArgs:\n    indices (LongTensor): the indices into self\n    tensor (Tensor): the tensor containing values to copy from\n    accumulate (bool): whether to accumulate into self\n\nExample::\n\n    >>> src = torch.tensor([[4, 3, 5],\n                            [6, 7, 8]])\n    >>> src.put_(torch.tensor([1, 3]), torch.tensor([9, 10]))\n    tensor([[  4,   9,   5],\n            [ 10,   7,   8]])\n'
        pass
    
    def q_scale(self):
        '\nq_scale() -> float\n\nGiven a Tensor quantized by linear(affine) quantization,\nreturns the scale of the underlying quantizer().\n'
        pass
    
    def q_zero_point(self):
        '\nq_zero_point() -> int\n\nGiven a Tensor quantized by linear(affine) quantization,\nreturns the zero_point of the underlying quantizer().\n'
        pass
    
    def qr(self):
        '\nqr() -> (Tensor, Tensor)\n\nSee :func:`torch.qr`\n'
        pass
    
    def quantize_linear(self):
        '\nquantize_linear(scale, zero_point) -> Tensor\n\nQuantize a float Tensor using affine quantization scheme with given scale and\nzero_point.\nreturns the quantized Tensor.\n'
        pass
    
    def random_(self):
        "\nrandom_(from=0, to=None, *, generator=None) -> Tensor\n\nFills :attr:`self` tensor with numbers sampled from the discrete uniform\ndistribution over ``[from, to - 1]``. If not specified, the values are usually\nonly bounded by :attr:`self` tensor's data type. However, for floating point\ntypes, if unspecified, range will be ``[0, 2^mantissa]`` to ensure that every\nvalue is representable. For example, `torch.tensor(1, dtype=torch.double).random_()`\nwill be uniform in ``[0, 2^53]``.\n"
        pass
    
    def reciprocal(self):
        '\nreciprocal() -> Tensor\n\nSee :func:`torch.reciprocal`\n'
        pass
    
    def reciprocal_(self):
        '\nreciprocal_() -> Tensor\n\nIn-place version of :meth:`~Tensor.reciprocal`\n'
        pass
    
    def record_stream(self):
        pass
    
    def relu(self):
        pass
    
    def relu_(self):
        pass
    
    def remainder(self):
        '\nremainder(divisor) -> Tensor\n\nSee :func:`torch.remainder`\n'
        pass
    
    def remainder_(self):
        '\nremainder_(divisor) -> Tensor\n\nIn-place version of :meth:`~Tensor.remainder`\n'
        pass
    
    def renorm(self):
        '\nrenorm(p, dim, maxnorm) -> Tensor\n\nSee :func:`torch.renorm`\n'
        pass
    
    def renorm_(self):
        '\nrenorm_(p, dim, maxnorm) -> Tensor\n\nIn-place version of :meth:`~Tensor.renorm`\n'
        pass
    
    def repeat(self):
        "\nrepeat(*sizes) -> Tensor\n\nRepeats this tensor along the specified dimensions.\n\nUnlike :meth:`~Tensor.expand`, this function copies the tensor's data.\n\n.. warning::\n\n    :func:`torch.repeat` behaves differently from\n    `numpy.repeat <https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html>`_,\n    but is more similar to\n    `numpy.tile <https://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html>`_.\n    For the operator similar to `numpy.repeat`, see :func:`torch.repeat_interleave`.\n\nArgs:\n    sizes (torch.Size or int...): The number of times to repeat this tensor along each\n        dimension\n\nExample::\n\n    >>> x = torch.tensor([1, 2, 3])\n    >>> x.repeat(4, 2)\n    tensor([[ 1,  2,  3,  1,  2,  3],\n            [ 1,  2,  3,  1,  2,  3],\n            [ 1,  2,  3,  1,  2,  3],\n            [ 1,  2,  3,  1,  2,  3]])\n    >>> x.repeat(4, 2, 1).size()\n    torch.Size([4, 2, 3])\n"
        pass
    
    def repeat_interleave(self):
        '\nrepeat_interleave(repeats, dim=None) -> Tensor\n\nSee :func:`torch.repeat_interleave`.\n'
        pass
    
    @property
    def requires_grad(self):
        '\nIs ``True`` if gradients need to be computed for this Tensor, ``False`` otherwise.\n\n.. note::\n\n    The fact that gradients need to be computed for a Tensor do not mean that the :attr:`grad`\n    attribute will be populated, see :attr:`is_leaf` for more details.\n\n'
        pass
    
    def requires_grad_(self):
        "\nrequires_grad_(requires_grad=True) -> Tensor\n\nChange if autograd should record operations on this tensor: sets this tensor's\n:attr:`requires_grad` attribute in-place. Returns this tensor.\n\n:func:`require_grad_`'s main use case is to tell autograd to begin recording\noperations on a Tensor ``tensor``. If ``tensor`` has ``requires_grad=False``\n(because it was obtained through a DataLoader, or required preprocessing or\ninitialization), ``tensor.requires_grad_()`` makes it so that autograd will\nbegin to record operations on ``tensor``.\n\nArgs:\n    requires_grad (bool): If autograd should record operations on this tensor.\n        Default: ``True``.\n\nExample::\n\n    >>> # Let's say we want to preprocess some saved weights and use\n    >>> # the result as new weights.\n    >>> saved_weights = [0.1, 0.2, 0.3, 0.25]\n    >>> loaded_weights = torch.tensor(saved_weights)\n    >>> weights = preprocess(loaded_weights)  # some function\n    >>> weights\n    tensor([-0.5503,  0.4926, -2.1158, -0.8303])\n\n    >>> # Now, start to record operations done to weights\n    >>> weights.requires_grad_()\n    >>> out = weights.pow(2).sum()\n    >>> out.backward()\n    >>> weights.grad\n    tensor([-1.1007,  0.9853, -4.2316, -1.6606])\n\n"
        pass
    
    def reshape(self):
        '\nreshape(*shape) -> Tensor\n\nReturns a tensor with the same data and number of elements as :attr:`self`\nbut with the specified shape. This method returns a view if :attr:`shape` is\ncompatible with the current shape. See :meth:`torch.Tensor.view` on when it is\npossible to return a view.\n\nSee :func:`torch.reshape`\n\nArgs:\n    shape (tuple of ints or int...): the desired shape\n\n'
        pass
    
    def reshape_as(self):
        '\nreshape_as(other) -> Tensor\n\nReturns this tensor as the same shape as :attr:`other`.\n``self.reshape_as(other)`` is equivalent to ``self.reshape(other.sizes())``.\nThis method returns a view if ``other.sizes()`` is compatible with the current\nshape. See :meth:`torch.Tensor.view` on when it is possible to return a view.\n\nPlease see :meth:`reshape` for more information about ``reshape``.\n\nArgs:\n    other (:class:`torch.Tensor`): The result tensor has the same shape\n        as :attr:`other`.\n'
        pass
    
    def resize_(self):
        '\nresize_(*sizes) -> Tensor\n\nResizes :attr:`self` tensor to the specified size. If the number of elements is\nlarger than the current storage size, then the underlying storage is resized\nto fit the new number of elements. If the number of elements is smaller, the\nunderlying storage is not changed. Existing elements are preserved but any new\nmemory is uninitialized.\n\n.. warning::\n\n    This is a low-level method. The storage is reinterpreted as C-contiguous,\n    ignoring the current strides (unless the target size equals the current\n    size, in which case the tensor is left unchanged). For most purposes, you\n    will instead want to use :meth:`~Tensor.view()`, which checks for\n    contiguity, or :meth:`~Tensor.reshape()`, which copies data if needed. To\n    change the size in-place with custom strides, see :meth:`~Tensor.set_()`.\n\nArgs:\n    sizes (torch.Size or int...): the desired size\n\nExample::\n\n    >>> x = torch.tensor([[1, 2], [3, 4], [5, 6]])\n    >>> x.resize_(2, 2)\n    tensor([[ 1,  2],\n            [ 3,  4]])\n'
        pass
    
    def resize_as_(self):
        '\nresize_as_(tensor) -> Tensor\n\nResizes the :attr:`self` tensor to be the same size as the specified\n:attr:`tensor`. This is equivalent to ``self.resize_(tensor.size())``.\n'
        pass
    
    def rfft(self):
        '\nrfft(signal_ndim, normalized=False, onesided=True) -> Tensor\n\nSee :func:`torch.rfft`\n'
        pass
    
    def roll(self):
        '\nroll(shifts, dims) -> Tensor\n\nSee :func:`torch.roll`\n'
        pass
    
    def rot90(self):
        '\nrot90(k, dims) -> Tensor\n\nSee :func:`torch.rot90`\n'
        pass
    
    def round(self):
        '\nround() -> Tensor\n\nSee :func:`torch.round`\n'
        pass
    
    def round_(self):
        '\nround_() -> Tensor\n\nIn-place version of :meth:`~Tensor.round`\n'
        pass
    
    def rsqrt(self):
        '\nrsqrt() -> Tensor\n\nSee :func:`torch.rsqrt`\n'
        pass
    
    def rsqrt_(self):
        '\nrsqrt_() -> Tensor\n\nIn-place version of :meth:`~Tensor.rsqrt`\n'
        pass
    
    def scatter(self):
        '\nscatter(dim, index, source) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.scatter_`\n'
        pass
    
    def scatter_(self):
        '\nscatter_(dim, index, src) -> Tensor\n\nWrites all values from the tensor :attr:`src` into :attr:`self` at the indices\nspecified in the :attr:`index` tensor. For each value in :attr:`src`, its output\nindex is specified by its index in :attr:`src` for ``dimension != dim`` and by\nthe corresponding value in :attr:`index` for ``dimension = dim``.\n\nFor a 3-D tensor, :attr:`self` is updated as::\n\n    self[index[i][j][k]][j][k] = src[i][j][k]  # if dim == 0\n    self[i][index[i][j][k]][k] = src[i][j][k]  # if dim == 1\n    self[i][j][index[i][j][k]] = src[i][j][k]  # if dim == 2\n\nThis is the reverse operation of the manner described in :meth:`~Tensor.gather`.\n\n:attr:`self`, :attr:`index` and :attr:`src` (if it is a Tensor) should have same\nnumber of dimensions. It is also required that ``index.size(d) <= src.size(d)``\nfor all dimensions ``d``, and that ``index.size(d) <= self.size(d)`` for all\ndimensions ``d != dim``.\n\nMoreover, as for :meth:`~Tensor.gather`, the values of :attr:`index` must be\nbetween ``0`` and ``self.size(dim) - 1`` inclusive, and all values in a row\nalong the specified dimension :attr:`dim` must be unique.\n\nArgs:\n    dim (int): the axis along which to index\n    index (LongTensor): the indices of elements to scatter,\n      can be either empty or the same size of src.\n      When empty, the operation returns identity\n    src (Tensor): the source element(s) to scatter,\n      incase `value` is not specified\n    value (float): the source element(s) to scatter,\n      incase `src` is not specified\n\nExample::\n\n    >>> x = torch.rand(2, 5)\n    >>> x\n    tensor([[ 0.3992,  0.2908,  0.9044,  0.4850,  0.6004],\n            [ 0.5735,  0.9006,  0.6797,  0.4152,  0.1732]])\n    >>> torch.zeros(3, 5).scatter_(0, torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]]), x)\n    tensor([[ 0.3992,  0.9006,  0.6797,  0.4850,  0.6004],\n            [ 0.0000,  0.2908,  0.0000,  0.4152,  0.0000],\n            [ 0.5735,  0.0000,  0.9044,  0.0000,  0.1732]])\n\n    >>> z = torch.zeros(2, 4).scatter_(1, torch.tensor([[2], [3]]), 1.23)\n    >>> z\n    tensor([[ 0.0000,  0.0000,  1.2300,  0.0000],\n            [ 0.0000,  0.0000,  0.0000,  1.2300]])\n'
        pass
    
    def scatter_add(self):
        '\nscatter_add(dim, index, source) -> Tensor\n\nOut-of-place version of :meth:`torch.Tensor.scatter_add_`\n'
        pass
    
    def scatter_add_(self):
        '\nscatter_add_(dim, index, other) -> Tensor\n\nAdds all values from the tensor :attr:`other` into :attr:`self` at the indices\nspecified in the :attr:`index` tensor in a similar fashion as\n:meth:`~torch.Tensor.scatter_`. For each value in :attr:`other`, it is added to\nan index in :attr:`self` which is specified by its index in :attr:`other`\nfor ``dimension != dim`` and by the corresponding value in :attr:`index` for\n``dimension = dim``.\n\nFor a 3-D tensor, :attr:`self` is updated as::\n\n    self[index[i][j][k]][j][k] += other[i][j][k]  # if dim == 0\n    self[i][index[i][j][k]][k] += other[i][j][k]  # if dim == 1\n    self[i][j][index[i][j][k]] += other[i][j][k]  # if dim == 2\n\n:attr:`self`, :attr:`index` and :attr:`other` should have same number of\ndimensions. It is also required that ``index.size(d) <= other.size(d)`` for all\ndimensions ``d``, and that ``index.size(d) <= self.size(d)`` for all dimensions\n``d != dim``.\n\nMoreover, as for :meth:`~Tensor.gather`, the values of :attr:`index` must be\nbetween ``0`` and ``self.size(dim) - 1`` inclusive, and all values in a row along\nthe specified dimension :attr:`dim` must be unique.\n\n.. include:: cuda_deterministic.rst\n\nArgs:\n    dim (int): the axis along which to index\n    index (LongTensor): the indices of elements to scatter and add,\n      can be either empty or the same size of src.\n      When empty, the operation returns identity.\n    other (Tensor): the source elements to scatter and add\n\nExample::\n\n    >>> x = torch.rand(2, 5)\n    >>> x\n    tensor([[0.7404, 0.0427, 0.6480, 0.3806, 0.8328],\n            [0.7953, 0.2009, 0.9154, 0.6782, 0.9620]])\n    >>> torch.ones(3, 5).scatter_add_(0, torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]]), x)\n    tensor([[1.7404, 1.2009, 1.9154, 1.3806, 1.8328],\n            [1.0000, 1.0427, 1.0000, 1.6782, 1.0000],\n            [1.7953, 1.0000, 1.6480, 1.0000, 1.9620]])\n\n'
        pass
    
    def select(self):
        '\nselect(dim, index) -> Tensor\n\nSlices the :attr:`self` tensor along the selected dimension at the given index.\nThis function returns a tensor with the given dimension removed.\n\nArgs:\n    dim (int): the dimension to slice\n    index (int): the index to select with\n\n.. note::\n\n    :meth:`select` is equivalent to slicing. For example,\n    ``tensor.select(0, index)`` is equivalent to ``tensor[index]`` and\n    ``tensor.select(2, index)`` is equivalent to ``tensor[:,:,index]``.\n'
        pass
    
    def set_(self):
        '\nset_(source=None, storage_offset=0, size=None, stride=None) -> Tensor\n\nSets the underlying storage, size, and strides. If :attr:`source` is a tensor,\n:attr:`self` tensor will share the same storage and have the same size and\nstrides as :attr:`source`. Changes to elements in one tensor will be reflected\nin the other.\n\nIf :attr:`source` is a :class:`~torch.Storage`, the method sets the underlying\nstorage, offset, size, and stride.\n\nArgs:\n    source (Tensor or Storage): the tensor or storage to use\n    storage_offset (int, optional): the offset in the storage\n    size (torch.Size, optional): the desired size. Defaults to the size of the source.\n    stride (tuple, optional): the desired stride. Defaults to C-contiguous strides.\n'
        pass
    
    @property
    def shape(self):
        pass
    
    def short(self):
        '\nshort() -> Tensor\n\n``self.short()`` is equivalent to ``self.to(torch.int16)``. See :func:`to`.\n'
        pass
    
    def sigmoid(self):
        '\nsigmoid() -> Tensor\n\nSee :func:`torch.sigmoid`\n'
        pass
    
    def sigmoid_(self):
        '\nsigmoid_() -> Tensor\n\nIn-place version of :meth:`~Tensor.sigmoid`\n'
        pass
    
    def sign(self):
        '\nsign() -> Tensor\n\nSee :func:`torch.sign`\n'
        pass
    
    def sign_(self):
        '\nsign_() -> Tensor\n\nIn-place version of :meth:`~Tensor.sign`\n'
        pass
    
    def sin(self):
        '\nsin() -> Tensor\n\nSee :func:`torch.sin`\n'
        pass
    
    def sin_(self):
        '\nsin_() -> Tensor\n\nIn-place version of :meth:`~Tensor.sin`\n'
        pass
    
    def sinh(self):
        '\nsinh() -> Tensor\n\nSee :func:`torch.sinh`\n'
        pass
    
    def sinh_(self):
        '\nsinh_() -> Tensor\n\nIn-place version of :meth:`~Tensor.sinh`\n'
        pass
    
    def size(self):
        '\nsize() -> torch.Size\n\nReturns the size of the :attr:`self` tensor. The returned value is a subclass of\n:class:`tuple`.\n\nExample::\n\n    >>> torch.empty(3, 4, 5).size()\n    torch.Size([3, 4, 5])\n\n'
        pass
    
    def slogdet(self):
        '\nslogdet() -> (Tensor, Tensor)\n\nSee :func:`torch.slogdet`\n'
        pass
    
    def smm(self):
        pass
    
    def softmax(self):
        pass
    
    def solve(self):
        '\nsolve(A) -> Tensor, Tensor\n\nSee :func:`torch.solve`\n'
        pass
    
    def sort(self):
        '\nsort(dim=-1, descending=False) -> (Tensor, LongTensor)\n\nSee :func:`torch.sort`\n'
        pass
    
    def sparse_dim(self):
        '\nsparse_dim() -> int\n\nIf :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),\nthis returns a the number of sparse dimensions. Otherwise, this throws an\nerror.\n\nSee also :meth:`Tensor.dense_dim`.\n'
        pass
    
    def sparse_mask(self):
        '\nsparse_mask(input, mask) -> Tensor\n\nReturns a new SparseTensor with values from Tensor :attr:`input` filtered\nby indices of :attr:`mask` and values are ignored. :attr:`input` and :attr:`mask`\nmust have the same shape.\n\nArgs:\n    input (Tensor): an input Tensor\n    mask (SparseTensor): a SparseTensor which we filter :attr:`input` based on its indices\n\nExample::\n\n    >>> nnz = 5\n    >>> dims = [5, 5, 2, 2]\n    >>> I = torch.cat([torch.randint(0, dims[0], size=(nnz,)),\n                       torch.randint(0, dims[1], size=(nnz,))], 0).reshape(2, nnz)\n    >>> V = torch.randn(nnz, dims[2], dims[3])\n    >>> size = torch.Size(dims)\n    >>> S = torch.sparse_coo_tensor(I, V, size).coalesce()\n    >>> D = torch.randn(dims)\n    >>> D.sparse_mask(S)\n    tensor(indices=tensor([[0, 0, 0, 2],\n                           [0, 1, 4, 3]]),\n           values=tensor([[[ 1.6550,  0.2397],\n                           [-0.1611, -0.0779]],\n\n                          [[ 0.2326, -1.0558],\n                           [ 1.4711,  1.9678]],\n\n                          [[-0.5138, -0.0411],\n                           [ 1.9417,  0.5158]],\n\n                          [[ 0.0793,  0.0036],\n                           [-0.2569, -0.1055]]]),\n           size=(5, 5, 2, 2), nnz=4, layout=torch.sparse_coo)\n'
        pass
    
    def sparse_resize_(self):
        pass
    
    def sparse_resize_and_clear_(self):
        pass
    
    def split(self):
        pass
    
    def split_with_sizes(self):
        pass
    
    def sqrt(self):
        '\nsqrt() -> Tensor\n\nSee :func:`torch.sqrt`\n'
        pass
    
    def sqrt_(self):
        '\nsqrt_() -> Tensor\n\nIn-place version of :meth:`~Tensor.sqrt`\n'
        pass
    
    def squeeze(self):
        '\nsqueeze(dim=None) -> Tensor\n\nSee :func:`torch.squeeze`\n'
        pass
    
    def squeeze_(self):
        '\nsqueeze_(dim=None) -> Tensor\n\nIn-place version of :meth:`~Tensor.squeeze`\n'
        pass
    
    def sspaddmm(self):
        pass
    
    def std(self):
        '\nstd(dim=None, unbiased=True, keepdim=False) -> Tensor\n\nSee :func:`torch.std`\n'
        pass
    
    def stft(self):
        '\nstft(frame_length, hop, fft_size=None, return_onesided=True, window=None, pad_end=0) -> Tensor\n\nSee :func:`torch.stft`\n'
        pass
    
    def storage(self):
        '\nstorage() -> torch.Storage\n\nReturns the underlying storage.\n'
        pass
    
    def storage_offset(self):
        "\nstorage_offset() -> int\n\nReturns :attr:`self` tensor's offset in the underlying storage in terms of\nnumber of storage elements (not bytes).\n\nExample::\n\n    >>> x = torch.tensor([1, 2, 3, 4, 5])\n    >>> x.storage_offset()\n    0\n    >>> x[3:].storage_offset()\n    3\n\n"
        pass
    
    def storage_type(self):
        '\nstorage_type() -> type\n\nReturns the type of the underlying storage.\n'
        pass
    
    def stride(self):
        '\nstride(dim) -> tuple or int\n\nReturns the stride of :attr:`self` tensor.\n\nStride is the jump necessary to go from one element to the next one in the\nspecified dimension :attr:`dim`. A tuple of all strides is returned when no\nargument is passed in. Otherwise, an integer value is returned as the stride in\nthe particular dimension :attr:`dim`.\n\nArgs:\n    dim (int, optional): the desired dimension in which stride is required\n\nExample::\n\n    >>> x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])\n    >>> x.stride()\n    (5, 1)\n    >>>x.stride(0)\n    5\n    >>> x.stride(-1)\n    1\n\n'
        pass
    
    def sub(self):
        '\nsub(value, other) -> Tensor\n\nSubtracts a scalar or tensor from :attr:`self` tensor. If both :attr:`value` and\n:attr:`other` are specified, each element of :attr:`other` is scaled by\n:attr:`value` before being used.\n\nWhen :attr:`other` is a tensor, the shape of :attr:`other` must be\n:ref:`broadcastable <broadcasting-semantics>` with the shape of the underlying\ntensor.\n\n'
        pass
    
    def sub_(self):
        '\nsub_(x) -> Tensor\n\nIn-place version of :meth:`~Tensor.sub`\n'
        pass
    
    def sum(self):
        '\nsum(dim=None, keepdim=False, dtype=None) -> Tensor\n\nSee :func:`torch.sum`\n'
        pass
    
    def sum_to_size(self):
        '\nsum_to_size(*size) -> Tensor\n\nSum ``this`` tensor to :attr:`size`.\n:attr:`size` must be broadcastable to ``this`` tensor size.\nArgs:\n    other (:class:`torch.Tensor`): The result tensor has the same size\n        as :attr:`other`.\n'
        pass
    
    def svd(self):
        '\nsvd(some=True, compute_uv=True) -> (Tensor, Tensor, Tensor)\n\nSee :func:`torch.svd`\n'
        pass
    
    def symeig(self):
        '\nsymeig(eigenvectors=False, upper=True) -> (Tensor, Tensor)\n\nSee :func:`torch.symeig`\n'
        pass
    
    def t(self):
        '\nt() -> Tensor\n\nSee :func:`torch.t`\n'
        pass
    
    def t_(self):
        '\nt_() -> Tensor\n\nIn-place version of :meth:`~Tensor.t`\n'
        pass
    
    def take(self):
        '\ntake(indices) -> Tensor\n\nSee :func:`torch.take`\n'
        pass
    
    def tan(self):
        '\ntan() -> Tensor\n\nSee :func:`torch.tan`\n'
        pass
    
    def tan_(self):
        '\ntan_() -> Tensor\n\nIn-place version of :meth:`~Tensor.tan`\n'
        pass
    
    def tanh(self):
        '\ntanh() -> Tensor\n\nSee :func:`torch.tanh`\n'
        pass
    
    def tanh_(self):
        '\ntanh_() -> Tensor\n\nIn-place version of :meth:`~Tensor.tanh`\n'
        pass
    
    def to(self):
        "\nto(*args, **kwargs) -> Tensor\n\nPerforms Tensor dtype and/or device conversion. A :class:`torch.dtype` and :class:`torch.device` are\ninferred from the arguments of ``self.to(*args, **kwargs)``.\n\n.. note::\n\n    If the ``self`` Tensor already\n    has the correct :class:`torch.dtype` and :class:`torch.device`, then ``self`` is returned.\n    Otherwise, the returned tensor is a copy of ``self`` with the desired\n    :class:`torch.dtype` and :class:`torch.device`.\n\nHere are the ways to call ``to``:\n\n.. function:: to(dtype, non_blocking=False, copy=False) -> Tensor\n\n    Returns a Tensor with the specified :attr:`dtype`\n\n.. function:: to(device=None, dtype=None, non_blocking=False, copy=False) -> Tensor\n\n    Returns a Tensor with the specified :attr:`device` and (optional)\n    :attr:`dtype`. If :attr:`dtype` is ``None`` it is inferred to be ``self.dtype``.\n    When :attr:`non_blocking`, tries to convert asynchronously with respect to\n    the host if possible, e.g., converting a CPU Tensor with pinned memory to a\n    CUDA Tensor.\n    When :attr:`copy` is set, a new Tensor is created even when the Tensor\n    already matches the desired conversion.\n\n.. function:: to(other, non_blocking=False, copy=False) -> Tensor\n\n    Returns a Tensor with same :class:`torch.dtype` and :class:`torch.device` as\n    the Tensor :attr:`other`. When :attr:`non_blocking`, tries to convert\n    asynchronously with respect to the host if possible, e.g., converting a CPU\n    Tensor with pinned memory to a CUDA Tensor.\n    When :attr:`copy` is set, a new Tensor is created even when the Tensor\n    already matches the desired conversion.\n\nExample::\n\n    >>> tensor = torch.randn(2, 2)  # Initially dtype=float32, device=cpu\n    >>> tensor.to(torch.float64)\n    tensor([[-0.5044,  0.0005],\n            [ 0.3310, -0.0584]], dtype=torch.float64)\n\n    >>> cuda0 = torch.device('cuda:0')\n    >>> tensor.to(cuda0)\n    tensor([[-0.5044,  0.0005],\n            [ 0.3310, -0.0584]], device='cuda:0')\n\n    >>> tensor.to(cuda0, dtype=torch.float64)\n    tensor([[-0.5044,  0.0005],\n            [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')\n\n    >>> other = torch.randn((), dtype=torch.float64, device=cuda0)\n    >>> tensor.to(other, non_blocking=True)\n    tensor([[-0.5044,  0.0005],\n            [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')\n\n"
        pass
    
    def to_dense(self):
        pass
    
    def to_mkldnn(self):
        '\nto_mkldnn() -> Tensor\nReturns a copy of the tensor in ``torch.mkldnn`` layout.\n\n'
        pass
    
    def to_sparse(self):
        '\nto_sparse(sparseDims) -> Tensor\nReturns a sparse copy of the tensor.  PyTorch supports sparse tensors in\n:ref:`coordinate format <sparse-docs>`.\n\nArgs:\n    sparseDims (int, optional): the number of sparse dimensions to include in the new sparse tensor\n\nExample::\n\n    >>> d = torch.tensor([[0, 0, 0], [9, 0, 10], [0, 0, 0]])\n    >>> d\n    tensor([[ 0,  0,  0],\n            [ 9,  0, 10],\n            [ 0,  0,  0]])\n    >>> d.to_sparse()\n    tensor(indices=tensor([[1, 1],\n                           [0, 2]]),\n           values=tensor([ 9, 10]),\n           size=(3, 3), nnz=2, layout=torch.sparse_coo)\n    >>> d.to_sparse(1)\n    tensor(indices=tensor([[1]]),\n           values=tensor([[ 9,  0, 10]]),\n           size=(3, 3), nnz=1, layout=torch.sparse_coo)\n'
        pass
    
    def tolist(self):
        '"\ntolist() -> list or number\n\nReturns the tensor as a (nested) list. For scalars, a standard\nPython number is returned, just like with :meth:`~Tensor.item`.\nTensors are automatically moved to the CPU first if necessary.\n\nThis operation is not differentiable.\n\nExamples::\n\n    >>> a = torch.randn(2, 2)\n    >>> a.tolist()\n    [[0.012766935862600803, 0.5415473580360413],\n     [-0.08909505605697632, 0.7729271650314331]]\n    >>> a[0,0].tolist()\n    0.012766935862600803\n'
        pass
    
    def topk(self):
        '\ntopk(k, dim=None, largest=True, sorted=True) -> (Tensor, LongTensor)\n\nSee :func:`torch.topk`\n'
        pass
    
    def trace(self):
        '\ntrace() -> Tensor\n\nSee :func:`torch.trace`\n'
        pass
    
    def transpose(self):
        '\ntranspose(dim0, dim1) -> Tensor\n\nSee :func:`torch.transpose`\n'
        pass
    
    def transpose_(self):
        '\ntranspose_(dim0, dim1) -> Tensor\n\nIn-place version of :meth:`~Tensor.transpose`\n'
        pass
    
    def triangular_solve(self):
        '\ntriangular_solve(A, upper=True, transpose=False, unitriangular=False) -> (Tensor, Tensor)\n\nSee :func:`torch.triangular_solve`\n'
        pass
    
    def tril(self):
        '\ntril(k=0) -> Tensor\n\nSee :func:`torch.tril`\n'
        pass
    
    def tril_(self):
        '\ntril_(k=0) -> Tensor\n\nIn-place version of :meth:`~Tensor.tril`\n'
        pass
    
    def triu(self):
        '\ntriu(k=0) -> Tensor\n\nSee :func:`torch.triu`\n'
        pass
    
    def triu_(self):
        '\ntriu_(k=0) -> Tensor\n\nIn-place version of :meth:`~Tensor.triu`\n'
        pass
    
    def trunc(self):
        '\ntrunc() -> Tensor\n\nSee :func:`torch.trunc`\n'
        pass
    
    def trunc_(self):
        '\ntrunc_() -> Tensor\n\nIn-place version of :meth:`~Tensor.trunc`\n'
        pass
    
    def type(self):
        '\ntype(dtype=None, non_blocking=False, **kwargs) -> str or Tensor\nReturns the type if `dtype` is not provided, else casts this object to\nthe specified type.\n\nIf this is already of the correct type, no copy is performed and the\noriginal object is returned.\n\nArgs:\n    dtype (type or string): The desired type\n    non_blocking (bool): If ``True``, and the source is in pinned memory\n        and destination is on the GPU or vice versa, the copy is performed\n        asynchronously with respect to the host. Otherwise, the argument\n        has no effect.\n    **kwargs: For compatibility, may contain the key ``async`` in place of\n        the ``non_blocking`` argument. The ``async`` arg is deprecated.\n'
        pass
    
    def type_as(self):
        '\ntype_as(tensor) -> Tensor\n\nReturns this tensor cast to the type of the given tensor.\n\nThis is a no-op if the tensor is already of the correct type. This is\nequivalent to ``self.type(tensor.type())``\n\nArgs:\n    tensor (Tensor): the tensor which has the desired type\n'
        pass
    
    def unbind(self):
        '\nunbind(dim=0) -> seq\n\nSee :func:`torch.unbind`\n'
        pass
    
    def unfold(self):
        '\nunfold(dimension, size, step) -> Tensor\n\nReturns a tensor which contains all slices of size :attr:`size` from\n:attr:`self` tensor in the dimension :attr:`dimension`.\n\nStep between two slices is given by :attr:`step`.\n\nIf `sizedim` is the size of dimension :attr:`dimension` for :attr:`self`, the size of\ndimension :attr:`dimension` in the returned tensor will be\n`(sizedim - size) / step + 1`.\n\nAn additional dimension of size :attr:`size` is appended in the returned tensor.\n\nArgs:\n    dimension (int): dimension in which unfolding happens\n    size (int): the size of each slice that is unfolded\n    step (int): the step between each slice\n\nExample::\n\n    >>> x = torch.arange(1., 8)\n    >>> x\n    tensor([ 1.,  2.,  3.,  4.,  5.,  6.,  7.])\n    >>> x.unfold(0, 2, 1)\n    tensor([[ 1.,  2.],\n            [ 2.,  3.],\n            [ 3.,  4.],\n            [ 4.,  5.],\n            [ 5.,  6.],\n            [ 6.,  7.]])\n    >>> x.unfold(0, 2, 2)\n    tensor([[ 1.,  2.],\n            [ 3.,  4.],\n            [ 5.,  6.]])\n'
        pass
    
    def uniform_(self):
        '\nuniform_(from=0, to=1) -> Tensor\n\nFills :attr:`self` tensor with numbers sampled from the continuous uniform\ndistribution:\n\n.. math::\n    P(x) = \\dfrac{1}{\\text{to} - \\text{from}}\n'
        pass
    
    def unsqueeze(self):
        '\nunsqueeze(dim) -> Tensor\n\nSee :func:`torch.unsqueeze`\n'
        pass
    
    def unsqueeze_(self):
        '\nunsqueeze_(dim) -> Tensor\n\nIn-place version of :meth:`~Tensor.unsqueeze`\n'
        pass
    
    def values(self):
        '\nvalues() -> Tensor\n\nIf :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),\nthis returns a view of the contained values tensor. Otherwise, this throws an\nerror.\n\nSee also :meth:`Tensor.indices`.\n\n.. note::\n  This method can only be called on a coalesced sparse tensor. See\n  :meth:`Tensor.coalesce` for details.\n'
        pass
    
    def var(self):
        '\nvar(dim=None, unbiased=True, keepdim=False) -> Tensor\n\nSee :func:`torch.var`\n'
        pass
    
    def view(self):
        '\nview(*shape) -> Tensor\n\nReturns a new tensor with the same data as the :attr:`self` tensor but of a\ndifferent :attr:`shape`.\n\nThe returned tensor shares the same data and must have the same number\nof elements, but may have a different size. For a tensor to be viewed, the new\nview size must be compatible with its original size and stride, i.e., each new\nview dimension must either be a subspace of an original dimension, or only span\nacross original dimensions :math:`d, d+1, \\dots, d+k` that satisfy the following\ncontiguity-like condition that :math:`\\forall i = 0, \\dots, k-1`,\n\n.. math::\n\n  \\text{stride}[i] = \\text{stride}[i+1] \\times \\text{size}[i+1]\n\nOtherwise, :meth:`contiguous` needs to be called before the tensor can be\nviewed. See also: :meth:`reshape`, which returns a view if the shapes are\ncompatible, and copies (equivalent to calling :meth:`contiguous`) otherwise.\n\nArgs:\n    shape (torch.Size or int...): the desired size\n\nExample::\n\n    >>> x = torch.randn(4, 4)\n    >>> x.size()\n    torch.Size([4, 4])\n    >>> y = x.view(16)\n    >>> y.size()\n    torch.Size([16])\n    >>> z = x.view(-1, 8)  # the size -1 is inferred from other dimensions\n    >>> z.size()\n    torch.Size([2, 8])\n\n    >>> a = torch.randn(1, 2, 3, 4)\n    >>> a.size()\n    torch.Size([1, 2, 3, 4])\n    >>> b = a.transpose(1, 2)  # Swaps 2nd and 3rd dimension\n    >>> b.size()\n    torch.Size([1, 3, 2, 4])\n    >>> c = a.view(1, 3, 2, 4)  # Does not change tensor layout in memory\n    >>> c.size()\n    torch.Size([1, 3, 2, 4])\n    >>> torch.equal(b, c)\n    False\n\n'
        pass
    
    def view_as(self):
        '\nview_as(other) -> Tensor\n\nView this tensor as the same size as :attr:`other`.\n``self.view_as(other)`` is equivalent to ``self.view(other.size())``.\n\nPlease see :meth:`~Tensor.view` for more information about ``view``.\n\nArgs:\n    other (:class:`torch.Tensor`): The result tensor has the same size\n        as :attr:`other`.\n'
        pass
    
    @property
    def volatile(self):
        pass
    
    def where(self):
        '\nwhere(condition, y) -> Tensor\n\n``self.where(condition, y)`` is equivalent to ``torch.where(condition, self, y)``.\nSee :func:`torch.where`\n'
        pass
    
    def zero_(self):
        '\nzero_() -> Tensor\n\nFills :attr:`self` tensor with zeros.\n'
        pass
    

class _VariableFunctions(_mod_builtins.object):
    @classmethod
    def __and__(cls):
        return _VariableFunctions()
    
    __class__ = _VariableFunctions
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __lshift__(cls):
        return _VariableFunctions()
    
    @classmethod
    def __or__(cls):
        return _VariableFunctions()
    
    @classmethod
    def __rshift__(cls):
        return _VariableFunctions()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def __xor__(cls):
        return _VariableFunctions()
    
    @classmethod
    def _adaptive_avg_pool2d(cls):
        pass
    
    @classmethod
    def _baddbmm_mkl_(cls):
        pass
    
    @classmethod
    def _batch_norm_impl_index(cls):
        pass
    
    @classmethod
    def _cast_Byte(cls):
        pass
    
    @classmethod
    def _cast_Char(cls):
        pass
    
    @classmethod
    def _cast_Double(cls):
        pass
    
    @classmethod
    def _cast_Float(cls):
        pass
    
    @classmethod
    def _cast_Half(cls):
        pass
    
    @classmethod
    def _cast_Int(cls):
        pass
    
    @classmethod
    def _cast_Long(cls):
        pass
    
    @classmethod
    def _cast_Short(cls):
        pass
    
    @classmethod
    def _convolution(cls):
        pass
    
    @classmethod
    def _convolution_nogroup(cls):
        pass
    
    @classmethod
    def _copy_same_type_(cls):
        pass
    
    @classmethod
    def _ctc_loss(cls):
        pass
    
    @classmethod
    def _cudnn_ctc_loss(cls):
        pass
    
    @classmethod
    def _cudnn_init_dropout_state(cls):
        pass
    
    @classmethod
    def _cudnn_rnn(cls):
        pass
    
    @classmethod
    def _cudnn_rnn_flatten_weight(cls):
        pass
    
    @classmethod
    def _cufft_clear_plan_cache(cls):
        pass
    
    @classmethod
    def _cufft_get_plan_cache_max_size(cls):
        pass
    
    @classmethod
    def _cufft_get_plan_cache_size(cls):
        pass
    
    @classmethod
    def _cufft_set_plan_cache_max_size(cls):
        pass
    
    @classmethod
    def _debug_has_internal_overlap(cls):
        pass
    
    @classmethod
    def _dim_arange(cls):
        pass
    
    @classmethod
    def _dirichlet_grad(cls):
        pass
    
    @classmethod
    def _embedding_bag(cls):
        pass
    
    @classmethod
    def _empty_affine_quantized(cls):
        pass
    
    @classmethod
    def _fft_with_size(cls):
        pass
    
    @classmethod
    def _fused_dropout(cls):
        pass
    
    @classmethod
    def _log_softmax(cls):
        pass
    
    @classmethod
    def _log_softmax_backward_data(cls):
        pass
    
    @classmethod
    def _lu_with_info(cls):
        pass
    
    @classmethod
    def _masked_scale(cls):
        pass
    
    @classmethod
    def _multinomial_alias_draw(cls):
        pass
    
    @classmethod
    def _multinomial_alias_setup(cls):
        pass
    
    @classmethod
    def _nnpack_available(cls):
        pass
    
    @classmethod
    def _nnpack_spatial_convolution(cls):
        pass
    
    @classmethod
    def _pack_padded_sequence(cls):
        pass
    
    @classmethod
    def _pad_packed_sequence(cls):
        pass
    
    @classmethod
    def _promote_types(cls):
        pass
    
    @classmethod
    def _reshape_from_tensor(cls):
        pass
    
    @classmethod
    def _s_copy_from(cls):
        pass
    
    @classmethod
    def _s_where(cls):
        pass
    
    @classmethod
    def _sample_dirichlet(cls):
        pass
    
    @classmethod
    def _shape_as_tensor(cls):
        pass
    
    @classmethod
    def _sobol_engine_draw(cls):
        pass
    
    @classmethod
    def _sobol_engine_ff_(cls):
        pass
    
    @classmethod
    def _sobol_engine_initialize_state_(cls):
        pass
    
    @classmethod
    def _sobol_engine_scramble_(cls):
        pass
    
    @classmethod
    def _softmax(cls):
        pass
    
    @classmethod
    def _softmax_backward_data(cls):
        pass
    
    @classmethod
    def _sparse_addmm(cls):
        pass
    
    @classmethod
    def _sparse_mm(cls):
        pass
    
    @classmethod
    def _sparse_sum(cls):
        pass
    
    @classmethod
    def _standard_gamma(cls):
        pass
    
    @classmethod
    def _standard_gamma_grad(cls):
        pass
    
    @classmethod
    def _trilinear(cls):
        pass
    
    @classmethod
    def _unique(cls):
        pass
    
    @classmethod
    def _unique2(cls):
        pass
    
    @classmethod
    def _weight_norm(cls):
        pass
    
    @classmethod
    def _weight_norm_cuda_interface(cls):
        pass
    
    @classmethod
    def abs(cls):
        '\nabs(input, out=None) -> Tensor\n\nComputes the element-wise absolute value of the given :attr:`input` tensor.\n\n.. math::\n    \\text{out}_{i} = |\\text{input}_{i}|\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.abs(torch.tensor([-1, -2, 3]))\n    tensor([ 1,  2,  3])\n'
        pass
    
    @classmethod
    def abs_(cls):
        pass
    
    @classmethod
    def acos(cls):
        '\nacos(input, out=None) -> Tensor\n\nReturns a new tensor with the arccosine  of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\cos^{-1}(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.3348, -0.5889,  0.2005, -0.1584])\n    >>> torch.acos(a)\n    tensor([ 1.2294,  2.2004,  1.3690,  1.7298])\n'
        pass
    
    @classmethod
    def acos_(cls):
        pass
    
    @classmethod
    def adaptive_avg_pool1d(cls):
        '\nadaptive_avg_pool1d(input, output_size) -> Tensor\n\nApplies a 1D adaptive average pooling over an input signal composed of\nseveral input planes.\n\nSee :class:`~torch.nn.AdaptiveAvgPool1d` for details and output shape.\n\nArgs:\n    output_size: the target output size (single integer)\n'
        pass
    
    @classmethod
    def adaptive_max_pool1d(cls):
        pass
    
    @classmethod
    def add(cls):
        '\n.. function:: add(input, value, out=None)\n\nAdds the scalar :attr:`value` to each element of the input :attr:`input`\nand returns a new resulting tensor.\n\n.. math::\n    \\text{out} = \\text{input} + \\text{value}\n\nIf :attr:`input` is of type FloatTensor or DoubleTensor, :attr:`value` must be\na real number, otherwise it should be an integer.\n\nArgs:\n    input (Tensor): the input tensor\n    value (Number): the number to be added to each element of :attr:`input`\n\nKeyword arguments:\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.0202,  1.0985,  1.3506, -0.6056])\n    >>> torch.add(a, 20)\n    tensor([ 20.0202,  21.0985,  21.3506,  19.3944])\n\n.. function:: add(input, value=1, other, out=None)\n\nEach element of the tensor :attr:`other` is multiplied by the scalar\n:attr:`value` and added to each element of the tensor :attr:`input`.\nThe resulting tensor is returned.\n\nThe shapes of :attr:`input` and :attr:`other` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\n.. math::\n    \\text{out} = \\text{input} + \\text{value} \\times \\text{other}\n\nIf :attr:`other` is of type FloatTensor or DoubleTensor, :attr:`value` must be\na real number, otherwise it should be an integer.\n\nArgs:\n    input (Tensor): the first input tensor\n    value (Number): the scalar multiplier for :attr:`other`\n    other (Tensor): the second input tensor\n\nKeyword arguments:\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.9732, -0.3497,  0.6245,  0.4022])\n    >>> b = torch.randn(4, 1)\n    >>> b\n    tensor([[ 0.3743],\n            [-1.7724],\n            [-0.5811],\n            [-0.8017]])\n    >>> torch.add(a, 10, b)\n    tensor([[  2.7695,   3.3930,   4.3672,   4.1450],\n            [-18.6971, -18.0736, -17.0994, -17.3216],\n            [ -6.7845,  -6.1610,  -5.1868,  -5.4090],\n            [ -8.9902,  -8.3667,  -7.3925,  -7.6147]])\n'
        pass
    
    @classmethod
    def addbmm(cls):
        '\naddbmm(beta=1, mat, alpha=1, batch1, batch2, out=None) -> Tensor\n\nPerforms a batch matrix-matrix product of matrices stored\nin :attr:`batch1` and :attr:`batch2`,\nwith a reduced add step (all matrix multiplications get accumulated\nalong the first dimension).\n:attr:`mat` is added to the final result.\n\n:attr:`batch1` and :attr:`batch2` must be 3-D tensors each containing the\nsame number of matrices.\n\nIf :attr:`batch1` is a :math:`(b \\times n \\times m)` tensor, :attr:`batch2` is a\n:math:`(b \\times m \\times p)` tensor, :attr:`mat` must be\n:ref:`broadcastable <broadcasting-semantics>` with a :math:`(n \\times p)` tensor\nand :attr:`out` will be a :math:`(n \\times p)` tensor.\n\n.. math::\n    out = \\beta\\ \\text{mat} + \\alpha\\ (\\sum_{i=0}^{b-1} \\text{batch1}_i \\mathbin{@} \\text{batch2}_i)\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, arguments :attr:`beta` and :attr:`alpha`\nmust be real numbers, otherwise they should be integers.\n\nArgs:\n    beta (Number, optional): multiplier for :attr:`mat` (:math:`\\beta`)\n    mat (Tensor): matrix to be added\n    alpha (Number, optional): multiplier for `batch1 @ batch2` (:math:`\\alpha`)\n    batch1 (Tensor): the first batch of matrices to be multiplied\n    batch2 (Tensor): the second batch of matrices to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> M = torch.randn(3, 5)\n    >>> batch1 = torch.randn(10, 3, 4)\n    >>> batch2 = torch.randn(10, 4, 5)\n    >>> torch.addbmm(M, batch1, batch2)\n    tensor([[  6.6311,   0.0503,   6.9768, -12.0362,  -2.1653],\n            [ -4.8185,  -1.4255,  -6.6760,   8.9453,   2.5743],\n            [ -3.8202,   4.3691,   1.0943,  -1.1109,   5.4730]])\n'
        pass
    
    @classmethod
    def addcdiv(cls):
        '\naddcdiv(tensor, value=1, tensor1, tensor2, out=None) -> Tensor\n\nPerforms the element-wise division of :attr:`tensor1` by :attr:`tensor2`,\nmultiply the result by the scalar :attr:`value` and add it to :attr:`tensor`.\n\n.. math::\n    \\text{out}_i = \\text{tensor}_i + \\text{value} \\times \\frac{\\text{tensor1}_i}{\\text{tensor2}_i}\n\nThe shapes of :attr:`tensor`, :attr:`tensor1`, and :attr:`tensor2` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, :attr:`value` must be\na real number, otherwise an integer.\n\nArgs:\n    tensor (Tensor): the tensor to be added\n    value (Number, optional): multiplier for :math:`\\text{tensor1} / \\text{tensor2}`\n    tensor1 (Tensor): the numerator tensor\n    tensor2 (Tensor): the denominator tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> t = torch.randn(1, 3)\n    >>> t1 = torch.randn(3, 1)\n    >>> t2 = torch.randn(1, 3)\n    >>> torch.addcdiv(t, 0.1, t1, t2)\n    tensor([[-0.2312, -3.6496,  0.1312],\n            [-1.0428,  3.4292, -0.1030],\n            [-0.5369, -0.9829,  0.0430]])\n'
        pass
    
    @classmethod
    def addcmul(cls):
        '\naddcmul(tensor, value=1, tensor1, tensor2, out=None) -> Tensor\n\nPerforms the element-wise multiplication of :attr:`tensor1`\nby :attr:`tensor2`, multiply the result by the scalar :attr:`value`\nand add it to :attr:`tensor`.\n\n.. math::\n    \\text{out}_i = \\text{tensor}_i + \\text{value} \\times \\text{tensor1}_i \\times \\text{tensor2}_i\n\nThe shapes of :attr:`tensor`, :attr:`tensor1`, and :attr:`tensor2` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, :attr:`value` must be\na real number, otherwise an integer.\n\nArgs:\n    tensor (Tensor): the tensor to be added\n    value (Number, optional): multiplier for :math:`tensor1 .* tensor2`\n    tensor1 (Tensor): the tensor to be multiplied\n    tensor2 (Tensor): the tensor to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> t = torch.randn(1, 3)\n    >>> t1 = torch.randn(3, 1)\n    >>> t2 = torch.randn(1, 3)\n    >>> torch.addcmul(t, 0.1, t1, t2)\n    tensor([[-0.8635, -0.6391,  1.6174],\n            [-0.7617, -0.5879,  1.7388],\n            [-0.8353, -0.6249,  1.6511]])\n'
        pass
    
    @classmethod
    def addmm(cls):
        '\naddmm(beta=1, mat, alpha=1, mat1, mat2, out=None) -> Tensor\n\nPerforms a matrix multiplication of the matrices :attr:`mat1` and :attr:`mat2`.\nThe matrix :attr:`mat` is added to the final result.\n\nIf :attr:`mat1` is a :math:`(n \\times m)` tensor, :attr:`mat2` is a\n:math:`(m \\times p)` tensor, then :attr:`mat` must be\n:ref:`broadcastable <broadcasting-semantics>` with a :math:`(n \\times p)` tensor\nand :attr:`out` will be a :math:`(n \\times p)` tensor.\n\n:attr:`alpha` and :attr:`beta` are scaling factors on matrix-vector product between\n:attr:`mat1` and :attr:`mat2` and the added matrix :attr:`mat` respectively.\n\n.. math::\n    \\text{out} = \\beta\\ \\text{mat} + \\alpha\\ (\\text{mat1}_i \\mathbin{@} \\text{mat2}_i)\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, arguments :attr:`beta` and\n:attr:`alpha` must be real numbers, otherwise they should be integers.\n\nArgs:\n    beta (Number, optional): multiplier for :attr:`mat` (:math:`\\beta`)\n    mat (Tensor): matrix to be added\n    alpha (Number, optional): multiplier for :math:`mat1 @ mat2` (:math:`\\alpha`)\n    mat1 (Tensor): the first matrix to be multiplied\n    mat2 (Tensor): the second matrix to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> M = torch.randn(2, 3)\n    >>> mat1 = torch.randn(2, 3)\n    >>> mat2 = torch.randn(3, 3)\n    >>> torch.addmm(M, mat1, mat2)\n    tensor([[-4.8716,  1.4671, -1.3746],\n            [ 0.7573, -3.9555, -2.8681]])\n'
        pass
    
    @classmethod
    def addmv(cls):
        '\naddmv(beta=1, tensor, alpha=1, mat, vec, out=None) -> Tensor\n\nPerforms a matrix-vector product of the matrix :attr:`mat` and\nthe vector :attr:`vec`.\nThe vector :attr:`tensor` is added to the final result.\n\nIf :attr:`mat` is a :math:`(n \\times m)` tensor, :attr:`vec` is a 1-D tensor of\nsize `m`, then :attr:`tensor` must be\n:ref:`broadcastable <broadcasting-semantics>` with a 1-D tensor of size `n` and\n:attr:`out` will be 1-D tensor of size `n`.\n\n:attr:`alpha` and :attr:`beta` are scaling factors on matrix-vector product between\n:attr:`mat` and :attr:`vec` and the added tensor :attr:`tensor` respectively.\n\n.. math::\n    \\text{out} = \\beta\\ \\text{tensor} + \\alpha\\ (\\text{mat} \\mathbin{@} \\text{vec})\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, arguments :attr:`beta` and\n:attr:`alpha` must be real numbers, otherwise they should be integers\n\nArgs:\n    beta (Number, optional): multiplier for :attr:`tensor` (:math:`\\beta`)\n    tensor (Tensor): vector to be added\n    alpha (Number, optional): multiplier for :math:`mat @ vec` (:math:`\\alpha`)\n    mat (Tensor): matrix to be multiplied\n    vec (Tensor): vector to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> M = torch.randn(2)\n    >>> mat = torch.randn(2, 3)\n    >>> vec = torch.randn(3)\n    >>> torch.addmv(M, mat, vec)\n    tensor([-0.3768, -5.5565])\n'
        pass
    
    @classmethod
    def addmv_(cls):
        pass
    
    @classmethod
    def addr(cls):
        '\naddr(beta=1, mat, alpha=1, vec1, vec2, out=None) -> Tensor\n\nPerforms the outer-product of vectors :attr:`vec1` and :attr:`vec2`\nand adds it to the matrix :attr:`mat`.\n\nOptional values :attr:`beta` and :attr:`alpha` are scaling factors on the\nouter product between :attr:`vec1` and :attr:`vec2` and the added matrix\n:attr:`mat` respectively.\n\n.. math::\n    \\text{out} = \\beta\\ \\text{mat} + \\alpha\\ (\\text{vec1} \\otimes \\text{vec2})\n\nIf :attr:`vec1` is a vector of size `n` and :attr:`vec2` is a vector\nof size `m`, then :attr:`mat` must be\n:ref:`broadcastable <broadcasting-semantics>` with a matrix of size\n:math:`(n \\times m)` and :attr:`out` will be a matrix of size\n:math:`(n \\times m)`.\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, arguments :attr:`beta` and\n:attr:`alpha` must be real numbers, otherwise they should be integers\n\nArgs:\n    beta (Number, optional): multiplier for :attr:`mat` (:math:`\\beta`)\n    mat (Tensor): matrix to be added\n    alpha (Number, optional): multiplier for :math:`\\text{vec1} \\otimes \\text{vec2}` (:math:`\\alpha`)\n    vec1 (Tensor): the first vector of the outer product\n    vec2 (Tensor): the second vector of the outer product\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> vec1 = torch.arange(1., 4.)\n    >>> vec2 = torch.arange(1., 3.)\n    >>> M = torch.zeros(3, 2)\n    >>> torch.addr(M, vec1, vec2)\n    tensor([[ 1.,  2.],\n            [ 2.,  4.],\n            [ 3.,  6.]])\n'
        pass
    
    @classmethod
    def affine_grid_generator(cls):
        pass
    
    @classmethod
    def all(cls):
        pass
    
    @classmethod
    def allclose(cls):
        "\nallclose(self, other, rtol=1e-05, atol=1e-08, equal_nan=False) -> bool\n\nThis function checks if all :attr:`self` and :attr:`other` satisfy the condition:\n\n.. math::\n    \\lvert \\text{self} - \\text{other} \\rvert \\leq \\texttt{atol} + \\texttt{rtol} \\times \\lvert \\text{other} \\rvert\n\nelementwise, for all elements of :attr:`self` and :attr:`other`. The behaviour of this function is analogous to\n`numpy.allclose <https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html>`_\n\nArgs:\n    self (Tensor): first tensor to compare\n    other (Tensor): second tensor to compare\n    atol (float, optional): absolute tolerance. Default: 1e-08\n    rtol (float, optional): relative tolerance. Default: 1e-05\n    equal_nan (float, optional): if ``True``, then two ``NaN`` s will be compared as equal. Default: ``False``\n\nExample::\n\n    >>> torch.allclose(torch.tensor([10000., 1e-07]), torch.tensor([10000.1, 1e-08]))\n    False\n    >>> torch.allclose(torch.tensor([10000., 1e-08]), torch.tensor([10000.1, 1e-09]))\n    True\n    >>> torch.allclose(torch.tensor([1.0, float('nan')]), torch.tensor([1.0, float('nan')]))\n    False\n    >>> torch.allclose(torch.tensor([1.0, float('nan')]), torch.tensor([1.0, float('nan')]), equal_nan=True)\n    True\n"
        pass
    
    @classmethod
    def alpha_dropout(cls):
        pass
    
    @classmethod
    def alpha_dropout_(cls):
        pass
    
    @classmethod
    def any(cls):
        pass
    
    @classmethod
    def arange(cls):
        '\narange(start=0, end, step=1, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a 1-D tensor of size :math:`\\left\\lfloor \\frac{\\text{end} - \\text{start}}{\\text{step}} \\right\\rfloor`\nwith values from the interval ``[start, end)`` taken with common difference\n:attr:`step` beginning from `start`.\n\nNote that non-integer :attr:`step` is subject to floating point rounding errors when\ncomparing against :attr:`end`; to avoid inconsistency, we advise adding a small epsilon to :attr:`end`\nin such cases.\n\n.. math::\n    \\text{out}_{{i+1}} = \\text{out}_{i} + \\text{step}\n\nArgs:\n    start (Number): the starting value for the set of points. Default: ``0``.\n    end (Number): the ending value for the set of points\n    step (Number): the gap between each pair of adjacent points. Default: ``1``.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`). If `dtype` is not given, infer the data type from the other input\n        arguments. If any of `start`, `end`, or `stop` are floating-point, the\n        `dtype` is inferred to be the default dtype, see\n        :meth:`~torch.get_default_dtype`. Otherwise, the `dtype` is inferred to\n        be `torch.int64`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.arange(5)\n    tensor([ 0,  1,  2,  3,  4])\n    >>> torch.arange(1, 4)\n    tensor([ 1,  2,  3])\n    >>> torch.arange(1, 2.5, 0.5)\n    tensor([ 1.0000,  1.5000,  2.0000])\n'
        pass
    
    @classmethod
    def argmax(cls):
        '\n.. function:: argmax(input) -> LongTensor\n\nReturns the indices of all elements in the :attr:`input` tensor.\n\nThis is the second value returned by :meth:`torch.max`. See its\ndocumentation for the exact semantics of this method.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 1.3398,  0.2663, -0.2686,  0.2450],\n            [-0.7401, -0.8805, -0.3402, -1.1936],\n            [ 0.4907, -1.3948, -1.0691, -0.3132],\n            [-1.6092,  0.5419, -0.2993,  0.3195]])\n    >>> torch.argmax(a)\n    tensor(0)\n\n.. function:: argmax(input, dim, keepdim=False) -> LongTensor\n\nReturns the indices of the maximum values of a tensor across a dimension.\n\nThis is the second value returned by :meth:`torch.max`. See its\ndocumentation for the exact semantics of this method.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce. If ``None``, the argmax of the\n        flattened input is returned.\n    keepdim (bool): whether the output tensors have :attr:`dim`\n        retained or not. Ignored if ``dim=None``.\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 1.3398,  0.2663, -0.2686,  0.2450],\n            [-0.7401, -0.8805, -0.3402, -1.1936],\n            [ 0.4907, -1.3948, -1.0691, -0.3132],\n            [-1.6092,  0.5419, -0.2993,  0.3195]])\n    >>> torch.argmax(a, dim=1)\n    tensor([ 0,  2,  0,  1])\n'
        pass
    
    @classmethod
    def argmin(cls):
        '\n.. function:: argmin(input) -> LongTensor\n\nReturns the indices of the minimum value of all elements in the :attr:`input` tensor.\n\nThis is the second value returned by :meth:`torch.min`. See its\ndocumentation for the exact semantics of this method.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 0.1139,  0.2254, -0.1381,  0.3687],\n            [ 1.0100, -1.1975, -0.0102, -0.4732],\n            [-0.9240,  0.1207, -0.7506, -1.0213],\n            [ 1.7809, -1.2960,  0.9384,  0.1438]])\n    >>> torch.argmin(a)\n    tensor(13)\n\n.. function:: argmin(input, dim, keepdim=False, out=None) -> LongTensor\n\nReturns the indices of the minimum values of a tensor across a dimension.\n\nThis is the second value returned by :meth:`torch.min`. See its\ndocumentation for the exact semantics of this method.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce. If ``None``, the argmin of the\n        flattened input is returned.\n    keepdim (bool): whether the output tensors have :attr:`dim`\n        retained or not. Ignored if ``dim=None``.\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 0.1139,  0.2254, -0.1381,  0.3687],\n            [ 1.0100, -1.1975, -0.0102, -0.4732],\n            [-0.9240,  0.1207, -0.7506, -1.0213],\n            [ 1.7809, -1.2960,  0.9384,  0.1438]])\n    >>> torch.argmin(a, dim=1)\n    tensor([ 2,  1,  3,  1])\n'
        pass
    
    @classmethod
    def argsort(cls):
        '\nargsort(input, dim=-1, descending=False, out=None) -> LongTensor\n\nReturns the indices that sort a tensor along a given dimension in ascending\norder by value.\n\nThis is the second value returned by :meth:`torch.sort`.  See its documentation\nfor the exact semantics of this method.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int, optional): the dimension to sort along\n    descending (bool, optional): controls the sorting order (ascending or descending)\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 0.0785,  1.5267, -0.8521,  0.4065],\n            [ 0.1598,  0.0788, -0.0745, -1.2700],\n            [ 1.2208,  1.0722, -0.7064,  1.2564],\n            [ 0.0669, -0.2318, -0.8229, -0.9280]])\n\n\n    >>> torch.argsort(a, dim=1)\n    tensor([[2, 0, 3, 1],\n            [3, 2, 1, 0],\n            [2, 1, 0, 3],\n            [3, 2, 1, 0]])\n'
        pass
    
    @classmethod
    def as_strided(cls):
        pass
    
    @classmethod
    def as_strided_(cls):
        pass
    
    @classmethod
    def as_tensor(cls):
        "\nas_tensor(data, dtype=None, device=None) -> Tensor\n\nConvert the data into a `torch.Tensor`. If the data is already a `Tensor` with the same `dtype` and `device`,\nno copy will be performed, otherwise a new `Tensor` will be returned with computational graph retained if data\n`Tensor` has ``requires_grad=True``. Similarly, if the data is an ``ndarray`` of the corresponding `dtype` and\nthe `device` is the cpu, no copy will be performed.\n\nArgs:\n    data (array_like): Initial data for the tensor. Can be a list, tuple,\n        NumPy ``ndarray``, scalar, and other types.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, infers data type from :attr:`data`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n\nExample::\n\n    >>> a = numpy.array([1, 2, 3])\n    >>> t = torch.as_tensor(a)\n    >>> t\n    tensor([ 1,  2,  3])\n    >>> t[0] = -1\n    >>> a\n    array([-1,  2,  3])\n\n    >>> a = numpy.array([1, 2, 3])\n    >>> t = torch.as_tensor(a, device=torch.device('cuda'))\n    >>> t\n    tensor([ 1,  2,  3])\n    >>> t[0] = -1\n    >>> a\n    array([1,  2,  3])\n"
        pass
    
    @classmethod
    def asin(cls):
        '\nasin(input, out=None) -> Tensor\n\nReturns a new tensor with the arcsine  of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\sin^{-1}(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.5962,  1.4985, -0.4396,  1.4525])\n    >>> torch.asin(a)\n    tensor([-0.6387,     nan, -0.4552,     nan])\n'
        pass
    
    @classmethod
    def asin_(cls):
        pass
    
    @classmethod
    def atan(cls):
        '\natan(input, out=None) -> Tensor\n\nReturns a new tensor with the arctangent  of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\tan^{-1}(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.2341,  0.2539, -0.6256, -0.6448])\n    >>> torch.atan(a)\n    tensor([ 0.2299,  0.2487, -0.5591, -0.5727])\n'
        pass
    
    @classmethod
    def atan2(cls):
        '\natan2(input1, input2, out=None) -> Tensor\n\nReturns a new tensor with the arctangent of the elements of :attr:`input1`\nand :attr:`input2`.\n\nThe shapes of :attr:`input1` and :attr:`input2` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\nArgs:\n    input1 (Tensor): the first input tensor\n    input2 (Tensor): the second input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.9041,  0.0196, -0.3108, -2.4423])\n    >>> torch.atan2(a, torch.randn(4))\n    tensor([ 0.9833,  0.0811, -1.9743, -1.4151])\n'
        pass
    
    @classmethod
    def atan_(cls):
        pass
    
    @classmethod
    def avg_pool1d(cls):
        '\navg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True) -> Tensor\n\nApplies a 1D average pooling over an input signal composed of several\ninput planes.\n\nSee :class:`~torch.nn.AvgPool1d` for details and output shape.\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iW)`\n    kernel_size: the size of the window. Can be a single number or a\n      tuple `(kW,)`\n    stride: the stride of the window. Can be a single number or a tuple\n      `(sW,)`. Default: :attr:`kernel_size`\n    padding: implicit zero paddings on both sides of the input. Can be a\n      single number or a tuple `(padW,)`. Default: 0\n    ceil_mode: when True, will use `ceil` instead of `floor` to compute the\n        output shape. Default: ``False``\n    count_include_pad: when True, will include the zero-padding in the\n        averaging calculation. Default: ``True``\n\nExamples::\n\n    >>> # pool of square window of size=3, stride=2\n    >>> input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7]]], dtype=torch.float32)\n    >>> F.avg_pool1d(input, kernel_size=3, stride=2)\n    tensor([[[ 2.,  4.,  6.]]])\n\n'
        pass
    
    @classmethod
    def baddbmm(cls):
        '\nbaddbmm(beta=1, mat, alpha=1, batch1, batch2, out=None) -> Tensor\n\nPerforms a batch matrix-matrix product of matrices in :attr:`batch1`\nand :attr:`batch2`.\n:attr:`mat` is added to the final result.\n\n:attr:`batch1` and :attr:`batch2` must be 3-D tensors each containing the same\nnumber of matrices.\n\nIf :attr:`batch1` is a :math:`(b \\times n \\times m)` tensor, :attr:`batch2` is a\n:math:`(b \\times m \\times p)` tensor, then :attr:`mat` must be\n:ref:`broadcastable <broadcasting-semantics>` with a\n:math:`(b \\times n \\times p)` tensor and :attr:`out` will be a\n:math:`(b \\times n \\times p)` tensor. Both :attr:`alpha` and :attr:`beta` mean the\nsame as the scaling factors used in :meth:`torch.addbmm`.\n\n.. math::\n    \\text{out}_i = \\beta\\ \\text{mat}_i + \\alpha\\ (\\text{batch1}_i \\mathbin{@} \\text{batch2}_i)\n\nFor inputs of type `FloatTensor` or `DoubleTensor`, arguments :attr:`beta` and\n:attr:`alpha` must be real numbers, otherwise they should be integers.\n\nArgs:\n    beta (Number, optional): multiplier for :attr:`mat` (:math:`\\beta`)\n    mat (Tensor): the tensor to be added\n    alpha (Number, optional): multiplier for :math:`\\text{batch1} \\mathbin{@} \\text{batch2}` (:math:`\\alpha`)\n    batch1 (Tensor): the first batch of matrices to be multiplied\n    batch2 (Tensor): the second batch of matrices to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> M = torch.randn(10, 3, 5)\n    >>> batch1 = torch.randn(10, 3, 4)\n    >>> batch2 = torch.randn(10, 4, 5)\n    >>> torch.baddbmm(M, batch1, batch2).size()\n    torch.Size([10, 3, 5])\n'
        pass
    
    @classmethod
    def bartlett_window(cls):
        '\nbartlett_window(window_length, periodic=True, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nBartlett window function.\n\n.. math::\n    w[n] = 1 - \\left| \\frac{2n}{N-1} - 1 \\right| = \\begin{cases}\n        \\frac{2n}{N - 1} & \\text{if } 0 \\leq n \\leq \\frac{N - 1}{2} \\\\\n        2 - \\frac{2n}{N - 1} & \\text{if } \\frac{N - 1}{2} < n < N \\\\\n    \\end{cases},\n\nwhere :math:`N` is the full window size.\n\nThe input :attr:`window_length` is a positive integer controlling the\nreturned window size. :attr:`periodic` flag determines whether the returned\nwindow trims off the last duplicate value from the symmetric window and is\nready to be used as a periodic window with functions like\n:meth:`torch.stft`. Therefore, if :attr:`periodic` is true, the :math:`N` in\nabove formula is in fact :math:`\\text{window\\_length} + 1`. Also, we always have\n``torch.bartlett_window(L, periodic=True)`` equal to\n``torch.bartlett_window(L + 1, periodic=False)[:-1])``.\n\n.. note::\n    If :attr:`window_length` :math:`=1`, the returned window contains a single value 1.\n\nArguments:\n    window_length (int): the size of returned window\n    periodic (bool, optional): If True, returns a window to be used as periodic\n        function. If False, return a symmetric window.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`). Only floating point types are supported.\n    layout (:class:`torch.layout`, optional): the desired layout of returned window tensor. Only\n          ``torch.strided`` (dense layout) is supported.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nReturns:\n    Tensor: A 1-D tensor of size :math:`(\\text{window\\_length},)` containing the window\n\n'
        pass
    
    @classmethod
    def batch_norm(cls):
        pass
    
    @classmethod
    def batch_norm_backward_elemt(cls):
        pass
    
    @classmethod
    def batch_norm_backward_reduce(cls):
        pass
    
    @classmethod
    def batch_norm_elemt(cls):
        pass
    
    @classmethod
    def batch_norm_gather_stats(cls):
        pass
    
    @classmethod
    def batch_norm_stats(cls):
        pass
    
    @classmethod
    def batch_norm_update_stats(cls):
        pass
    
    @classmethod
    def bernoulli(cls):
        '\nbernoulli(input, *, generator=None, out=None) -> Tensor\n\nDraws binary random numbers (0 or 1) from a Bernoulli distribution.\n\nThe :attr:`input` tensor should be a tensor containing probabilities\nto be used for drawing the binary random number.\nHence, all values in :attr:`input` have to be in the range:\n:math:`0 \\leq \\text{input}_i \\leq 1`.\n\nThe :math:`\\text{i}^{th}` element of the output tensor will draw a\nvalue :math:`1` according to the :math:`\\text{i}^{th}` probability value given\nin :attr:`input`.\n\n.. math::\n    \\text{out}_{i} \\sim \\mathrm{Bernoulli}(p = \\text{input}_{i})\n\nThe returned :attr:`out` tensor only has values 0 or 1 and is of the same\nshape as :attr:`input`.\n\n:attr:`out` can have integral ``dtype``, but :attr:`input` must have floating\npoint ``dtype``.\n\nArgs:\n    input (Tensor): the input tensor of probability values for the Bernoulli distribution\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.empty(3, 3).uniform_(0, 1)  # generate a uniform random matrix with range [0, 1]\n    >>> a\n    tensor([[ 0.1737,  0.0950,  0.3609],\n            [ 0.7148,  0.0289,  0.2676],\n            [ 0.9456,  0.8937,  0.7202]])\n    >>> torch.bernoulli(a)\n    tensor([[ 1.,  0.,  0.],\n            [ 0.,  0.,  0.],\n            [ 1.,  1.,  1.]])\n\n    >>> a = torch.ones(3, 3) # probability of drawing "1" is 1\n    >>> torch.bernoulli(a)\n    tensor([[ 1.,  1.,  1.],\n            [ 1.,  1.,  1.],\n            [ 1.,  1.,  1.]])\n    >>> a = torch.zeros(3, 3) # probability of drawing "1" is 0\n    >>> torch.bernoulli(a)\n    tensor([[ 0.,  0.,  0.],\n            [ 0.,  0.,  0.],\n            [ 0.,  0.,  0.]])\n'
        pass
    
    @classmethod
    def bilinear(cls):
        pass
    
    @classmethod
    def binary_cross_entropy_with_logits(cls):
        pass
    
    @classmethod
    def bincount(cls):
        '\nbincount(self, weights=None, minlength=0) -> Tensor\n\nCount the frequency of each value in an array of non-negative ints.\n\nThe number of bins (size 1) is one larger than the largest value in\n:attr:`input` unless :attr:`input` is empty, in which case the result is a\ntensor of size 0. If :attr:`minlength` is specified, the number of bins is at least\n:attr:`minlength` and if :attr:`input` is empty, then the result is tensor of size\n:attr:`minlength` filled with zeros. If ``n`` is the value at position ``i``,\n``out[n] += weights[i]`` if :attr:`weights` is specified else\n``out[n] += 1``.\n\n.. include:: cuda_deterministic.rst\n\nArguments:\n    input (Tensor): 1-d int tensor\n    weights (Tensor): optional, weight for each value in the input tensor.\n        Should be of same size as input tensor.\n    minlength (int): optional, minimum number of bins. Should be non-negative.\n\nReturns:\n    output (Tensor): a tensor of shape ``Size([max(input) + 1])`` if\n    :attr:`input` is non-empty, else ``Size(0)``\n\nExample::\n\n    >>> input = torch.randint(0, 8, (5,), dtype=torch.int64)\n    >>> weights = torch.linspace(0, 1, steps=5)\n    >>> input, weights\n    (tensor([4, 3, 6, 3, 4]),\n     tensor([ 0.0000,  0.2500,  0.5000,  0.7500,  1.0000])\n\n    >>> torch.bincount(input)\n    tensor([0, 0, 0, 2, 2, 0, 1])\n\n    >>> input.bincount(weights)\n    tensor([0.0000, 0.0000, 0.0000, 1.0000, 1.0000, 0.0000, 0.5000])\n'
        pass
    
    @classmethod
    def blackman_window(cls):
        '\nblackman_window(window_length, periodic=True, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nBlackman window function.\n\n.. math::\n    w[n] = 0.42 - 0.5 \\cos \\left( \\frac{2 \\pi n}{N - 1} \\right) + 0.08 \\cos \\left( \\frac{4 \\pi n}{N - 1} \\right)\n\nwhere :math:`N` is the full window size.\n\nThe input :attr:`window_length` is a positive integer controlling the\nreturned window size. :attr:`periodic` flag determines whether the returned\nwindow trims off the last duplicate value from the symmetric window and is\nready to be used as a periodic window with functions like\n:meth:`torch.stft`. Therefore, if :attr:`periodic` is true, the :math:`N` in\nabove formula is in fact :math:`\\text{window\\_length} + 1`. Also, we always have\n``torch.blackman_window(L, periodic=True)`` equal to\n``torch.blackman_window(L + 1, periodic=False)[:-1])``.\n\n.. note::\n    If :attr:`window_length` :math:`=1`, the returned window contains a single value 1.\n\nArguments:\n    window_length (int): the size of returned window\n    periodic (bool, optional): If True, returns a window to be used as periodic\n        function. If False, return a symmetric window.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`). Only floating point types are supported.\n    layout (:class:`torch.layout`, optional): the desired layout of returned window tensor. Only\n          ``torch.strided`` (dense layout) is supported.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nReturns:\n    Tensor: A 1-D tensor of size :math:`(\\text{window\\_length},)` containing the window\n\n'
        pass
    
    @classmethod
    def bmm(cls):
        '\nbmm(batch1, batch2, out=None) -> Tensor\n\nPerforms a batch matrix-matrix product of matrices stored in :attr:`batch1`\nand :attr:`batch2`.\n\n:attr:`batch1` and :attr:`batch2` must be 3-D tensors each containing\nthe same number of matrices.\n\nIf :attr:`batch1` is a :math:`(b \\times n \\times m)` tensor, :attr:`batch2` is a\n:math:`(b \\times m \\times p)` tensor, :attr:`out` will be a\n:math:`(b \\times n \\times p)` tensor.\n\n.. math::\n    \\text{out}_i = \\text{batch1}_i \\mathbin{@} \\text{batch2}_i\n\n.. note:: This function does not :ref:`broadcast <broadcasting-semantics>`.\n          For broadcasting matrix products, see :func:`torch.matmul`.\n\nArgs:\n    batch1 (Tensor): the first batch of matrices to be multiplied\n    batch2 (Tensor): the second batch of matrices to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> batch1 = torch.randn(10, 3, 4)\n    >>> batch2 = torch.randn(10, 4, 5)\n    >>> res = torch.bmm(batch1, batch2)\n    >>> res.size()\n    torch.Size([10, 3, 5])\n'
        pass
    
    @classmethod
    def broadcast_tensors(cls):
        pass
    
    @classmethod
    def cartesian_prod(cls):
        pass
    
    @classmethod
    def cat(cls):
        '\ncat(tensors, dim=0, out=None) -> Tensor\n\nConcatenates the given sequence of :attr:`seq` tensors in the given dimension.\nAll tensors must either have the same shape (except in the concatenating\ndimension) or be empty.\n\n:func:`torch.cat` can be seen as an inverse operation for :func:`torch.split`\nand :func:`torch.chunk`.\n\n:func:`torch.cat` can be best understood via examples.\n\nArgs:\n    tensors (sequence of Tensors): any python sequence of tensors of the same type.\n        Non-empty tensors provided must have the same shape, except in the\n        cat dimension.\n    dim (int, optional): the dimension over which the tensors are concatenated\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> x = torch.randn(2, 3)\n    >>> x\n    tensor([[ 0.6580, -1.0969, -0.4614],\n            [-0.1034, -0.5790,  0.1497]])\n    >>> torch.cat((x, x, x), 0)\n    tensor([[ 0.6580, -1.0969, -0.4614],\n            [-0.1034, -0.5790,  0.1497],\n            [ 0.6580, -1.0969, -0.4614],\n            [-0.1034, -0.5790,  0.1497],\n            [ 0.6580, -1.0969, -0.4614],\n            [-0.1034, -0.5790,  0.1497]])\n    >>> torch.cat((x, x, x), 1)\n    tensor([[ 0.6580, -1.0969, -0.4614,  0.6580, -1.0969, -0.4614,  0.6580,\n             -1.0969, -0.4614],\n            [-0.1034, -0.5790,  0.1497, -0.1034, -0.5790,  0.1497, -0.1034,\n             -0.5790,  0.1497]])\n'
        pass
    
    @classmethod
    def cdist(cls):
        pass
    
    @classmethod
    def ceil(cls):
        '\nceil(input, out=None) -> Tensor\n\nReturns a new tensor with the ceil of the elements of :attr:`input`,\nthe smallest integer greater than or equal to each element.\n\n.. math::\n    \\text{out}_{i} = \\left\\lceil \\text{input}_{i} \\right\\rceil = \\left\\lfloor \\text{input}_{i} \\right\\rfloor + 1\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.6341, -1.4208, -1.0900,  0.5826])\n    >>> torch.ceil(a)\n    tensor([-0., -1., -1.,  1.])\n'
        pass
    
    @classmethod
    def ceil_(cls):
        pass
    
    @classmethod
    def celu(cls):
        pass
    
    @classmethod
    def celu_(cls):
        '\ncelu_(input, alpha=1.) -> Tensor\n\nIn-place version of :func:`~celu`.\n'
        pass
    
    @classmethod
    def chain_matmul(cls):
        pass
    
    @classmethod
    def cholesky(cls):
        '\ncholesky(A, upper=False, out=None) -> Tensor\n\nComputes the Cholesky decomposition of a symmetric positive-definite\nmatrix :math:`A` or for batches of symmetric positive-definite matrices.\n\nIf :attr:`upper` is ``True``, the returned matrix ``U`` is upper-triangular, and\nthe decomposition has the form:\n\n.. math::\n\n  A = U^TU\n\nIf :attr:`upper` is ``False``, the returned matrix ``L`` is lower-triangular, and\nthe decomposition has the form:\n\n.. math::\n\n    A = LL^T\n\nIf :attr:`upper` is ``True``, and :attr:`A` is a batch of symmetric positive-definite\nmatrices, then the returned tensor will be composed of upper-triangular Cholesky factors\nof each of the individual matrices. Similarly, when :attr:`upper` is ``False``, the returned\ntensor will be composed of lower-triangular Cholesky factors of each of the individual\nmatrices.\n\nArgs:\n    a (Tensor): the input tensor of size (*, n, n) where `*` is zero or more\n                batch dimensions consisting of symmetric positive-definite matrices.\n    upper (bool, optional): flag that indicates whether to return a\n                            upper or lower triangular matrix. Default: ``False``\n    out (Tensor, optional): the output matrix\n\nExample::\n\n    >>> a = torch.randn(3, 3)\n    >>> a = torch.mm(a, a.t()) # make symmetric positive-definite\n    >>> l = torch.cholesky(a)\n    >>> a\n    tensor([[ 2.4112, -0.7486,  1.4551],\n            [-0.7486,  1.3544,  0.1294],\n            [ 1.4551,  0.1294,  1.6724]])\n    >>> l\n    tensor([[ 1.5528,  0.0000,  0.0000],\n            [-0.4821,  1.0592,  0.0000],\n            [ 0.9371,  0.5487,  0.7023]])\n    >>> torch.mm(l, l.t())\n    tensor([[ 2.4112, -0.7486,  1.4551],\n            [-0.7486,  1.3544,  0.1294],\n            [ 1.4551,  0.1294,  1.6724]])\n    >>> a = torch.randn(3, 2, 2)\n    >>> a = torch.matmul(a, a.transpose(-1, -2)) + 1e-03 # make symmetric positive-definite\n    >>> l = torch.cholesky(a)\n    >>> z = torch.matmul(l, l.transpose(-1, -2))\n    >>> torch.max(torch.abs(z - a)) # Max non-zero\n    tensor(2.3842e-07)\n'
        pass
    
    @classmethod
    def cholesky_inverse(cls):
        '\ncholesky_inverse(u, upper=False, out=None) -> Tensor\n\nComputes the inverse of a symmetric positive-definite matrix :math:`A` using its\nCholesky factor :attr:`u`: returns matrix ``inv``. The inverse is computed using\nLAPACK routines ``dpotri`` and ``spotri`` (and the corresponding MAGMA routines).\n\nIf :attr:`upper` is ``False``, :attr:`u` is lower triangular\nsuch that the returned tensor is\n\n.. math::\n    inv = (uu^{T})^{-1}\n\nIf :attr:`upper` is ``True`` or not provided, :attr:`u` is upper\ntriangular such that the returned tensor is\n\n.. math::\n    inv = (u^T u)^{-1}\n\nArgs:\n    u (Tensor): the input 2-D tensor, a upper or lower triangular\n           Cholesky factor\n    upper (bool, optional): whether to return a lower (default) or upper triangular matrix\n    out (Tensor, optional): the output tensor for `inv`\n\nExample::\n\n    >>> a = torch.randn(3, 3)\n    >>> a = torch.mm(a, a.t()) + 1e-05 * torch.eye(3) # make symmetric positive definite\n    >>> u = torch.cholesky(a)\n    >>> a\n    tensor([[  0.9935,  -0.6353,   1.5806],\n            [ -0.6353,   0.8769,  -1.7183],\n            [  1.5806,  -1.7183,  10.6618]])\n    >>> torch.cholesky_inverse(u)\n    tensor([[ 1.9314,  1.2251, -0.0889],\n            [ 1.2251,  2.4439,  0.2122],\n            [-0.0889,  0.2122,  0.1412]])\n    >>> a.inverse()\n    tensor([[ 1.9314,  1.2251, -0.0889],\n            [ 1.2251,  2.4439,  0.2122],\n            [-0.0889,  0.2122,  0.1412]])\n'
        pass
    
    @classmethod
    def cholesky_solve(cls):
        '\ncholesky_solve(b, u, upper=False, out=None) -> Tensor\n\nSolves a linear system of equations with a positive semidefinite\nmatrix to be inverted given its Cholesky factor matrix :attr:`u`.\n\nIf :attr:`upper` is ``False``, :attr:`u` is and lower triangular and `c` is\nreturned such that:\n\n.. math::\n    c = (u u^T)^{-1} b\n\nIf :attr:`upper` is ``True`` or not provided, :attr:`u` is upper triangular\nand `c` is returned such that:\n\n.. math::\n    c = (u^T u)^{-1} b\n\n`torch.cholesky_solve(b, u)` can take in 2D inputs `b, u` or inputs that are\nbatches of 2D matrices. If the inputs are batches, then returns\nbatched outputs `c`\n\n.. note::\n\n    The :attr:`out` keyword only supports 2D matrix inputs, that is,\n    `b, u` must be 2D matrices.\n\nArgs:\n    b (Tensor): input matrix of size :math:`(*, m, k)`,\n                where :math:`*` is zero or more batch dimensions\n    u (Tensor): input matrix of size :math:`(*, m, m)`,\n                where :math:`*` is zero of more batch dimensions composed of\n                upper or lower triangular Cholesky factor\n    upper (bool, optional): whether to consider the Cholesky factor as a\n                            lower or upper triangular matrix. Default: ``False``.\n    out (Tensor, optional): the output tensor for `c`\n\nExample::\n\n    >>> a = torch.randn(3, 3)\n    >>> a = torch.mm(a, a.t()) # make symmetric positive definite\n    >>> u = torch.cholesky(a)\n    >>> a\n    tensor([[ 0.7747, -1.9549,  1.3086],\n            [-1.9549,  6.7546, -5.4114],\n            [ 1.3086, -5.4114,  4.8733]])\n    >>> b = torch.randn(3, 2)\n    >>> b\n    tensor([[-0.6355,  0.9891],\n            [ 0.1974,  1.4706],\n            [-0.4115, -0.6225]])\n    >>> torch.cholesky_solve(b, u)\n    tensor([[ -8.1625,  19.6097],\n            [ -5.8398,  14.2387],\n            [ -4.3771,  10.4173]])\n    >>> torch.mm(a.inverse(), b)\n    tensor([[ -8.1626,  19.6097],\n            [ -5.8398,  14.2387],\n            [ -4.3771,  10.4173]])\n'
        pass
    
    @classmethod
    def chunk(cls):
        '\nchunk(tensor, chunks, dim=0) -> List of Tensors\n\nSplits a tensor into a specific number of chunks.\n\nLast chunk will be smaller if the tensor size along the given dimension\n:attr:`dim` is not divisible by :attr:`chunks`.\n\nArguments:\n    tensor (Tensor): the tensor to split\n    chunks (int): number of chunks to return\n    dim (int): dimension along which to split the tensor\n'
        pass
    
    @classmethod
    def clamp(cls):
        '\nclamp(input, min, max, out=None) -> Tensor\n\nClamp all elements in :attr:`input` into the range `[` :attr:`min`, :attr:`max` `]` and return\na resulting tensor:\n\n.. math::\n    y_i = \\begin{cases}\n        \\text{min} & \\text{if } x_i < \\text{min} \\\\\n        x_i & \\text{if } \\text{min} \\leq x_i \\leq \\text{max} \\\\\n        \\text{max} & \\text{if } x_i > \\text{max}\n    \\end{cases}\n\nIf :attr:`input` is of type `FloatTensor` or `DoubleTensor`, args :attr:`min`\nand :attr:`max` must be real numbers, otherwise they should be integers.\n\nArgs:\n    input (Tensor): the input tensor\n    min (Number): lower-bound of the range to be clamped to\n    max (Number): upper-bound of the range to be clamped to\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-1.7120,  0.1734, -0.0478, -0.0922])\n    >>> torch.clamp(a, min=-0.5, max=0.5)\n    tensor([-0.5000,  0.1734, -0.0478, -0.0922])\n\n.. function:: clamp(input, *, min, out=None) -> Tensor\n\nClamps all elements in :attr:`input` to be larger or equal :attr:`min`.\n\nIf :attr:`input` is of type `FloatTensor` or `DoubleTensor`, :attr:`value`\nshould be a real number, otherwise it should be an integer.\n\nArgs:\n    input (Tensor): the input tensor\n    value (Number): minimal value of each element in the output\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.0299, -2.3184,  2.1593, -0.8883])\n    >>> torch.clamp(a, min=0.5)\n    tensor([ 0.5000,  0.5000,  2.1593,  0.5000])\n\n.. function:: clamp(input, *, max, out=None) -> Tensor\n\nClamps all elements in :attr:`input` to be smaller or equal :attr:`max`.\n\nIf :attr:`input` is of type `FloatTensor` or `DoubleTensor`, :attr:`value`\nshould be a real number, otherwise it should be an integer.\n\nArgs:\n    input (Tensor): the input tensor\n    value (Number): maximal value of each element in the output\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.7753, -0.4702, -0.4599,  1.1899])\n    >>> torch.clamp(a, max=0.5)\n    tensor([ 0.5000, -0.4702, -0.4599,  0.5000])\n'
        pass
    
    @classmethod
    def clamp_(cls):
        pass
    
    @classmethod
    def clamp_max(cls):
        pass
    
    @classmethod
    def clamp_max_(cls):
        pass
    
    @classmethod
    def clamp_min(cls):
        pass
    
    @classmethod
    def clamp_min_(cls):
        pass
    
    @classmethod
    def clone(cls):
        pass
    
    @classmethod
    def combinations(cls):
        "\ncombinations(tensor, r=2, with_replacement=False) -> seq\n\nCompute combinations of length :math:`r` of the given tensor. The behavior is similar to\npython's `itertools.combinations` when `with_replacement` is set to `False`, and\n`itertools.combinations_with_replacement` when `with_replacement` is set to `True`.\n\nArguments:\n    tensor (Tensor): 1D vector.\n    r (int, optional): number of elements to combine\n    with_replacement (boolean, optional): whether to allow duplication in combination\n\nReturns:\n    Tensor: A tensor equivalent to converting all the input tensors into lists, do\n    `itertools.combinations` or `itertools.combinations_with_replacement` on these\n    lists, and finally convert the resulting list into tensor.\n\nExample::\n\n    >>> a = [1, 2, 3]\n    >>> list(itertools.combinations(a, r=2))\n    [(1, 2), (1, 3), (2, 3)]\n    >>> list(itertools.combinations(a, r=3))\n    [(1, 2, 3)]\n    >>> list(itertools.combinations_with_replacement(a, r=2))\n    [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]\n    >>> tensor_a = torch.tensor(a)\n    >>> torch.combinations(tensor_a)\n    tensor([[1, 2],\n            [1, 3],\n            [2, 3]])\n    >>> torch.combinations(tensor_a, r=3)\n    tensor([[1, 2, 3]])\n    >>> torch.combinations(tensor_a, with_replacement=True)\n    tensor([[1, 1],\n            [1, 2],\n            [1, 3],\n            [2, 2],\n            [2, 3],\n            [3, 3]])\n"
        pass
    
    @classmethod
    def constant_pad_nd(cls):
        pass
    
    @classmethod
    def conv1d(cls):
        "\nconv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1, padding_mode='zeros') -> Tensor\n\nApplies a 1D convolution over an input signal composed of several input\nplanes.\n\nSee :class:`~torch.nn.Conv1d` for details and output shape.\n\n.. include:: cudnn_deterministic.rst\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iW)`\n    weight: filters of shape :math:`(\\text{out\\_channels} , \\frac{\\text{in\\_channels}}{\\text{groups}} , kW)`\n    bias: optional bias of shape :math:`(\\text{out\\_channels})`. Default: ``None``\n    stride: the stride of the convolving kernel. Can be a single number or\n      a one-element tuple `(sW,)`. Default: 1\n    padding: implicit paddings on both sides of the input. Can be a\n      single number or a one-element tuple `(padW,)`. Default: 0\n    dilation: the spacing between kernel elements. Can be a single number or\n      a one-element tuple `(dW,)`. Default: 1\n    groups: split input into groups, :math:`\\text{in\\_channels}` should be divisible by\n      the number of groups. Default: 1\n    padding_mode: the type of paddings applied to both sided can be: `zeros` or `circular`. Default: `zeros`\n\nExamples::\n\n    >>> filters = torch.randn(33, 16, 3)\n    >>> inputs = torch.randn(20, 16, 50)\n    >>> F.conv1d(inputs, filters)\n"
        pass
    
    @classmethod
    def conv2d(cls):
        "\nconv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1, padding_mode='zeros') -> Tensor\n\nApplies a 2D convolution over an input image composed of several input\nplanes.\n\nSee :class:`~torch.nn.Conv2d` for details and output shape.\n\n.. include:: cudnn_deterministic.rst\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iH , iW)`\n    weight: filters of shape :math:`(\\text{out\\_channels} , \\frac{\\text{in\\_channels}}{\\text{groups}} , kH , kW)`\n    bias: optional bias tensor of shape :math:`(\\text{out\\_channels})`. Default: ``None``\n    stride: the stride of the convolving kernel. Can be a single number or a\n      tuple `(sH, sW)`. Default: 1\n    padding: implicit paddings on both sides of the input. Can be a\n      single number or a tuple `(padH, padW)`. Default: 0\n    dilation: the spacing between kernel elements. Can be a single number or\n      a tuple `(dH, dW)`. Default: 1\n    groups: split input into groups, :math:`\\text{in\\_channels}` should be divisible by the\n      number of groups. Default: 1\n    padding_mode: the type of paddings applied to both sided can be: `zeros` or `circular`. Default: `zeros`\n\nExamples::\n\n    >>> # With square kernels and equal stride\n    >>> filters = torch.randn(8,4,3,3)\n    >>> inputs = torch.randn(1,4,5,5)\n    >>> F.conv2d(inputs, filters, padding=1)\n"
        pass
    
    @classmethod
    def conv3d(cls):
        "\nconv3d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1, padding_mode='zeros') -> Tensor\n\nApplies a 3D convolution over an input image composed of several input\nplanes.\n\nSee :class:`~torch.nn.Conv3d` for details and output shape.\n\n.. include:: cudnn_deterministic.rst\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iT , iH , iW)`\n    weight: filters of shape :math:`(\\text{out\\_channels} , \\frac{\\text{in\\_channels}}{\\text{groups}} , kT , kH , kW)`\n    bias: optional bias tensor of shape :math:`(\\text{out\\_channels})`. Default: None\n    stride: the stride of the convolving kernel. Can be a single number or a\n      tuple `(sT, sH, sW)`. Default: 1\n    padding: implicit paddings on both sides of the input. Can be a\n      single number or a tuple `(padT, padH, padW)`. Default: 0\n    dilation: the spacing between kernel elements. Can be a single number or\n      a tuple `(dT, dH, dW)`. Default: 1\n    groups: split input into groups, :math:`\\text{in\\_channels}` should be divisible by\n      the number of groups. Default: 1\n    padding_mode: the type of paddings applied to both sided can be: `zeros` or `circular`. Default: `zeros`\n\nExamples::\n\n    >>> filters = torch.randn(33, 16, 3, 3, 3)\n    >>> inputs = torch.randn(20, 16, 50, 10, 20)\n    >>> F.conv3d(inputs, filters)\n"
        pass
    
    @classmethod
    def conv_tbc(cls):
        '\nApplies a 1-dimensional sequence convolution over an input sequence.\nInput and output dimensions are (Time, Batch, Channels) - hence TBC.\n\nArgs:\n    input: input tensor of shape :math:`(\\text{sequence length} \\times batch \\times \\text{in\\_channels})`\n    weight: filter of shape (:math:`\\text{kernel width} \\times \\text{in\\_channels} \\times \\text{out\\_channels}`)\n    bias: bias of shape (:math:`\\text{out\\_channels}`)\n    pad: number of timesteps to pad. Default: 0\n'
        pass
    
    @classmethod
    def conv_transpose1d(cls):
        '\nconv_transpose1d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1) -> Tensor\n\nApplies a 1D transposed convolution operator over an input signal\ncomposed of several input planes, sometimes also called "deconvolution".\n\nSee :class:`~torch.nn.ConvTranspose1d` for details and output shape.\n\n.. include:: cudnn_deterministic.rst\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iW)`\n    weight: filters of shape :math:`(\\text{in\\_channels} , \\frac{\\text{out\\_channels}}{\\text{groups}} , kW)`\n    bias: optional bias of shape :math:`(\\text{out\\_channels})`. Default: None\n    stride: the stride of the convolving kernel. Can be a single number or a\n      tuple ``(sW,)``. Default: 1\n    padding: ``dilation * (kernel_size - 1) - padding`` zero-padding will be added to both\n      sides of each dimension in the input. Can be a single number or a tuple\n      ``(padW,)``. Default: 0\n    output_padding: additional size added to one side of each dimension in the\n      output shape. Can be a single number or a tuple ``(out_padW)``. Default: 0\n    groups: split input into groups, :math:`\\text{in\\_channels}` should be divisible by the\n      number of groups. Default: 1\n    dilation: the spacing between kernel elements. Can be a single number or\n      a tuple ``(dW,)``. Default: 1\n\nExamples::\n\n    >>> inputs = torch.randn(20, 16, 50)\n    >>> weights = torch.randn(16, 33, 5)\n    >>> F.conv_transpose1d(inputs, weights)\n'
        pass
    
    @classmethod
    def conv_transpose2d(cls):
        '\nconv_transpose2d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1) -> Tensor\n\nApplies a 2D transposed convolution operator over an input image\ncomposed of several input planes, sometimes also called "deconvolution".\n\nSee :class:`~torch.nn.ConvTranspose2d` for details and output shape.\n\n.. include:: cudnn_deterministic.rst\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iH , iW)`\n    weight: filters of shape :math:`(\\text{in\\_channels} , \\frac{\\text{out\\_channels}}{\\text{groups}} , kH , kW)`\n    bias: optional bias of shape :math:`(\\text{out\\_channels})`. Default: None\n    stride: the stride of the convolving kernel. Can be a single number or a\n      tuple ``(sH, sW)``. Default: 1\n    padding: ``dilation * (kernel_size - 1) - padding`` zero-padding will be added to both\n      sides of each dimension in the input. Can be a single number or a tuple\n      ``(padH, padW)``. Default: 0\n    output_padding: additional size added to one side of each dimension in the\n      output shape. Can be a single number or a tuple ``(out_padH, out_padW)``.\n      Default: 0\n    groups: split input into groups, :math:`\\text{in\\_channels}` should be divisible by the\n      number of groups. Default: 1\n    dilation: the spacing between kernel elements. Can be a single number or\n      a tuple ``(dH, dW)``. Default: 1\n\nExamples::\n\n    >>> # With square kernels and equal stride\n    >>> inputs = torch.randn(1, 4, 5, 5)\n    >>> weights = torch.randn(4, 8, 3, 3)\n    >>> F.conv_transpose2d(inputs, weights, padding=1)\n'
        pass
    
    @classmethod
    def conv_transpose3d(cls):
        '\nconv_transpose3d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1) -> Tensor\n\nApplies a 3D transposed convolution operator over an input image\ncomposed of several input planes, sometimes also called "deconvolution"\n\nSee :class:`~torch.nn.ConvTranspose3d` for details and output shape.\n\n.. include:: cudnn_deterministic.rst\n\nArgs:\n    input: input tensor of shape :math:`(\\text{minibatch} , \\text{in\\_channels} , iT , iH , iW)`\n    weight: filters of shape :math:`(\\text{in\\_channels} , \\frac{\\text{out\\_channels}}{\\text{groups}} , kT , kH , kW)`\n    bias: optional bias of shape :math:`(\\text{out\\_channels})`. Default: None\n    stride: the stride of the convolving kernel. Can be a single number or a\n      tuple ``(sT, sH, sW)``. Default: 1\n    padding: ``dilation * (kernel_size - 1) - padding`` zero-padding will be added to both\n      sides of each dimension in the input. Can be a single number or a tuple\n      ``(padT, padH, padW)``. Default: 0\n    output_padding: additional size added to one side of each dimension in the\n      output shape. Can be a single number or a tuple\n      ``(out_padT, out_padH, out_padW)``. Default: 0\n    groups: split input into groups, :math:`\\text{in\\_channels}` should be divisible by the\n      number of groups. Default: 1\n    dilation: the spacing between kernel elements. Can be a single number or\n      a tuple `(dT, dH, dW)`. Default: 1\n\nExamples::\n\n    >>> inputs = torch.randn(20, 16, 50, 10, 20)\n    >>> weights = torch.randn(16, 33, 3, 3, 3)\n    >>> F.conv_transpose3d(inputs, weights)\n'
        pass
    
    @classmethod
    def convolution(cls):
        pass
    
    @classmethod
    def cos(cls):
        '\ncos(input, out=None) -> Tensor\n\nReturns a new tensor with the cosine  of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\cos(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 1.4309,  1.2706, -0.8562,  0.9796])\n    >>> torch.cos(a)\n    tensor([ 0.1395,  0.2957,  0.6553,  0.5574])\n'
        pass
    
    @classmethod
    def cos_(cls):
        pass
    
    @classmethod
    def cosh(cls):
        '\ncosh(input, out=None) -> Tensor\n\nReturns a new tensor with the hyperbolic cosine  of the elements of\n:attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\cosh(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.1632,  1.1835, -0.6979, -0.7325])\n    >>> torch.cosh(a)\n    tensor([ 1.0133,  1.7860,  1.2536,  1.2805])\n'
        pass
    
    @classmethod
    def cosh_(cls):
        pass
    
    @classmethod
    def cosine_embedding_loss(cls):
        pass
    
    @classmethod
    def cosine_similarity(cls):
        '\ncosine_similarity(x1, x2, dim=1, eps=1e-8) -> Tensor\n\nReturns cosine similarity between x1 and x2, computed along dim.\n\n.. math ::\n    \\text{similarity} = \\dfrac{x_1 \\cdot x_2}{\\max(\\Vert x_1 \\Vert _2 \\cdot \\Vert x_2 \\Vert _2, \\epsilon)}\n\nArgs:\n    x1 (Tensor): First input.\n    x2 (Tensor): Second input (of size matching x1).\n    dim (int, optional): Dimension of vectors. Default: 1\n    eps (float, optional): Small value to avoid division by zero.\n        Default: 1e-8\n\nShape:\n    - Input: :math:`(\\ast_1, D, \\ast_2)` where D is at position `dim`.\n    - Output: :math:`(\\ast_1, \\ast_2)` where 1 is at position `dim`.\n\nExample::\n\n    >>> input1 = torch.randn(100, 128)\n    >>> input2 = torch.randn(100, 128)\n    >>> output = F.cosine_similarity(input1, input2)\n    >>> print(output)\n'
        pass
    
    @classmethod
    def cross(cls):
        '\ncross(input, other, dim=-1, out=None) -> Tensor\n\n\nReturns the cross product of vectors in dimension :attr:`dim` of :attr:`input`\nand :attr:`other`.\n\n:attr:`input` and :attr:`other` must have the same size, and the size of their\n:attr:`dim` dimension should be 3.\n\nIf :attr:`dim` is not given, it defaults to the first dimension found with the\nsize 3.\n\nArgs:\n    input (Tensor): the input tensor\n    other (Tensor): the second input tensor\n    dim  (int, optional): the dimension to take the cross-product in.\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 3)\n    >>> a\n    tensor([[-0.3956,  1.1455,  1.6895],\n            [-0.5849,  1.3672,  0.3599],\n            [-1.1626,  0.7180, -0.0521],\n            [-0.1339,  0.9902, -2.0225]])\n    >>> b = torch.randn(4, 3)\n    >>> b\n    tensor([[-0.0257, -1.4725, -1.2251],\n            [-1.1479, -0.7005, -1.9757],\n            [-1.3904,  0.3726, -1.1836],\n            [-0.9688, -0.7153,  0.2159]])\n    >>> torch.cross(a, b, dim=1)\n    tensor([[ 1.0844, -0.5281,  0.6120],\n            [-2.4490, -1.5687,  1.9792],\n            [-0.8304, -1.3037,  0.5650],\n            [-1.2329,  1.9883,  1.0551]])\n    >>> torch.cross(a, b)\n    tensor([[ 1.0844, -0.5281,  0.6120],\n            [-2.4490, -1.5687,  1.9792],\n            [-0.8304, -1.3037,  0.5650],\n            [-1.2329,  1.9883,  1.0551]])\n'
        pass
    
    @classmethod
    def ctc_loss(cls):
        pass
    
    @classmethod
    def cudnn_affine_grid_generator(cls):
        pass
    
    @classmethod
    def cudnn_batch_norm(cls):
        pass
    
    @classmethod
    def cudnn_convolution(cls):
        pass
    
    @classmethod
    def cudnn_convolution_transpose(cls):
        pass
    
    @classmethod
    def cudnn_grid_sampler(cls):
        pass
    
    @classmethod
    def cudnn_is_acceptable(cls):
        pass
    
    @classmethod
    def cumprod(cls):
        '\ncumprod(input, dim, out=None, dtype=None) -> Tensor\n\nReturns the cumulative product of elements of :attr:`input` in the dimension\n:attr:`dim`.\n\nFor example, if :attr:`input` is a vector of size N, the result will also be\na vector of size N, with elements.\n\n.. math::\n    y_i = x_1 \\times x_2\\times x_3\\times \\dots \\times x_i\n\nArgs:\n    input (Tensor): the input tensor\n    dim  (int): the dimension to do the operation over\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        If specified, the input tensor is casted to :attr:`dtype` before the operation\n        is performed. This is useful for preventing data type overflows. Default: None.\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(10)\n    >>> a\n    tensor([ 0.6001,  0.2069, -0.1919,  0.9792,  0.6727,  1.0062,  0.4126,\n            -0.2129, -0.4206,  0.1968])\n    >>> torch.cumprod(a, dim=0)\n    tensor([ 0.6001,  0.1241, -0.0238, -0.0233, -0.0157, -0.0158, -0.0065,\n             0.0014, -0.0006, -0.0001])\n\n    >>> a[5] = 0.0\n    >>> torch.cumprod(a, dim=0)\n    tensor([ 0.6001,  0.1241, -0.0238, -0.0233, -0.0157, -0.0000, -0.0000,\n             0.0000, -0.0000, -0.0000])\n'
        pass
    
    @classmethod
    def cumsum(cls):
        '\ncumsum(input, dim, out=None, dtype=None) -> Tensor\n\nReturns the cumulative sum of elements of :attr:`input` in the dimension\n:attr:`dim`.\n\nFor example, if :attr:`input` is a vector of size N, the result will also be\na vector of size N, with elements.\n\n.. math::\n    y_i = x_1 + x_2 + x_3 + \\dots + x_i\n\nArgs:\n    input (Tensor): the input tensor\n    dim  (int): the dimension to do the operation over\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        If specified, the input tensor is casted to :attr:`dtype` before the operation\n        is performed. This is useful for preventing data type overflows. Default: None.\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(10)\n    >>> a\n    tensor([-0.8286, -0.4890,  0.5155,  0.8443,  0.1865, -0.1752, -2.0595,\n             0.1850, -1.1571, -0.4243])\n    >>> torch.cumsum(a, dim=0)\n    tensor([-0.8286, -1.3175, -0.8020,  0.0423,  0.2289,  0.0537, -2.0058,\n            -1.8209, -2.9780, -3.4022])\n'
        pass
    
    @classmethod
    def dequantize(cls):
        pass
    
    @classmethod
    def det(cls):
        "\ndet(A) -> Tensor\n\nCalculates determinant of a 2D square tensor.\n\n.. note::\n    Backward through :meth:`det` internally uses SVD results when :attr:`A` is\n    not invertible. In this case, double backward through :meth:`det` will be\n    unstable in when :attr:`A` doesn't have distinct singular values. See\n    :meth:`~torch.svd` for details.\n\nArguments:\n    A (Tensor): The input 2D square tensor\n\nExample::\n\n    >>> A = torch.randn(3, 3)\n    >>> torch.det(A)\n    tensor(3.7641)\n"
        pass
    
    @classmethod
    def detach(cls):
        pass
    
    @classmethod
    def detach_(cls):
        pass
    
    @classmethod
    def diag(cls):
        '\ndiag(input, diagonal=0, out=None) -> Tensor\n\n- If :attr:`input` is a vector (1-D tensor), then returns a 2-D square tensor\n  with the elements of :attr:`input` as the diagonal.\n- If :attr:`input` is a matrix (2-D tensor), then returns a 1-D tensor with\n  the diagonal elements of :attr:`input`.\n\nThe argument :attr:`diagonal` controls which diagonal to consider:\n\n- If :attr:`diagonal` = 0, it is the main diagonal.\n- If :attr:`diagonal` > 0, it is above the main diagonal.\n- If :attr:`diagonal` < 0, it is below the main diagonal.\n\nArgs:\n    input (Tensor): the input tensor\n    diagonal (int, optional): the diagonal to consider\n    out (Tensor, optional): the output tensor\n\n.. seealso::\n\n        :func:`torch.diagonal` always returns the diagonal of its input.\n\n        :func:`torch.diagflat` always constructs a tensor with diagonal elements\n        specified by the input.\n\nExamples:\n\nGet the square matrix where the input vector is the diagonal::\n\n    >>> a = torch.randn(3)\n    >>> a\n    tensor([ 0.5950,-0.0872, 2.3298])\n    >>> torch.diag(a)\n    tensor([[ 0.5950, 0.0000, 0.0000],\n            [ 0.0000,-0.0872, 0.0000],\n            [ 0.0000, 0.0000, 2.3298]])\n    >>> torch.diag(a, 1)\n    tensor([[ 0.0000, 0.5950, 0.0000, 0.0000],\n            [ 0.0000, 0.0000,-0.0872, 0.0000],\n            [ 0.0000, 0.0000, 0.0000, 2.3298],\n            [ 0.0000, 0.0000, 0.0000, 0.0000]])\n\nGet the k-th diagonal of a given matrix::\n\n    >>> a = torch.randn(3, 3)\n    >>> a\n    tensor([[-0.4264, 0.0255,-0.1064],\n            [ 0.8795,-0.2429, 0.1374],\n            [ 0.1029,-0.6482,-1.6300]])\n    >>> torch.diag(a, 0)\n    tensor([-0.4264,-0.2429,-1.6300])\n    >>> torch.diag(a, 1)\n    tensor([ 0.0255, 0.1374])\n'
        pass
    
    @classmethod
    def diag_embed(cls):
        '\ndiag_embed(input, offset=0, dim1=-2, dim2=-1) -> Tensor\n\nCreates a tensor whose diagonals of certain 2D planes (specified by\n:attr:`dim1` and :attr:`dim2`) are filled by :attr:`input`.\nTo facilitate creating batched diagonal matrices, the 2D planes formed by\nthe last two dimensions of the returned tensor are chosen by default.\n\nThe argument :attr:`offset` controls which diagonal to consider:\n\n- If :attr:`offset` = 0, it is the main diagonal.\n- If :attr:`offset` > 0, it is above the main diagonal.\n- If :attr:`offset` < 0, it is below the main diagonal.\n\nThe size of the new matrix will be calculated to make the specified diagonal\nof the size of the last input dimension.\nNote that for :attr:`offset` other than :math:`0`, the order of :attr:`dim1`\nand :attr:`dim2` matters. Exchanging them is equivalent to changing the\nsign of :attr:`offset`.\n\nApplying :meth:`torch.diagonal` to the output of this function with\nthe same arguments yields a matrix identical to input. However,\n:meth:`torch.diagonal` has different default dimensions, so those\nneed to be explicitly specified.\n\nArgs:\n    input (Tensor): the input tensor. Must be at least 1-dimensional.\n    offset (int, optional): which diagonal to consider. Default: 0\n        (main diagonal).\n    dim1 (int, optional): first dimension with respect to which to\n        take diagonal. Default: -2.\n    dim2 (int, optional): second dimension with respect to which to\n        take diagonal. Default: -1.\n\nExample::\n\n    >>> a = torch.randn(2, 3)\n    >>> torch.diag_embed(a)\n    tensor([[[ 1.5410,  0.0000,  0.0000],\n             [ 0.0000, -0.2934,  0.0000],\n             [ 0.0000,  0.0000, -2.1788]],\n\n            [[ 0.5684,  0.0000,  0.0000],\n             [ 0.0000, -1.0845,  0.0000],\n             [ 0.0000,  0.0000, -1.3986]]])\n\n    >>> torch.diag_embed(a, offset=1, dim1=0, dim2=2)\n    tensor([[[ 0.0000,  1.5410,  0.0000,  0.0000],\n             [ 0.0000,  0.5684,  0.0000,  0.0000]],\n\n            [[ 0.0000,  0.0000, -0.2934,  0.0000],\n             [ 0.0000,  0.0000, -1.0845,  0.0000]],\n\n            [[ 0.0000,  0.0000,  0.0000, -2.1788],\n             [ 0.0000,  0.0000,  0.0000, -1.3986]],\n\n            [[ 0.0000,  0.0000,  0.0000,  0.0000],\n             [ 0.0000,  0.0000,  0.0000,  0.0000]]])\n'
        pass
    
    @classmethod
    def diagflat(cls):
        '\ndiagflat(input, diagonal=0) -> Tensor\n\n- If :attr:`input` is a vector (1-D tensor), then returns a 2-D square tensor\n  with the elements of :attr:`input` as the diagonal.\n- If :attr:`input` is a tensor with more than one dimension, then returns a\n  2-D tensor with diagonal elements equal to a flattened :attr:`input`.\n\nThe argument :attr:`offset` controls which diagonal to consider:\n\n- If :attr:`offset` = 0, it is the main diagonal.\n- If :attr:`offset` > 0, it is above the main diagonal.\n- If :attr:`offset` < 0, it is below the main diagonal.\n\nArgs:\n    input (Tensor): the input tensor\n    offset (int, optional): the diagonal to consider. Default: 0 (main\n        diagonal).\n\nExamples::\n\n    >>> a = torch.randn(3)\n    >>> a\n    tensor([-0.2956, -0.9068,  0.1695])\n    >>> torch.diagflat(a)\n    tensor([[-0.2956,  0.0000,  0.0000],\n            [ 0.0000, -0.9068,  0.0000],\n            [ 0.0000,  0.0000,  0.1695]])\n    >>> torch.diagflat(a, 1)\n    tensor([[ 0.0000, -0.2956,  0.0000,  0.0000],\n            [ 0.0000,  0.0000, -0.9068,  0.0000],\n            [ 0.0000,  0.0000,  0.0000,  0.1695],\n            [ 0.0000,  0.0000,  0.0000,  0.0000]])\n\n    >>> a = torch.randn(2, 2)\n    >>> a\n    tensor([[ 0.2094, -0.3018],\n            [-0.1516,  1.9342]])\n    >>> torch.diagflat(a)\n    tensor([[ 0.2094,  0.0000,  0.0000,  0.0000],\n            [ 0.0000, -0.3018,  0.0000,  0.0000],\n            [ 0.0000,  0.0000, -0.1516,  0.0000],\n            [ 0.0000,  0.0000,  0.0000,  1.9342]])\n'
        pass
    
    @classmethod
    def diagonal(cls):
        '\ndiagonal(input, offset=0, dim1=0, dim2=1) -> Tensor\n\nReturns a partial view of :attr:`input` with the its diagonal elements\nwith respect to :attr:`dim1` and :attr:`dim2` appended as a dimension\nat the end of the shape.\n\nThe argument :attr:`offset` controls which diagonal to consider:\n\n- If :attr:`offset` = 0, it is the main diagonal.\n- If :attr:`offset` > 0, it is above the main diagonal.\n- If :attr:`offset` < 0, it is below the main diagonal.\n\nApplying :meth:`torch.diag_embed` to the output of this function with\nthe same arguments yields a diagonal matrix with the diagonal entries\nof the input. However, :meth:`torch.diag_embed` has different default\ndimensions, so those need to be explicitly specified.\n\nArgs:\n    input (Tensor): the input tensor. Must be at least 2-dimensional.\n    offset (int, optional): which diagonal to consider. Default: 0\n        (main diagonal).\n    dim1 (int, optional): first dimension with respect to which to\n        take diagonal. Default: 0.\n    dim2 (int, optional): second dimension with respect to which to\n        take diagonal. Default: 1.\n\n.. note::  To take a batch diagonal, pass in dim1=-2, dim2=-1.\n\nExamples::\n\n    >>> a = torch.randn(3, 3)\n    >>> a\n    tensor([[-1.0854,  1.1431, -0.1752],\n            [ 0.8536, -0.0905,  0.0360],\n            [ 0.6927, -0.3735, -0.4945]])\n\n\n    >>> torch.diagonal(a, 0)\n    tensor([-1.0854, -0.0905, -0.4945])\n\n\n    >>> torch.diagonal(a, 1)\n    tensor([ 1.1431,  0.0360])\n\n\n    >>> x = torch.randn(2, 5, 4, 2)\n    >>> torch.diagonal(x, offset=-1, dim1=1, dim2=2)\n    tensor([[[-1.2631,  0.3755, -1.5977, -1.8172],\n             [-1.1065,  1.0401, -0.2235, -0.7938]],\n\n            [[-1.7325, -0.3081,  0.6166,  0.2335],\n             [ 1.0500,  0.7336, -0.3836, -1.1015]]])\n'
        pass
    
    @classmethod
    def digamma(cls):
        "\ndigamma(input, out=None) -> Tensor\n\nComputes the logarithmic derivative of the gamma function on `input`.\n\n.. math::\n    \\psi(x) = \\frac{d}{dx} \\ln\\left(\\Gamma\\left(x\\right)\\right) = \\frac{\\Gamma'(x)}{\\Gamma(x)}\n\nArgs:\n    input (Tensor): the tensor to compute the digamma function on\n\nExample::\n\n    >>> a = torch.tensor([1, 0.5])\n    >>> torch.digamma(a)\n    tensor([-0.5772, -1.9635])\n"
        pass
    
    @classmethod
    def dist(cls):
        '\ndist(input, other, p=2) -> Tensor\n\nReturns the p-norm of (:attr:`input` - :attr:`other`)\n\nThe shapes of :attr:`input` and :attr:`other` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\nArgs:\n    input (Tensor): the input tensor\n    other (Tensor): the Right-hand-side input tensor\n    p (float, optional): the norm to be computed\n\nExample::\n\n    >>> x = torch.randn(4)\n    >>> x\n    tensor([-1.5393, -0.8675,  0.5916,  1.6321])\n    >>> y = torch.randn(4)\n    >>> y\n    tensor([ 0.0967, -1.0511,  0.6295,  0.8360])\n    >>> torch.dist(x, y, 3.5)\n    tensor(1.6727)\n    >>> torch.dist(x, y, 3)\n    tensor(1.6973)\n    >>> torch.dist(x, y, 0)\n    tensor(inf)\n    >>> torch.dist(x, y, 1)\n    tensor(2.6537)\n'
        pass
    
    @classmethod
    def div(cls):
        '\n.. function:: div(input, value, out=None) -> Tensor\n\nDivides each element of the input :attr:`input` with the scalar :attr:`value`\nand returns a new resulting tensor.\n\n.. math::\n    \\text{out}_i = \\frac{\\text{input}_i}{\\text{value}}\n\nIf :attr:`input` is of type `FloatTensor` or `DoubleTensor`, :attr:`value`\nshould be a real number, otherwise it should be an integer\n\nArgs:\n    input (Tensor): the input tensor\n    value (Number): the number to be divided to each element of :attr:`input`\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(5)\n    >>> a\n    tensor([ 0.3810,  1.2774, -0.2972, -0.3719,  0.4637])\n    >>> torch.div(a, 0.5)\n    tensor([ 0.7620,  2.5548, -0.5944, -0.7439,  0.9275])\n\n.. function:: div(input, other, out=None) -> Tensor\n\nEach element of the tensor :attr:`input` is divided by each element\nof the tensor :attr:`other`. The resulting tensor is returned. The shapes of\n:attr:`input` and :attr:`other` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\n.. math::\n    \\text{out}_i = \\frac{\\text{input}_i}{\\text{other}_i}\n\nArgs:\n    input (Tensor): the numerator tensor\n    other (Tensor): the denominator tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[-0.3711, -1.9353, -0.4605, -0.2917],\n            [ 0.1815, -1.0111,  0.9805, -1.5923],\n            [ 0.1062,  1.4581,  0.7759, -1.2344],\n            [-0.1830, -0.0313,  1.1908, -1.4757]])\n    >>> b = torch.randn(4)\n    >>> b\n    tensor([ 0.8032,  0.2930, -0.8113, -0.2308])\n    >>> torch.div(a, b)\n    tensor([[-0.4620, -6.6051,  0.5676,  1.2637],\n            [ 0.2260, -3.4507, -1.2086,  6.8988],\n            [ 0.1322,  4.9764, -0.9564,  5.3480],\n            [-0.2278, -0.1068, -1.4678,  6.3936]])\n'
        pass
    
    @classmethod
    def dot(cls):
        '\ndot(tensor1, tensor2) -> Tensor\n\nComputes the dot product (inner product) of two tensors.\n\n.. note:: This function does not :ref:`broadcast <broadcasting-semantics>`.\n\nExample::\n\n    >>> torch.dot(torch.tensor([2, 3]), torch.tensor([2, 1]))\n    tensor(7)\n'
        pass
    
    @classmethod
    def dropout(cls):
        pass
    
    @classmethod
    def dropout_(cls):
        pass
    
    @classmethod
    def dsmm(cls):
        pass
    
    @classmethod
    def eig(cls):
        "\neig(a, eigenvectors=False, out=None) -> (Tensor, Tensor)\n\nComputes the eigenvalues and eigenvectors of a real square matrix.\n\n.. note:: Since eigenvalues and eigenvectors might be complex, backward pass is supported only\nfor :func:`torch.symeig`\n\nArgs:\n    a (Tensor): the square matrix of shape :math:`(n \\times n)` for which the eigenvalues and eigenvectors\n        will be computed\n    eigenvectors (bool): ``True`` to compute both eigenvalues and eigenvectors;\n        otherwise, only eigenvalues will be computed\n    out (tuple, optional): the output tensors\n\nReturns:\n    (Tensor, Tensor): A namedtuple (eigenvalues, eigenvectors) containing\n\n        - **eigenvalues** (*Tensor*): Shape :math:`(n \\times 2)`. Each row is an eigenvalue of ``a``,\n          where the first element is the real part and the second element is the imaginary part.\n          The eigenvalues are not necessarily ordered.\n        - **eigenvectors** (*Tensor*): If ``eigenvectors=False``, it's an empty tensor.\n          Otherwise, this tensor of shape :math:`(n \\times n)` can be used to compute normalized (unit length)\n          eigenvectors of corresponding eigenvalues as follows.\n          If the corresponding `eigenvalues[j]` is a real number, column `eigenvectors[:, j]` is the eigenvector\n          corresponding to `eigenvalues[j]`.\n          If the corresponding `eigenvalues[j]` and `eigenvalues[j + 1]` form a complex conjugate pair, then the\n          true eigenvectors can be computed as\n          :math:`\\text{true eigenvector}[j] = eigenvectors[:, j] + i \\times eigenvectors[:, j + 1]`,\n          :math:`\\text{true eigenvector}[j + 1] = eigenvectors[:, j] - i \\times eigenvectors[:, j + 1]`.\n"
        pass
    
    @classmethod
    def einsum(cls):
        pass
    
    @classmethod
    def embedding(cls):
        pass
    
    @classmethod
    def embedding_bag(cls):
        pass
    
    @classmethod
    def embedding_renorm_(cls):
        pass
    
    @classmethod
    def empty(cls):
        '\nempty(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False) -> Tensor\n\nReturns a tensor filled with uninitialized data. The shape of the tensor is\ndefined by the variable argument :attr:`sizes`.\n\nArgs:\n    sizes (int...): a sequence of integers defining the shape of the output tensor.\n        Can be a variable number of arguments or a collection like a list or tuple.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n    pin_memory (bool, optional): If set, returned tensor would be allocated in\n        the pinned memory. Works only for CPU tensors. Default: ``False``.\n\nExample::\n\n    >>> torch.empty(2, 3)\n    tensor(1.00000e-08 *\n           [[ 6.3984,  0.0000,  0.0000],\n            [ 0.0000,  0.0000,  0.0000]])\n\n'
        pass
    
    @classmethod
    def empty_like(cls):
        '\nempty_like(input, dtype=None, layout=None, device=None, requires_grad=False) -> Tensor\n\nReturns an uninitialized tensor with the same size as :attr:`input`.\n``torch.empty_like(input)`` is equivalent to\n``torch.empty(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)``.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.empty((2,3), dtype=torch.int64)\n    tensor([[ 9.4064e+13,  2.8000e+01,  9.3493e+13],\n            [ 7.5751e+18,  7.1428e+18,  7.5955e+18]])\n'
        pass
    
    @classmethod
    def empty_strided(cls):
        pass
    
    @classmethod
    def eq(cls):
        '\neq(input, other, out=None) -> Tensor\n\nComputes element-wise equality\n\nThe second argument can be a number or a tensor whose shape is\n:ref:`broadcastable <broadcasting-semantics>` with the first argument.\n\nArgs:\n    input (Tensor): the tensor to compare\n    other (Tensor or float): the tensor or value to compare\n    out (Tensor, optional): the output tensor. Must be a `ByteTensor`\n\nReturns:\n    Tensor: A ``torch.ByteTensor`` containing a 1 at each location where comparison is true\n\nExample::\n\n    >>> torch.eq(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))\n    tensor([[ 1,  0],\n            [ 0,  1]], dtype=torch.uint8)\n'
        pass
    
    @classmethod
    def equal(cls):
        '\nequal(tensor1, tensor2) -> bool\n\n``True`` if two tensors have the same size and elements, ``False`` otherwise.\n\nExample::\n\n    >>> torch.equal(torch.tensor([1, 2]), torch.tensor([1, 2]))\n    True\n'
        pass
    
    @classmethod
    def erf(cls):
        '\nerf(tensor, out=None) -> Tensor\n\nComputes the error function of each element. The error function is defined as follows:\n\n.. math::\n    \\mathrm{erf}(x) = \\frac{2}{\\sqrt{\\pi}} \\int_{0}^{x} e^{-t^2} dt\n\nArgs:\n    tensor (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.erf(torch.tensor([0, -1., 10.]))\n    tensor([ 0.0000, -0.8427,  1.0000])\n'
        pass
    
    @classmethod
    def erf_(cls):
        pass
    
    @classmethod
    def erfc(cls):
        '\nerfc(input, out=None) -> Tensor\n\nComputes the complementary error function of each element of :attr:`input`.\nThe complementary error function is defined as follows:\n\n.. math::\n    \\mathrm{erfc}(x) = 1 - \\frac{2}{\\sqrt{\\pi}} \\int_{0}^{x} e^{-t^2} dt\n\nArgs:\n    tensor (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.erfc(torch.tensor([0, -1., 10.]))\n    tensor([ 1.0000, 1.8427,  0.0000])\n'
        pass
    
    @classmethod
    def erfc_(cls):
        pass
    
    @classmethod
    def erfinv(cls):
        '\nerfinv(input, out=None) -> Tensor\n\nComputes the inverse error function of each element of :attr:`input`.\nThe inverse error function is defined in the range :math:`(-1, 1)` as:\n\n.. math::\n    \\mathrm{erfinv}(\\mathrm{erf}(x)) = x\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.erfinv(torch.tensor([0, 0.5, -1.]))\n    tensor([ 0.0000,  0.4769,    -inf])\n'
        pass
    
    @classmethod
    def exp(cls):
        '\nexp(input, out=None) -> Tensor\n\nReturns a new tensor with the exponential of the elements\nof the input tensor :attr:`input`.\n\n.. math::\n    y_{i} = e^{x_{i}}\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.exp(torch.tensor([0, math.log(2.)]))\n    tensor([ 1.,  2.])\n'
        pass
    
    @classmethod
    def exp_(cls):
        pass
    
    @classmethod
    def expm1(cls):
        '\nexpm1(input, out=None) -> Tensor\n\nReturns a new tensor with the exponential of the elements minus 1\nof :attr:`input`.\n\n.. math::\n    y_{i} = e^{x_{i}} - 1\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.expm1(torch.tensor([0, math.log(2.)]))\n    tensor([ 0.,  1.])\n'
        pass
    
    @classmethod
    def expm1_(cls):
        pass
    
    @classmethod
    def eye(cls):
        '\neye(n, m=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a 2-D tensor with ones on the diagonal and zeros elsewhere.\n\nArgs:\n    n (int): the number of rows\n    m (int, optional): the number of columns with default being :attr:`n`\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nReturns:\n    Tensor: A 2-D tensor with ones on the diagonal and zeros elsewhere\n\nExample::\n\n    >>> torch.eye(3)\n    tensor([[ 1.,  0.,  0.],\n            [ 0.,  1.,  0.],\n            [ 0.,  0.,  1.]])\n'
        pass
    
    @classmethod
    def fbgemm_is_cpu_supported(cls):
        pass
    
    @classmethod
    def fbgemm_linear_int8_weight(cls):
        pass
    
    @classmethod
    def fbgemm_linear_quantize_weight(cls):
        pass
    
    @classmethod
    def fbgemm_pack_quantized_matrix(cls):
        pass
    
    @classmethod
    def feature_alpha_dropout(cls):
        pass
    
    @classmethod
    def feature_alpha_dropout_(cls):
        pass
    
    @classmethod
    def feature_dropout(cls):
        pass
    
    @classmethod
    def feature_dropout_(cls):
        pass
    
    @classmethod
    def fft(cls):
        '\nfft(input, signal_ndim, normalized=False) -> Tensor\n\nComplex-to-complex Discrete Fourier Transform\n\nThis method computes the complex-to-complex discrete Fourier transform.\nIgnoring the batch dimensions, it computes the following expression:\n\n.. math::\n    X[\\omega_1, \\dots, \\omega_d] =\n        \\sum_{n_1=0}^{N_1-1} \\dots \\sum_{n_d=0}^{N_d-1} x[n_1, \\dots, n_d]\n         e^{-j\\ 2 \\pi \\sum_{i=0}^d \\frac{\\omega_i n_i}{N_i}},\n\nwhere :math:`d` = :attr:`signal_ndim` is number of dimensions for the\nsignal, and :math:`N_i` is the size of signal dimension :math:`i`.\n\nThis method supports 1D, 2D and 3D complex-to-complex transforms, indicated\nby :attr:`signal_ndim`. :attr:`input` must be a tensor with last dimension\nof size 2, representing the real and imaginary components of complex\nnumbers, and should have at least ``signal_ndim + 1`` dimensions with optionally\narbitrary number of leading batch dimensions. If :attr:`normalized` is set to\n``True``, this normalizes the result by dividing it with\n:math:`\\sqrt{\\prod_{i=1}^K N_i}` so that the operator is unitary.\n\nReturns the real and the imaginary parts together as one tensor of the same\nshape of :attr:`input`.\n\nThe inverse of this function is :func:`~torch.ifft`.\n\n.. note::\n    For CUDA tensors, an LRU cache is used for cuFFT plans to speed up\n    repeatedly running FFT methods on tensors of same geometry with same\n    configuration. See :ref:`cufft-plan-cache` for more details on how to\n    monitor and control the cache.\n\n.. warning::\n    For CPU tensors, this method is currently only available with MKL. Use\n    :func:`torch.backends.mkl.is_available` to check if MKL is installed.\n\nArguments:\n    input (Tensor): the input tensor of at least :attr:`signal_ndim` ``+ 1``\n        dimensions\n    signal_ndim (int): the number of dimensions in each signal.\n        :attr:`signal_ndim` can only be 1, 2 or 3\n    normalized (bool, optional): controls whether to return normalized results.\n        Default: ``False``\n\nReturns:\n    Tensor: A tensor containing the complex-to-complex Fourier transform result\n\nExample::\n\n    >>> # unbatched 2D FFT\n    >>> x = torch.randn(4, 3, 2)\n    >>> torch.fft(x, 2)\n    tensor([[[-0.0876,  1.7835],\n             [-2.0399, -2.9754],\n             [ 4.4773, -5.0119]],\n\n            [[-1.5716,  2.7631],\n             [-3.8846,  5.2652],\n             [ 0.2046, -0.7088]],\n\n            [[ 1.9938, -0.5901],\n             [ 6.5637,  6.4556],\n             [ 2.9865,  4.9318]],\n\n            [[ 7.0193,  1.1742],\n             [-1.3717, -2.1084],\n             [ 2.0289,  2.9357]]])\n    >>> # batched 1D FFT\n    >>> torch.fft(x, 1)\n    tensor([[[ 1.8385,  1.2827],\n             [-0.1831,  1.6593],\n             [ 2.4243,  0.5367]],\n\n            [[-0.9176, -1.5543],\n             [-3.9943, -2.9860],\n             [ 1.2838, -2.9420]],\n\n            [[-0.8854, -0.6860],\n             [ 2.4450,  0.0808],\n             [ 1.3076, -0.5768]],\n\n            [[-0.1231,  2.7411],\n             [-0.3075, -1.7295],\n             [-0.5384, -2.0299]]])\n    >>> # arbitrary number of batch dimensions, 2D FFT\n    >>> x = torch.randn(3, 3, 5, 5, 2)\n    >>> y = torch.fft(x, 2)\n    >>> y.shape\n    torch.Size([3, 3, 5, 5, 2])\n\n'
        pass
    
    @classmethod
    def fill_(cls):
        pass
    
    @classmethod
    def flatten(cls):
        '\nflatten(input, start_dim=0, end_dim=-1) -> Tensor\n\nFlattens a contiguous range of dims in a tensor.\n\nArgs:\n    input (Tensor): the input tensor\n    start_dim (int): the first dim to flatten\n    end_dim (int): the last dim to flatten\n\nExample::\n\n    >>> t = torch.tensor([[[1, 2],\n                           [3, 4]],\n                          [[5, 6],\n                           [7, 8]]])\n    >>> torch.flatten(t)\n    tensor([1, 2, 3, 4, 5, 6, 7, 8])\n    >>> torch.flatten(t, start_dim=1)\n    tensor([[1, 2, 3, 4],\n            [5, 6, 7, 8]])\n'
        pass
    
    @classmethod
    def flip(cls):
        '\nflip(input, dims) -> Tensor\n\nReverse the order of a n-D tensor along given axis in dims.\n\nArgs:\n    input (Tensor): the input tensor\n    dims (a list or tuple): axis to flip on\n\nExample::\n\n    >>> x = torch.arange(8).view(2, 2, 2)\n    >>> x\n    tensor([[[ 0,  1],\n             [ 2,  3]],\n\n            [[ 4,  5],\n             [ 6,  7]]])\n    >>> torch.flip(x, [0, 1])\n    tensor([[[ 6,  7],\n             [ 4,  5]],\n\n            [[ 2,  3],\n             [ 0,  1]]])\n'
        pass
    
    @classmethod
    def floor(cls):
        '\nfloor(input, out=None) -> Tensor\n\nReturns a new tensor with the floor of the elements of :attr:`input`,\nthe largest integer less than or equal to each element.\n\n.. math::\n    \\text{out}_{i} = \\left\\lfloor \\text{input}_{i} \\right\\rfloor\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.8166,  1.5308, -0.2530, -0.2091])\n    >>> torch.floor(a)\n    tensor([-1.,  1., -1., -1.])\n'
        pass
    
    @classmethod
    def floor_(cls):
        pass
    
    @classmethod
    def fmod(cls):
        '\nfmod(input, divisor, out=None) -> Tensor\n\nComputes the element-wise remainder of division.\n\nThe dividend and divisor may contain both for integer and floating point\nnumbers. The remainder has the same sign as the dividend :attr:`input`.\n\nWhen :attr:`divisor` is a tensor, the shapes of :attr:`input` and\n:attr:`divisor` must be :ref:`broadcastable <broadcasting-semantics>`.\n\nArgs:\n    input (Tensor): the dividend\n    divisor (Tensor or float): the divisor, which may be either a number or a tensor of the same shape as the dividend\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.fmod(torch.tensor([-3., -2, -1, 1, 2, 3]), 2)\n    tensor([-1., -0., -1.,  1.,  0.,  1.])\n    >>> torch.fmod(torch.tensor([1., 2, 3, 4, 5]), 1.5)\n    tensor([ 1.0000,  0.5000,  0.0000,  1.0000,  0.5000])\n\n\n'
        pass
    
    @classmethod
    def frac(cls):
        '\nfrac(input, out=None) -> Tensor\n\nComputes the fractional portion of each element in :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\text{input}_{i} - \\left\\lfloor \\text{input}_{i} \\right\\rfloor\n\nExample::\n\n    >>> torch.frac(torch.tensor([1, 2.5, -3.2]))\n    tensor([ 0.0000,  0.5000, -0.2000])\n'
        pass
    
    @classmethod
    def frac_(cls):
        pass
    
    @classmethod
    def frobenius_norm(cls):
        pass
    
    @classmethod
    def from_file(cls):
        pass
    
    @classmethod
    def from_numpy(cls):
        '\nfrom_numpy(ndarray) -> Tensor\n\nCreates a :class:`Tensor` from a :class:`numpy.ndarray`.\n\nThe returned tensor and :attr:`ndarray` share the same memory. Modifications to\nthe tensor will be reflected in the :attr:`ndarray` and vice versa. The returned\ntensor is not resizable.\n\nExample::\n\n    >>> a = numpy.array([1, 2, 3])\n    >>> t = torch.from_numpy(a)\n    >>> t\n    tensor([ 1,  2,  3])\n    >>> t[0] = -1\n    >>> a\n    array([-1,  2,  3])\n'
        pass
    
    @classmethod
    def full(cls):
        '\nfull(size, fill_value, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor of size :attr:`size` filled with :attr:`fill_value`.\n\nArgs:\n    size (int...): a list, tuple, or :class:`torch.Size` of integers defining the\n        shape of the output tensor.\n    fill_value: the number to fill the output tensor with.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.full((2, 3), 3.141592)\n    tensor([[ 3.1416,  3.1416,  3.1416],\n            [ 3.1416,  3.1416,  3.1416]])\n\n'
        pass
    
    @classmethod
    def full_like(cls):
        '\nfull_like(input, fill_value, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor with the same size as :attr:`input` filled with :attr:`fill_value`.\n``torch.full_like(input, fill_value)`` is equivalent to\n``torch.full(input.size(), fill_value, dtype=input.dtype, layout=input.layout, device=input.device)``.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    fill_value: the number to fill the output tensor with.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n'
        pass
    
    @classmethod
    def gather(cls):
        '\ngather(input, dim, index, out=None, sparse_grad=False) -> Tensor\n\nGathers values along an axis specified by `dim`.\n\nFor a 3-D tensor the output is specified by::\n\n    out[i][j][k] = input[index[i][j][k]][j][k]  # if dim == 0\n    out[i][j][k] = input[i][index[i][j][k]][k]  # if dim == 1\n    out[i][j][k] = input[i][j][index[i][j][k]]  # if dim == 2\n\nIf :attr:`input` is an n-dimensional tensor with size\n:math:`(x_0, x_1..., x_{i-1}, x_i, x_{i+1}, ..., x_{n-1})`\nand ``dim = i``, then :attr:`index` must be an :math:`n`-dimensional tensor with\nsize :math:`(x_0, x_1, ..., x_{i-1}, y, x_{i+1}, ..., x_{n-1})` where :math:`y \\geq 1`\nand :attr:`out` will have the same size as :attr:`index`.\n\nArgs:\n    input (Tensor): the source tensor\n    dim (int): the axis along which to index\n    index (LongTensor): the indices of elements to gather\n    out (Tensor, optional): the destination tensor\n    sparse_grad(bool,optional): If ``True``, gradient w.r.t. :attr:`input` will be a sparse tensor.\n\nExample::\n\n    >>> t = torch.tensor([[1,2],[3,4]])\n    >>> torch.gather(t, 1, torch.tensor([[0,0],[1,0]]))\n    tensor([[ 1,  1],\n            [ 4,  3]])\n'
        pass
    
    @classmethod
    def ge(cls):
        '\nge(input, other, out=None) -> Tensor\n\nComputes :math:`\\text{input} \\geq \\text{other}` element-wise.\n\nThe second argument can be a number or a tensor whose shape is\n:ref:`broadcastable <broadcasting-semantics>` with the first argument.\n\nArgs:\n    input (Tensor): the tensor to compare\n    other (Tensor or float): the tensor or value to compare\n    out (Tensor, optional): the output tensor that must be a `ByteTensor`\n\nReturns:\n    Tensor: A ``torch.ByteTensor`` containing a 1 at each location where comparison is true\n\nExample::\n\n    >>> torch.ge(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))\n    tensor([[ 1,  1],\n            [ 0,  1]], dtype=torch.uint8)\n'
        pass
    
    @classmethod
    def gels(cls):
        '\ngels(B, A, out=None) -> Tensor\n\nComputes the solution to the least squares and least norm problems for a full\nrank matrix :math:`A` of size :math:`(m \\times n)` and a matrix :math:`B` of\nsize :math:`(m \\times k)`.\n\nIf :math:`m \\geq n`, :func:`gels` solves the least-squares problem:\n\n.. math::\n\n   \\begin{array}{ll}\n   \\min_X & \\|AX-B\\|_2.\n   \\end{array}\n\nIf :math:`m < n`, :func:`gels` solves the least-norm problem:\n\n.. math::\n\n   \\begin{array}{ll}\n   \\min_X & \\|X\\|_2 & \\text{subject to} & AX = B.\n   \\end{array}\n\nReturned tensor :math:`X` has shape :math:`(\\max(m, n) \\times k)`. The first :math:`n`\nrows of :math:`X` contains the solution. If :math:`m \\geq n`, the residual sum of squares\nfor the solution in each column is given by the sum of squares of elements in the\nremaining :math:`m - n` rows of that column.\n\nArgs:\n    B (Tensor): the matrix :math:`B`\n    A (Tensor): the :math:`m` by :math:`n` matrix :math:`A`\n    out (tuple, optional): the optional destination tensor\n\nReturns:\n    (Tensor, Tensor): A namedtuple (solution, QR) containing:\n\n        - **solution** (*Tensor*): the least squares solution\n        - **QR** (*Tensor*): the details of the QR factorization\n\n.. note::\n\n    The returned matrices will always be transposed, irrespective of the strides\n    of the input matrices. That is, they will have stride `(1, m)` instead of\n    `(m, 1)`.\n\nExample::\n\n    >>> A = torch.tensor([[1., 1, 1],\n                          [2, 3, 4],\n                          [3, 5, 2],\n                          [4, 2, 5],\n                          [5, 4, 3]])\n    >>> B = torch.tensor([[-10., -3],\n                          [ 12, 14],\n                          [ 14, 12],\n                          [ 16, 16],\n                          [ 18, 16]])\n    >>> X, _ = torch.gels(B, A)\n    >>> X\n    tensor([[  2.0000,   1.0000],\n            [  1.0000,   1.0000],\n            [  1.0000,   2.0000],\n            [ 10.9635,   4.8501],\n            [  8.9332,   5.2418]])\n'
        pass
    
    @classmethod
    def geqrf(cls):
        "\ngeqrf(input, out=None) -> (Tensor, Tensor)\n\nThis is a low-level function for calling LAPACK directly. This function\nreturns a namedtuple (a, tau) as defined in `LAPACK documentation for geqrf`_ .\n\nYou'll generally want to use :func:`torch.qr` instead.\n\nComputes a QR decomposition of :attr:`input`, but without constructing\n:math:`Q` and :math:`R` as explicit separate matrices.\n\nRather, this directly calls the underlying LAPACK function `?geqrf`\nwhich produces a sequence of 'elementary reflectors'.\n\nSee `LAPACK documentation for geqrf`_ for further details.\n\nArgs:\n    input (Tensor): the input matrix\n    out (tuple, optional): the output tuple of (Tensor, Tensor)\n\n.. _LAPACK documentation for geqrf:\n    https://software.intel.com/en-us/node/521004\n\n"
        pass
    
    @classmethod
    def ger(cls):
        '\nger(vec1, vec2, out=None) -> Tensor\n\nOuter product of :attr:`vec1` and :attr:`vec2`.\nIf :attr:`vec1` is a vector of size :math:`n` and :attr:`vec2` is a vector of\nsize :math:`m`, then :attr:`out` must be a matrix of size :math:`(n \\times m)`.\n\n.. note:: This function does not :ref:`broadcast <broadcasting-semantics>`.\n\nArgs:\n    vec1 (Tensor): 1-D input vector\n    vec2 (Tensor): 1-D input vector\n    out (Tensor, optional): optional output matrix\n\nExample::\n\n    >>> v1 = torch.arange(1., 5.)\n    >>> v2 = torch.arange(1., 4.)\n    >>> torch.ger(v1, v2)\n    tensor([[  1.,   2.,   3.],\n            [  2.,   4.,   6.],\n            [  3.,   6.,   9.],\n            [  4.,   8.,  12.]])\n'
        pass
    
    @classmethod
    def get_device(cls):
        pass
    
    @classmethod
    def grid_sampler(cls):
        pass
    
    @classmethod
    def grid_sampler_2d(cls):
        pass
    
    @classmethod
    def grid_sampler_3d(cls):
        pass
    
    @classmethod
    def group_norm(cls):
        pass
    
    @classmethod
    def gru(cls):
        pass
    
    @classmethod
    def gru_cell(cls):
        pass
    
    @classmethod
    def gt(cls):
        '\ngt(input, other, out=None) -> Tensor\n\nComputes :math:`\\text{input} > \\text{other}` element-wise.\n\nThe second argument can be a number or a tensor whose shape is\n:ref:`broadcastable <broadcasting-semantics>` with the first argument.\n\nArgs:\n    input (Tensor): the tensor to compare\n    other (Tensor or float): the tensor or value to compare\n    out (Tensor, optional): the output tensor that must be a `ByteTensor`\n\nReturns:\n    Tensor: A ``torch.ByteTensor`` containing a 1 at each location where comparison is true\n\nExample::\n\n    >>> torch.gt(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))\n    tensor([[ 0,  1],\n            [ 0,  0]], dtype=torch.uint8)\n'
        pass
    
    @classmethod
    def hamming_window(cls):
        '\nhamming_window(window_length, periodic=True, alpha=0.54, beta=0.46, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nHamming window function.\n\n.. math::\n    w[n] = \\alpha - \\beta\\ \\cos \\left( \\frac{2 \\pi n}{N - 1} \\right),\n\nwhere :math:`N` is the full window size.\n\nThe input :attr:`window_length` is a positive integer controlling the\nreturned window size. :attr:`periodic` flag determines whether the returned\nwindow trims off the last duplicate value from the symmetric window and is\nready to be used as a periodic window with functions like\n:meth:`torch.stft`. Therefore, if :attr:`periodic` is true, the :math:`N` in\nabove formula is in fact :math:`\\text{window\\_length} + 1`. Also, we always have\n``torch.hamming_window(L, periodic=True)`` equal to\n``torch.hamming_window(L + 1, periodic=False)[:-1])``.\n\n.. note::\n    If :attr:`window_length` :math:`=1`, the returned window contains a single value 1.\n\n.. note::\n    This is a generalized version of :meth:`torch.hann_window`.\n\nArguments:\n    window_length (int): the size of returned window\n    periodic (bool, optional): If True, returns a window to be used as periodic\n        function. If False, return a symmetric window.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`). Only floating point types are supported.\n    layout (:class:`torch.layout`, optional): the desired layout of returned window tensor. Only\n          ``torch.strided`` (dense layout) is supported.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nReturns:\n    Tensor: A 1-D tensor of size :math:`(\\text{window\\_length},)` containing the window\n\n'
        pass
    
    @classmethod
    def hann_window(cls):
        '\nhann_window(window_length, periodic=True, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nHann window function.\n\n.. math::\n    w[n] = \\frac{1}{2}\\ \\left[1 - \\cos \\left( \\frac{2 \\pi n}{N - 1} \\right)\\right] =\n            \\sin^2 \\left( \\frac{\\pi n}{N - 1} \\right),\n\nwhere :math:`N` is the full window size.\n\nThe input :attr:`window_length` is a positive integer controlling the\nreturned window size. :attr:`periodic` flag determines whether the returned\nwindow trims off the last duplicate value from the symmetric window and is\nready to be used as a periodic window with functions like\n:meth:`torch.stft`. Therefore, if :attr:`periodic` is true, the :math:`N` in\nabove formula is in fact :math:`\\text{window\\_length} + 1`. Also, we always have\n``torch.hann_window(L, periodic=True)`` equal to\n``torch.hann_window(L + 1, periodic=False)[:-1])``.\n\n.. note::\n    If :attr:`window_length` :math:`=1`, the returned window contains a single value 1.\n\nArguments:\n    window_length (int): the size of returned window\n    periodic (bool, optional): If True, returns a window to be used as periodic\n        function. If False, return a symmetric window.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`). Only floating point types are supported.\n    layout (:class:`torch.layout`, optional): the desired layout of returned window tensor. Only\n          ``torch.strided`` (dense layout) is supported.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nReturns:\n    Tensor: A 1-D tensor of size :math:`(\\text{window\\_length},)` containing the window\n\n'
        pass
    
    @classmethod
    def hardshrink(cls):
        pass
    
    @classmethod
    def hinge_embedding_loss(cls):
        pass
    
    @classmethod
    def histc(cls):
        '\nhistc(input, bins=100, min=0, max=0, out=None) -> Tensor\n\nComputes the histogram of a tensor.\n\nThe elements are sorted into equal width bins between :attr:`min` and\n:attr:`max`. If :attr:`min` and :attr:`max` are both zero, the minimum and\nmaximum values of the data are used.\n\nArgs:\n    input (Tensor): the input tensor\n    bins (int): number of histogram bins\n    min (int): lower end of the range (inclusive)\n    max (int): upper end of the range (inclusive)\n    out (Tensor, optional): the output tensor\n\nReturns:\n    Tensor: Histogram represented as a tensor\n\nExample::\n\n    >>> torch.histc(torch.tensor([1., 2, 1]), bins=4, min=0, max=3)\n    tensor([ 0.,  2.,  1.,  0.])\n'
        pass
    
    @classmethod
    def hsmm(cls):
        pass
    
    @classmethod
    def hspmm(cls):
        pass
    
    @classmethod
    def ifft(cls):
        '\nifft(input, signal_ndim, normalized=False) -> Tensor\n\nComplex-to-complex Inverse Discrete Fourier Transform\n\nThis method computes the complex-to-complex inverse discrete Fourier\ntransform. Ignoring the batch dimensions, it computes the following\nexpression:\n\n.. math::\n    X[\\omega_1, \\dots, \\omega_d] =\n        \\frac{1}{\\prod_{i=1}^d N_i} \\sum_{n_1=0}^{N_1-1} \\dots \\sum_{n_d=0}^{N_d-1} x[n_1, \\dots, n_d]\n         e^{\\ j\\ 2 \\pi \\sum_{i=0}^d \\frac{\\omega_i n_i}{N_i}},\n\nwhere :math:`d` = :attr:`signal_ndim` is number of dimensions for the\nsignal, and :math:`N_i` is the size of signal dimension :math:`i`.\n\nThe argument specifications are almost identical with :func:`~torch.fft`.\nHowever, if :attr:`normalized` is set to ``True``, this instead returns the\nresults multiplied by :math:`\\sqrt{\\prod_{i=1}^d N_i}`, to become a unitary\noperator. Therefore, to invert a :func:`~torch.fft`, the :attr:`normalized`\nargument should be set identically for :func:`~torch.fft`.\n\nReturns the real and the imaginary parts together as one tensor of the same\nshape of :attr:`input`.\n\nThe inverse of this function is :func:`~torch.fft`.\n\n.. note::\n    For CUDA tensors, an LRU cache is used for cuFFT plans to speed up\n    repeatedly running FFT methods on tensors of same geometry with same\n    configuration. See :ref:`cufft-plan-cache` for more details on how to\n    monitor and control the cache.\n\n.. warning::\n    For CPU tensors, this method is currently only available with MKL. Use\n    :func:`torch.backends.mkl.is_available` to check if MKL is installed.\n\nArguments:\n    input (Tensor): the input tensor of at least :attr:`signal_ndim` ``+ 1``\n        dimensions\n    signal_ndim (int): the number of dimensions in each signal.\n        :attr:`signal_ndim` can only be 1, 2 or 3\n    normalized (bool, optional): controls whether to return normalized results.\n        Default: ``False``\n\nReturns:\n    Tensor: A tensor containing the complex-to-complex inverse Fourier transform result\n\nExample::\n\n    >>> x = torch.randn(3, 3, 2)\n    >>> x\n    tensor([[[ 1.2766,  1.3680],\n             [-0.8337,  2.0251],\n             [ 0.9465, -1.4390]],\n\n            [[-0.1890,  1.6010],\n             [ 1.1034, -1.9230],\n             [-0.9482,  1.0775]],\n\n            [[-0.7708, -0.8176],\n             [-0.1843, -0.2287],\n             [-1.9034, -0.2196]]])\n    >>> y = torch.fft(x, 2)\n    >>> torch.ifft(y, 2)  # recover x\n    tensor([[[ 1.2766,  1.3680],\n             [-0.8337,  2.0251],\n             [ 0.9465, -1.4390]],\n\n            [[-0.1890,  1.6010],\n             [ 1.1034, -1.9230],\n             [-0.9482,  1.0775]],\n\n            [[-0.7708, -0.8176],\n             [-0.1843, -0.2287],\n             [-1.9034, -0.2196]]])\n\n'
        pass
    
    @classmethod
    def index_add(cls):
        pass
    
    @classmethod
    def index_copy(cls):
        pass
    
    @classmethod
    def index_fill(cls):
        pass
    
    @classmethod
    def index_put(cls):
        pass
    
    @classmethod
    def index_put_(cls):
        pass
    
    @classmethod
    def index_select(cls):
        '\nindex_select(input, dim, index, out=None) -> Tensor\n\nReturns a new tensor which indexes the :attr:`input` tensor along dimension\n:attr:`dim` using the entries in :attr:`index` which is a `LongTensor`.\n\nThe returned tensor has the same number of dimensions as the original tensor\n(:attr:`input`).  The :attr:`dim`\\ th dimension has the same size as the length\nof :attr:`index`; other dimensions have the same size as in the original tensor.\n\n.. note:: The returned tensor does **not** use the same storage as the original\n          tensor.  If :attr:`out` has a different shape than expected, we\n          silently change it to the correct shape, reallocating the underlying\n          storage if necessary.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension in which we index\n    index (LongTensor): the 1-D tensor containing the indices to index\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> x = torch.randn(3, 4)\n    >>> x\n    tensor([[ 0.1427,  0.0231, -0.5414, -1.0009],\n            [-0.4664,  0.2647, -0.1228, -1.1068],\n            [-1.1734, -0.6571,  0.7230, -0.6004]])\n    >>> indices = torch.tensor([0, 2])\n    >>> torch.index_select(x, 0, indices)\n    tensor([[ 0.1427,  0.0231, -0.5414, -1.0009],\n            [-1.1734, -0.6571,  0.7230, -0.6004]])\n    >>> torch.index_select(x, 1, indices)\n    tensor([[ 0.1427, -0.5414],\n            [-0.4664, -0.1228],\n            [-1.1734,  0.7230]])\n'
        pass
    
    @classmethod
    def instance_norm(cls):
        pass
    
    @classmethod
    def int_repr(cls):
        pass
    
    @classmethod
    def inverse(cls):
        '\ninverse(input, out=None) -> Tensor\n\nTakes the inverse of the square matrix :attr:`input`. :attr:`input` can be batches\nof 2D square tensors, in which case this function would return a tensor composed of\nindividual inverses.\n\n.. note::\n\n    Irrespective of the original strides, the returned tensors will be\n    transposed, i.e. with strides like `input.contiguous().transpose(-2, -1).strides()`\n\nArgs:\n    input (Tensor): the input tensor of size (*, n, n) where `*` is zero or more\n                    batch dimensions\n    out (Tensor, optional): the optional output tensor\n\nExample::\n\n    >>> x = torch.rand(4, 4)\n    >>> y = torch.inverse(x)\n    >>> z = torch.mm(x, y)\n    >>> z\n    tensor([[ 1.0000, -0.0000, -0.0000,  0.0000],\n            [ 0.0000,  1.0000,  0.0000,  0.0000],\n            [ 0.0000,  0.0000,  1.0000,  0.0000],\n            [ 0.0000, -0.0000, -0.0000,  1.0000]])\n    >>> torch.max(torch.abs(z - torch.eye(4))) # Max non-zero\n    tensor(1.1921e-07)\n    >>> # Batched inverse example\n    >>> x = torch.randn(2, 3, 4, 4)\n    >>> y = torch.inverse(x)\n    >>> z = torch.matmul(x, y)\n    >>> torch.max(torch.abs(z - torch.eye(4).expand_as(x))) # Max non-zero\n    tensor(1.9073e-06)\n'
        pass
    
    @classmethod
    def irfft(cls):
        '\nirfft(input, signal_ndim, normalized=False, onesided=True, signal_sizes=None) -> Tensor\n\nComplex-to-real Inverse Discrete Fourier Transform\n\nThis method computes the complex-to-real inverse discrete Fourier transform.\nIt is mathematically equivalent with :func:`ifft` with differences only in\nformats of the input and output.\n\nThe argument specifications are almost identical with :func:`~torch.ifft`.\nSimilar to :func:`~torch.ifft`, if :attr:`normalized` is set to ``True``,\nthis normalizes the result by multiplying it with\n:math:`\\sqrt{\\prod_{i=1}^K N_i}` so that the operator is unitary, where\n:math:`N_i` is the size of signal dimension :math:`i`.\n\nDue to the conjugate symmetry, :attr:`input` do not need to contain the full\ncomplex frequency values. Roughly half of the values will be sufficient, as\nis the case when :attr:`input` is given by :func:`~torch.rfft` with\n``rfft(signal, onesided=True)``. In such case, set the :attr:`onesided`\nargument of this method to ``True``. Moreover, the original signal shape\ninformation can sometimes be lost, optionally set :attr:`signal_sizes` to be\nthe size of the original signal (without the batch dimensions if in batched\nmode) to recover it with correct shape.\n\nTherefore, to invert an :func:`~torch.rfft`, the :attr:`normalized` and\n:attr:`onesided` arguments should be set identically for :func:`~torch.irfft`,\nand preferrably a :attr:`signal_sizes` is given to avoid size mismatch. See the\nexample below for a case of size mismatch.\n\nSee :func:`~torch.rfft` for details on conjugate symmetry.\n\nThe inverse of this function is :func:`~torch.rfft`.\n\n.. warning::\n    Generally speaking, the input of this function should contain values\n    following conjugate symmetry. Note that even if :attr:`onesided` is\n    ``True``, often symmetry on some part is still needed. When this\n    requirement is not satisfied, the behavior of :func:`~torch.irfft` is\n    undefined. Since :func:`torch.autograd.gradcheck` estimates numerical\n    Jacobian with point perturbations, :func:`~torch.irfft` will almost\n    certainly fail the check.\n\n.. note::\n    For CUDA tensors, an LRU cache is used for cuFFT plans to speed up\n    repeatedly running FFT methods on tensors of same geometry with same\n    configuration. See :ref:`cufft-plan-cache` for more details on how to\n    monitor and control the cache.\n\n.. warning::\n    For CPU tensors, this method is currently only available with MKL. Use\n    :func:`torch.backends.mkl.is_available` to check if MKL is installed.\n\nArguments:\n    input (Tensor): the input tensor of at least :attr:`signal_ndim` ``+ 1``\n        dimensions\n    signal_ndim (int): the number of dimensions in each signal.\n        :attr:`signal_ndim` can only be 1, 2 or 3\n    normalized (bool, optional): controls whether to return normalized results.\n        Default: ``False``\n    onesided (bool, optional): controls whether :attr:`input` was halfed to avoid\n        redundancy, e.g., by :func:`rfft`. Default: ``True``\n    signal_sizes (list or :class:`torch.Size`, optional): the size of the original\n        signal (without batch dimension). Default: ``None``\n\nReturns:\n    Tensor: A tensor containing the complex-to-real inverse Fourier transform result\n\nExample::\n\n    >>> x = torch.randn(4, 4)\n    >>> torch.rfft(x, 2, onesided=True).shape\n    torch.Size([4, 3, 2])\n    >>>\n    >>> # notice that with onesided=True, output size does not determine the original signal size\n    >>> x = torch.randn(4, 5)\n\n    >>> torch.rfft(x, 2, onesided=True).shape\n    torch.Size([4, 3, 2])\n    >>>\n    >>> # now we use the original shape to recover x\n    >>> x\n    tensor([[-0.8992,  0.6117, -1.6091, -0.4155, -0.8346],\n            [-2.1596, -0.0853,  0.7232,  0.1941, -0.0789],\n            [-2.0329,  1.1031,  0.6869, -0.5042,  0.9895],\n            [-0.1884,  0.2858, -1.5831,  0.9917, -0.8356]])\n    >>> y = torch.rfft(x, 2, onesided=True)\n    >>> torch.irfft(y, 2, onesided=True, signal_sizes=x.shape)  # recover x\n    tensor([[-0.8992,  0.6117, -1.6091, -0.4155, -0.8346],\n            [-2.1596, -0.0853,  0.7232,  0.1941, -0.0789],\n            [-2.0329,  1.1031,  0.6869, -0.5042,  0.9895],\n            [-0.1884,  0.2858, -1.5831,  0.9917, -0.8356]])\n\n'
        pass
    
    @classmethod
    def is_complex(cls):
        pass
    
    @classmethod
    def is_distributed(cls):
        pass
    
    @classmethod
    def is_floating_point(cls):
        '\nis_floating_point(tensor) -> (bool)\n\nReturns True if the data type of :attr:`tensor` is a floating point data type i.e.,\none of ``torch.float64``, ``torch.float32`` and ``torch.float16``.\n\nArgs:\n    tensor (Tensor): the PyTorch tensor to test\n'
        pass
    
    @classmethod
    def is_nonzero(cls):
        pass
    
    @classmethod
    def is_same_size(cls):
        pass
    
    @classmethod
    def is_signed(cls):
        pass
    
    @classmethod
    def isclose(cls):
        pass
    
    @classmethod
    def isnan(cls):
        "\nReturns a new tensor with boolean elements representing if each element is `NaN` or not.\n\nArguments:\n    tensor (Tensor): A tensor to check\n\nReturns:\n    Tensor: A ``torch.ByteTensor`` containing a 1 at each location of `NaN` elements.\n\nExample::\n\n    >>> torch.isnan(torch.tensor([1, float('nan'), 2]))\n    tensor([ 0,  1,  0], dtype=torch.uint8)\n"
        pass
    
    @classmethod
    def kl_div(cls):
        pass
    
    @classmethod
    def kthvalue(cls):
        '\nkthvalue(input, k, dim=None, keepdim=False, out=None) -> (Tensor, LongTensor)\n\nReturns a namedtuple ``(values, indices)`` where ``values`` is the :attr:`k` th\nsmallest element of each row of the :attr:`input` tensor in the given dimension\n:attr:`dim`. And ``indices`` is the index location of each element found.\n\nIf :attr:`dim` is not given, the last dimension of the `input` is chosen.\n\nIf :attr:`keepdim` is ``True``, both the :attr:`values` and :attr:`indices` tensors\nare the same size as :attr:`input`, except in the dimension :attr:`dim` where\nthey are of size 1. Otherwise, :attr:`dim` is squeezed\n(see :func:`torch.squeeze`), resulting in both the :attr:`values` and\n:attr:`indices` tensors having 1 fewer dimension than the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n    k (int): k for the k-th smallest element\n    dim (int, optional): the dimension to find the kth value along\n    keepdim (bool): whether the output tensors have :attr:`dim` retained or not\n    out (tuple, optional): the output tuple of (Tensor, LongTensor)\n                           can be optionally given to be used as output buffers\n\nExample::\n\n    >>> x = torch.arange(1., 6.)\n    >>> x\n    tensor([ 1.,  2.,  3.,  4.,  5.])\n    >>> torch.kthvalue(x, 4)\n    torch.return_types.kthvalue(values=tensor(4.), indices=tensor(3))\n\n    >>> x=torch.arange(1.,7.).resize_(2,3)\n    >>> x\n    tensor([[ 1.,  2.,  3.],\n            [ 4.,  5.,  6.]])\n    >>> torch.kthvalue(x, 2, 0, True)\n    torch.return_types.kthvalue(values=tensor([[4., 5., 6.]]), indices=tensor([[1, 1, 1]]))\n'
        pass
    
    @classmethod
    def layer_norm(cls):
        pass
    
    @classmethod
    def le(cls):
        '\nle(input, other, out=None) -> Tensor\n\nComputes :math:`\\text{input} \\leq \\text{other}` element-wise.\n\nThe second argument can be a number or a tensor whose shape is\n:ref:`broadcastable <broadcasting-semantics>` with the first argument.\n\nArgs:\n    input (Tensor): the tensor to compare\n    other (Tensor or float): the tensor or value to compare\n    out (Tensor, optional): the output tensor that must be a `ByteTensor`\n\nReturns:\n    Tensor: A ``torch.ByteTensor`` containing a 1 at each location where comparison is true\n\nExample::\n\n    >>> torch.le(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))\n    tensor([[ 1,  0],\n            [ 1,  1]], dtype=torch.uint8)\n'
        pass
    
    @classmethod
    def lerp(cls):
        '\nlerp(start, end, weight, out=None)\n\nDoes a linear interpolation of two tensors :attr:`start` and :attr:`end` based\non a scalar or tensor :attr:`weight` and returns the resulting :attr:`out` tensor.\n\n.. math::\n    \\text{out}_i = \\text{start}_i + \\text{weight}_i \\times (\\text{end}_i - \\text{start}_i)\n\nThe shapes of :attr:`start` and :attr:`end` must be\n:ref:`broadcastable <broadcasting-semantics>`. If :attr:`weight` is a tensor, then\nthe shapes of :attr:`start`, :attr:`end` must be :ref:`broadcastable <broadcasting-semantics>`.\n\nArgs:\n    start (Tensor): the tensor with the starting points\n    end (Tensor): the tensor with the ending points\n    weight (float or tensor): the weight for the interpolation formula\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> start = torch.arange(1., 5.)\n    >>> end = torch.empty(4).fill_(10)\n    >>> start\n    tensor([ 1.,  2.,  3.,  4.])\n    >>> end\n    tensor([ 10.,  10.,  10.,  10.])\n    >>> torch.lerp(start, end, 0.5)\n    tensor([ 5.5000,  6.0000,  6.5000,  7.0000])\n    >>> torch.lerp(start, end, torch.full_like(start, 0.5))\n    tensor([ 5.5000,  6.0000,  6.5000,  7.0000])\n'
        pass
    
    @classmethod
    def lgamma(cls):
        pass
    
    @classmethod
    def linspace(cls):
        '\nlinspace(start, end, steps=100, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a one-dimensional tensor of :attr:`steps`\nequally spaced points between :attr:`start` and :attr:`end`.\n\nThe output tensor is 1-D of size :attr:`steps`.\n\nArgs:\n    start (float): the starting value for the set of points\n    end (float): the ending value for the set of points\n    steps (int): number of points to sample between :attr:`start`\n        and :attr:`end`. Default: ``100``.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\n\nExample::\n\n    >>> torch.linspace(3, 10, steps=5)\n    tensor([  3.0000,   4.7500,   6.5000,   8.2500,  10.0000])\n    >>> torch.linspace(-10, 10, steps=5)\n    tensor([-10.,  -5.,   0.,   5.,  10.])\n    >>> torch.linspace(start=-10, end=10, steps=5)\n    tensor([-10.,  -5.,   0.,   5.,  10.])\n    >>> torch.linspace(start=-10, end=10, steps=1)\n    tensor([-10.])\n'
        pass
    
    @classmethod
    def log(cls):
        '\nlog(input, out=None) -> Tensor\n\nReturns a new tensor with the natural logarithm of the elements\nof :attr:`input`.\n\n.. math::\n    y_{i} = \\log_{e} (x_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(5)\n    >>> a\n    tensor([-0.7168, -0.5471, -0.8933, -1.4428, -0.1190])\n    >>> torch.log(a)\n    tensor([ nan,  nan,  nan,  nan,  nan])\n'
        pass
    
    @classmethod
    def log10(cls):
        '\nlog10(input, out=None) -> Tensor\n\nReturns a new tensor with the logarithm to the base 10 of the elements\nof :attr:`input`.\n\n.. math::\n    y_{i} = \\log_{10} (x_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.rand(5)\n    >>> a\n    tensor([ 0.5224,  0.9354,  0.7257,  0.1301,  0.2251])\n\n\n    >>> torch.log10(a)\n    tensor([-0.2820, -0.0290, -0.1392, -0.8857, -0.6476])\n\n'
        pass
    
    @classmethod
    def log10_(cls):
        pass
    
    @classmethod
    def log1p(cls):
        '\nlog1p(input, out=None) -> Tensor\n\nReturns a new tensor with the natural logarithm of (1 + :attr:`input`).\n\n.. math::\n    y_i = \\log_{e} (x_i + 1)\n\n.. note:: This function is more accurate than :func:`torch.log` for small\n          values of :attr:`input`\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(5)\n    >>> a\n    tensor([-1.0090, -0.9923,  1.0249, -0.5372,  0.2492])\n    >>> torch.log1p(a)\n    tensor([    nan, -4.8653,  0.7055, -0.7705,  0.2225])\n'
        pass
    
    @classmethod
    def log1p_(cls):
        pass
    
    @classmethod
    def log2(cls):
        '\nlog2(input, out=None) -> Tensor\n\nReturns a new tensor with the logarithm to the base 2 of the elements\nof :attr:`input`.\n\n.. math::\n    y_{i} = \\log_{2} (x_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.rand(5)\n    >>> a\n    tensor([ 0.8419,  0.8003,  0.9971,  0.5287,  0.0490])\n\n\n    >>> torch.log2(a)\n    tensor([-0.2483, -0.3213, -0.0042, -0.9196, -4.3504])\n\n'
        pass
    
    @classmethod
    def log2_(cls):
        pass
    
    @classmethod
    def log_(cls):
        pass
    
    @classmethod
    def log_softmax(cls):
        pass
    
    @classmethod
    def logdet(cls):
        "\nlogdet(A) -> Tensor\n\nCalculates log determinant of a 2D square tensor.\n\n.. note::\n    Result is ``-inf`` if :attr:`A` has zero log determinant, and is ``nan`` if\n    :attr:`A` has negative determinant.\n\n.. note::\n    Backward through :meth:`logdet` internally uses SVD results when :attr:`A`\n    is not invertible. In this case, double backward through :meth:`logdet` will\n    be unstable in when :attr:`A` doesn't have distinct singular values. See\n    :meth:`~torch.svd` for details.\n\nArguments:\n    A (Tensor): The input 2D square tensor\n\nExample::\n\n    >>> A = torch.randn(3, 3)\n    >>> torch.det(A)\n    tensor(0.2611)\n    >>> torch.logdet(A)\n    tensor(-1.3430)\n"
        pass
    
    @classmethod
    def logspace(cls):
        '\nlogspace(start, end, steps=100, base=10.0, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a one-dimensional tensor of :attr:`steps` points\nlogarithmically spaced with base :attr:`base` between\n:math:`{\\text{base}}^{\\text{start}}` and :math:`{\\text{base}}^{\\text{end}}`.\n\nThe output tensor is 1-D of size :attr:`steps`.\n\nArgs:\n    start (float): the starting value for the set of points\n    end (float): the ending value for the set of points\n    steps (int): number of points to sample between :attr:`start`\n        and :attr:`end`. Default: ``100``.\n    base (float): base of the logarithm function. Default: ``10.0``.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.logspace(start=-10, end=10, steps=5)\n    tensor([ 1.0000e-10,  1.0000e-05,  1.0000e+00,  1.0000e+05,  1.0000e+10])\n    >>> torch.logspace(start=0.1, end=1.0, steps=5)\n    tensor([  1.2589,   2.1135,   3.5481,   5.9566,  10.0000])\n    >>> torch.logspace(start=0.1, end=1.0, steps=1)\n    tensor([1.2589])\n    >>> torch.logspace(start=2, end=2, steps=1, base=2)\n    tensor([4.0])\n'
        pass
    
    @classmethod
    def logsumexp(cls):
        '\nlogsumexp(input, dim, keepdim=False, out=None)\n\nReturns the log of summed exponentials of each row of the :attr:`input`\ntensor in the given dimension :attr:`dim`. The computation is numerically\nstabilized.\n\nFor summation index :math:`j` given by `dim` and other indices :math:`i`, the result is\n\n    .. math::\n        \\text{logsumexp}(x)_{i} = \\log \\sum_j \\exp(x_{ij})\n\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size\nas :attr:`input` except in the dimension(s) :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in the\noutput tensor having 1 (or ``len(dim)``) fewer dimension(s).\n\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int or tuple of ints): the dimension or dimensions to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    out (Tensor, optional): the output tensor\n\n\nExample::\n    >>> a = torch.randn(3, 3)\n    >>> torch.logsumexp(a, 1)\n    tensor([ 0.8442,  1.4322,  0.8711])\n'
        pass
    
    @classmethod
    def lstm(cls):
        pass
    
    @classmethod
    def lstm_cell(cls):
        pass
    
    @classmethod
    def lt(cls):
        '\nlt(input, other, out=None) -> Tensor\n\nComputes :math:`\\text{input} < \\text{other}` element-wise.\n\nThe second argument can be a number or a tensor whose shape is\n:ref:`broadcastable <broadcasting-semantics>` with the first argument.\n\nArgs:\n    input (Tensor): the tensor to compare\n    other (Tensor or float): the tensor or value to compare\n    out (Tensor, optional): the output tensor that must be a `ByteTensor`\n\nReturns:\n    Tensor: A `torch.ByteTensor` containing a 1 at each location where comparison is true\n\nExample::\n\n    >>> torch.lt(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))\n    tensor([[ 0,  0],\n            [ 1,  0]], dtype=torch.uint8)\n'
        pass
    
    @classmethod
    def lu_solve(cls):
        '\nlu_solve(b, LU_data, LU_pivots, out=None) -> Tensor\n\nBatch LU solve.\n\nReturns the LU solve of the linear system :math:`Ax = b` using the partially pivoted\nLU factorization of A from :meth:`torch.lu`.\n\nArguments:\n    b (Tensor): the RHS tensor\n    LU_data (Tensor): the pivoted LU factorization of A from :meth:`torch.lu`.\n    LU_pivots (IntTensor): the pivots of the LU factorization\n    out (Tensor, optional): the optional output tensor\n\nExample::\n\n    >>> A = torch.randn(2, 3, 3)\n    >>> b = torch.randn(2, 3)\n    >>> A_LU = torch.lu(A)\n    >>> x = torch.lu_solve(b, *A_LU)\n    >>> torch.norm(torch.bmm(A, x.unsqueeze(2)) - b.unsqueeze(2))\n    tensor(1.00000e-07 *\n           2.8312)\n'
        pass
    
    @classmethod
    def margin_ranking_loss(cls):
        pass
    
    @classmethod
    def masked_fill(cls):
        pass
    
    @classmethod
    def masked_scatter(cls):
        pass
    
    @classmethod
    def masked_select(cls):
        "\nmasked_select(input, mask, out=None) -> Tensor\n\nReturns a new 1-D tensor which indexes the :attr:`input` tensor according to\nthe binary mask :attr:`mask` which is a `ByteTensor`.\n\nThe shapes of the :attr:`mask` tensor and the :attr:`input` tensor don't need\nto match, but they must be :ref:`broadcastable <broadcasting-semantics>`.\n\n.. note:: The returned tensor does **not** use the same storage\n          as the original tensor\n\nArgs:\n    input (Tensor): the input data\n    mask  (ByteTensor): the tensor containing the binary mask to index with\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> x = torch.randn(3, 4)\n    >>> x\n    tensor([[ 0.3552, -2.3825, -0.8297,  0.3477],\n            [-1.2035,  1.2252,  0.5002,  0.6248],\n            [ 0.1307, -2.0608,  0.1244,  2.0139]])\n    >>> mask = x.ge(0.5)\n    >>> mask\n    tensor([[ 0,  0,  0,  0],\n            [ 0,  1,  1,  1],\n            [ 0,  0,  0,  1]], dtype=torch.uint8)\n    >>> torch.masked_select(x, mask)\n    tensor([ 1.2252,  0.5002,  0.6248,  2.0139])\n"
        pass
    
    @classmethod
    def matmul(cls):
        '\nmatmul(tensor1, tensor2, out=None) -> Tensor\n\nMatrix product of two tensors.\n\nThe behavior depends on the dimensionality of the tensors as follows:\n\n- If both tensors are 1-dimensional, the dot product (scalar) is returned.\n- If both arguments are 2-dimensional, the matrix-matrix product is returned.\n- If the first argument is 1-dimensional and the second argument is 2-dimensional,\n  a 1 is prepended to its dimension for the purpose of the matrix multiply.\n  After the matrix multiply, the prepended dimension is removed.\n- If the first argument is 2-dimensional and the second argument is 1-dimensional,\n  the matrix-vector product is returned.\n- If both arguments are at least 1-dimensional and at least one argument is\n  N-dimensional (where N > 2), then a batched matrix multiply is returned.  If the first\n  argument is 1-dimensional, a 1 is prepended to its dimension for the purpose of the\n  batched matrix multiply and removed after.  If the second argument is 1-dimensional, a\n  1 is appended to its dimension for the purpose of the batched matrix multiple and removed after.\n  The non-matrix (i.e. batch) dimensions are :ref:`broadcasted <broadcasting-semantics>` (and thus\n  must be broadcastable).  For example, if :attr:`tensor1` is a\n  :math:`(j \\times 1 \\times n \\times m)` tensor and :attr:`tensor2` is a :math:`(k \\times m \\times p)`\n  tensor, :attr:`out` will be an :math:`(j \\times k \\times n \\times p)` tensor.\n\n.. note::\n\n    The 1-dimensional dot product version of this function does not support an :attr:`out` parameter.\n\nArguments:\n    tensor1 (Tensor): the first tensor to be multiplied\n    tensor2 (Tensor): the second tensor to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> # vector x vector\n    >>> tensor1 = torch.randn(3)\n    >>> tensor2 = torch.randn(3)\n    >>> torch.matmul(tensor1, tensor2).size()\n    torch.Size([])\n    >>> # matrix x vector\n    >>> tensor1 = torch.randn(3, 4)\n    >>> tensor2 = torch.randn(4)\n    >>> torch.matmul(tensor1, tensor2).size()\n    torch.Size([3])\n    >>> # batched matrix x broadcasted vector\n    >>> tensor1 = torch.randn(10, 3, 4)\n    >>> tensor2 = torch.randn(4)\n    >>> torch.matmul(tensor1, tensor2).size()\n    torch.Size([10, 3])\n    >>> # batched matrix x batched matrix\n    >>> tensor1 = torch.randn(10, 3, 4)\n    >>> tensor2 = torch.randn(10, 4, 5)\n    >>> torch.matmul(tensor1, tensor2).size()\n    torch.Size([10, 3, 5])\n    >>> # batched matrix x broadcasted matrix\n    >>> tensor1 = torch.randn(10, 3, 4)\n    >>> tensor2 = torch.randn(4, 5)\n    >>> torch.matmul(tensor1, tensor2).size()\n    torch.Size([10, 3, 5])\n\n'
        pass
    
    @classmethod
    def matrix_power(cls):
        '\nmatrix_power(input, n) -> Tensor\n\nReturns the matrix raised to the power :attr:`n` for square matrices.\nFor batch of matrices, each individual matrix is raised to the power :attr:`n`.\n\nIf :attr:`n` is negative, then the inverse of the matrix (if invertible) is\nraised to the power :attr:`n`.  For a batch of matrices, the batched inverse\n(if invertible) is raised to the power :attr:`n`. If :attr:`n` is 0, then an identity matrix\nis returned.\n\nArgs:\n    input (Tensor): the input tensor\n    n (int): the power to raise the matrix to\n\nExample::\n\n    >>> a = torch.randn(2, 2, 2)\n    >>> a\n    tensor([[[-1.9975, -1.9610],\n             [ 0.9592, -2.3364]],\n\n            [[-1.2534, -1.3429],\n             [ 0.4153, -1.4664]]])\n    >>> torch.matrix_power(a, 3)\n    tensor([[[  3.9392, -23.9916],\n             [ 11.7357,  -0.2070]],\n\n            [[  0.2468,  -6.7168],\n             [  2.0774,  -0.8187]]])\n'
        pass
    
    @classmethod
    def matrix_rank(cls):
        '\nmatrix_rank(input, tol=None, bool symmetric=False) -> Tensor\n\nReturns the numerical rank of a 2-D tensor. The method to compute the\nmatrix rank is done using SVD by default. If :attr:`symmetric` is ``True``,\nthen :attr:`input` is assumed to be symmetric, and the computation of the\nrank is done by obtaining the eigenvalues.\n\n:attr:`tol` is the threshold below which the singular values (or the eigenvalues\nwhen :attr:`symmetric` is ``True``) are considered to be 0. If :attr:`tol` is not\nspecified, :attr:`tol` is set to ``S.max() * max(S.size()) * eps`` where `S` is the\nsingular values (or the eigenvalues when :attr:`symmetric` is ``True``), and ``eps``\nis the epsilon value for the datatype of :attr:`input`.\n\nArgs:\n    input (Tensor): the input 2-D tensor\n    tol (float, optional): the tolerance value. Default: ``None``\n    symmetric(bool, optional): indicates whether :attr:`input` is symmetric.\n                               Default: ``False``\n\nExample::\n\n    >>> a = torch.eye(10)\n    >>> torch.matrix_rank(a)\n    tensor(10)\n    >>> b = torch.eye(10)\n    >>> b[0, 0] = 0\n    >>> torch.matrix_rank(b)\n    tensor(9)\n'
        pass
    
    @classmethod
    def max(cls):
        "\n.. function:: max(input) -> Tensor\n\nReturns the maximum value of all elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[ 0.6763,  0.7445, -2.2369]])\n    >>> torch.max(a)\n    tensor(0.7445)\n\n.. function:: max(input, dim, keepdim=False, out=None) -> (Tensor, LongTensor)\n\nReturns a namedtuple ``(values, indices)`` where ``values`` is the maximum\nvalue of each row of the :attr:`input` tensor in the given dimension\n:attr:`dim`. And ``indices`` is the index location of each maximum value found\n(argmax).\n\nIf :attr:`keepdim` is ``True``, the output tensors are of the same size\nas :attr:`input` except in the dimension :attr:`dim` where they are of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting\nin the output tensors having 1 fewer dimension than :attr:`input`.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce\n    keepdim (bool, optional): whether the output tensors have :attr:`dim` retained or not. Default: ``False``.\n    out (tuple, optional): the result tuple of two output tensors (max, max_indices)\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[-1.2360, -0.2942, -0.1222,  0.8475],\n            [ 1.1949, -1.1127, -2.2379, -0.6702],\n            [ 1.5717, -0.9207,  0.1297, -1.8768],\n            [-0.6172,  1.0036, -0.6060, -0.2432]])\n    >>> torch.max(a, 1)\n    torch.return_types.max(values=tensor([0.8475, 1.1949, 1.5717, 1.0036]), indices=tensor([3, 0, 0, 1]))\n\n.. function:: max(input, other, out=None) -> Tensor\n\nEach element of the tensor :attr:`input` is compared with the corresponding\nelement of the tensor :attr:`other` and an element-wise maximum is taken.\n\nThe shapes of :attr:`input` and :attr:`other` don't need to match,\nbut they must be :ref:`broadcastable <broadcasting-semantics>`.\n\n.. math::\n    \\text{out}_i = \\max(\\text{tensor}_i, \\text{other}_i)\n\n.. note:: When the shapes do not match, the shape of the returned output tensor\n          follows the :ref:`broadcasting rules <broadcasting-semantics>`.\n\nArgs:\n    input (Tensor): the input tensor\n    other (Tensor): the second input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.2942, -0.7416,  0.2653, -0.1584])\n    >>> b = torch.randn(4)\n    >>> b\n    tensor([ 0.8722, -1.7421, -0.4141, -0.5055])\n    >>> torch.max(a, b)\n    tensor([ 0.8722, -0.7416,  0.2653, -0.1584])\n"
        pass
    
    @classmethod
    def max_pool1d(cls):
        pass
    
    @classmethod
    def max_pool1d_with_indices(cls):
        pass
    
    @classmethod
    def max_pool2d(cls):
        pass
    
    @classmethod
    def max_pool3d(cls):
        pass
    
    @classmethod
    def mean(cls):
        '\n.. function:: mean(input) -> Tensor\n\nReturns the mean value of all elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[ 0.2294, -0.5481,  1.3288]])\n    >>> torch.mean(a)\n    tensor(0.3367)\n\n.. function:: mean(input, dim, keepdim=False, out=None) -> Tensor\n\nReturns the mean value of each row of the :attr:`input` tensor in the given\ndimension :attr:`dim`. If :attr:`dim` is a list of dimensions,\nreduce over all of them.\n\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size\nas :attr:`input` except in the dimension(s) :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in the\noutput tensor having 1 (or ``len(dim)``) fewer dimension(s).\n\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int or tuple of ints): the dimension or dimensions to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    out (Tensor): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[-0.3841,  0.6320,  0.4254, -0.7384],\n            [-0.9644,  1.0131, -0.6549, -1.4279],\n            [-0.2951, -1.3350, -0.7694,  0.5600],\n            [ 1.0842, -0.9580,  0.3623,  0.2343]])\n    >>> torch.mean(a, 1)\n    tensor([-0.0163, -0.5085, -0.4599,  0.1807])\n    >>> torch.mean(a, 1, True)\n    tensor([[-0.0163],\n            [-0.5085],\n            [-0.4599],\n            [ 0.1807]])\n'
        pass
    
    @classmethod
    def median(cls):
        '\n.. function:: median(input) -> Tensor\n\nReturns the median value of all elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[ 1.5219, -1.5212,  0.2202]])\n    >>> torch.median(a)\n    tensor(0.2202)\n\n.. function:: median(input, dim=-1, keepdim=False, values=None, indices=None) -> (Tensor, LongTensor)\n\nReturns a namedtuple ``(values, indices)`` where ``values`` is the median\nvalue of each row of the :attr:`input` tensor in the given dimension\n:attr:`dim`. And ``indices`` is the index location of each median value found.\n\nBy default, :attr:`dim` is the last dimension of the :attr:`input` tensor.\n\nIf :attr:`keepdim` is ``True``, the output tensors are of the same size\nas :attr:`input` except in the dimension :attr:`dim` where they are of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in\nthe outputs tensor having 1 fewer dimension than :attr:`input`.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce\n    keepdim (bool): whether the output tensors have :attr:`dim` retained or not\n    values (Tensor, optional): the output tensor\n    indices (Tensor, optional): the output index tensor\n\nExample::\n\n    >>> a = torch.randn(4, 5)\n    >>> a\n    tensor([[ 0.2505, -0.3982, -0.9948,  0.3518, -1.3131],\n            [ 0.3180, -0.6993,  1.0436,  0.0438,  0.2270],\n            [-0.2751,  0.7303,  0.2192,  0.3321,  0.2488],\n            [ 1.0778, -1.9510,  0.7048,  0.4742, -0.7125]])\n    >>> torch.median(a, 1)\n    torch.return_types.median(values=tensor([-0.3982,  0.2270,  0.2488,  0.4742]), indices=tensor([1, 4, 4, 3]))\n'
        pass
    
    @classmethod
    def meshgrid(cls):
        pass
    
    @classmethod
    def min(cls):
        "\n.. function:: min(input) -> Tensor\n\nReturns the minimum value of all elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[ 0.6750,  1.0857,  1.7197]])\n    >>> torch.min(a)\n    tensor(0.6750)\n\n.. function:: min(input, dim, keepdim=False, out=None) -> (Tensor, LongTensor)\n\nReturns a namedtuple ``(values, indices)`` where ``values`` is the minimum\nvalue of each row of the :attr:`input` tensor in the given dimension\n:attr:`dim`. And ``indices`` is the index location of each minimum value found\n(argmin).\n\nIf :attr:`keepdim` is ``True``, the output tensors are of the same size as\n:attr:`input` except in the dimension :attr:`dim` where they are of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in\nthe output tensors having 1 fewer dimension than :attr:`input`.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce\n    keepdim (bool): whether the output tensors have :attr:`dim` retained or not\n    out (tuple, optional): the tuple of two output tensors (min, min_indices)\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[-0.6248,  1.1334, -1.1899, -0.2803],\n            [-1.4644, -0.2635, -0.3651,  0.6134],\n            [ 0.2457,  0.0384,  1.0128,  0.7015],\n            [-0.1153,  2.9849,  2.1458,  0.5788]])\n    >>> torch.min(a, 1)\n    torch.return_types.min(values=tensor([-1.1899, -1.4644,  0.0384, -0.1153]), indices=tensor([2, 0, 1, 0]))\n\n.. function:: min(input, other, out=None) -> Tensor\n\nEach element of the tensor :attr:`input` is compared with the corresponding\nelement of the tensor :attr:`other` and an element-wise minimum is taken.\nThe resulting tensor is returned.\n\nThe shapes of :attr:`input` and :attr:`other` don't need to match,\nbut they must be :ref:`broadcastable <broadcasting-semantics>`.\n\n.. math::\n    \\text{out}_i = \\min(\\text{tensor}_i, \\text{other}_i)\n\n.. note:: When the shapes do not match, the shape of the returned output tensor\n          follows the :ref:`broadcasting rules <broadcasting-semantics>`.\n\nArgs:\n    input (Tensor): the input tensor\n    other (Tensor): the second input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.8137, -1.1740, -0.6460,  0.6308])\n    >>> b = torch.randn(4)\n    >>> b\n    tensor([-0.1369,  0.1555,  0.4019, -0.1929])\n    >>> torch.min(a, b)\n    tensor([-0.1369, -1.1740, -0.6460, -0.1929])\n"
        pass
    
    @classmethod
    def miopen_batch_norm(cls):
        pass
    
    @classmethod
    def miopen_convolution(cls):
        pass
    
    @classmethod
    def miopen_convolution_transpose(cls):
        pass
    
    @classmethod
    def miopen_depthwise_convolution(cls):
        pass
    
    @classmethod
    def mkldnn_convolution(cls):
        pass
    
    @classmethod
    def mkldnn_convolution_backward_weights(cls):
        pass
    
    @classmethod
    def mkldnn_max_pool2d(cls):
        pass
    
    @classmethod
    def mkldnn_reshape(cls):
        pass
    
    @classmethod
    def mm(cls):
        '\nmm(mat1, mat2, out=None) -> Tensor\n\nPerforms a matrix multiplication of the matrices :attr:`mat1` and :attr:`mat2`.\n\nIf :attr:`mat1` is a :math:`(n \\times m)` tensor, :attr:`mat2` is a\n:math:`(m \\times p)` tensor, :attr:`out` will be a :math:`(n \\times p)` tensor.\n\n.. note:: This function does not :ref:`broadcast <broadcasting-semantics>`.\n          For broadcasting matrix products, see :func:`torch.matmul`.\n\nArgs:\n    mat1 (Tensor): the first matrix to be multiplied\n    mat2 (Tensor): the second matrix to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> mat1 = torch.randn(2, 3)\n    >>> mat2 = torch.randn(3, 3)\n    >>> torch.mm(mat1, mat2)\n    tensor([[ 0.4851,  0.5037, -0.3633],\n            [-0.0760, -3.6705,  2.4784]])\n'
        pass
    
    @classmethod
    def mode(cls):
        '\nmode(input, dim=-1, keepdim=False, values=None, indices=None) -> (Tensor, LongTensor)\n\nReturns a namedtuple ``(values, indices)`` where ``values`` is the mode\nvalue of each row of the :attr:`input` tensor in the given dimension\n:attr:`dim`, i.e. a value which appears most often\nin that row, and ``indices`` is the index location of each mode value found.\n\nBy default, :attr:`dim` is the last dimension of the :attr:`input` tensor.\n\nIf :attr:`keepdim` is ``True``, the output tensors are of the same size as\n:attr:`input` except in the dimension :attr:`dim` where they are of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting\nin the output tensors having 1 fewer dimension than :attr:`input`.\n\n.. note:: This function is not defined for ``torch.cuda.Tensor`` yet.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce\n    keepdim (bool): whether the output tensors have :attr:`dim` retained or not\n    values (Tensor, optional): the output tensor\n    indices (Tensor, optional): the output index tensor\n\nExample::\n\n    >>> a = torch.randint(10, (5,))\n    >>> a\n    tensor([6, 5, 1, 0, 2])\n    >>> b = a + (torch.randn(50, 1) * 5).long()\n    >>> torch.mode(b, 0)\n    torch.return_types.mode(values=tensor([6, 5, 1, 0, 2]), indices=tensor([2, 2, 2, 2, 2]))\n'
        pass
    
    @classmethod
    def mul(cls):
        '\n.. function:: mul(input, value, out=None)\n\nMultiplies each element of the input :attr:`input` with the scalar\n:attr:`value` and returns a new resulting tensor.\n\n.. math::\n    \\text{out}_i = \\text{value} \\times \\text{input}_i\n\nIf :attr:`input` is of type `FloatTensor` or `DoubleTensor`, :attr:`value`\nshould be a real number, otherwise it should be an integer\n\nArgs:\n    input (Tensor): the input tensor\n    value (Number): the number to be multiplied to each element of :attr:`input`\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(3)\n    >>> a\n    tensor([ 0.2015, -0.4255,  2.6087])\n    >>> torch.mul(a, 100)\n    tensor([  20.1494,  -42.5491,  260.8663])\n\n.. function:: mul(input, other, out=None)\n\nEach element of the tensor :attr:`input` is multiplied by the corresponding\nelement of the Tensor :attr:`other`. The resulting tensor is returned.\n\nThe shapes of :attr:`input` and :attr:`other` must be\n:ref:`broadcastable <broadcasting-semantics>`.\n\n.. math::\n    \\text{out}_i = \\text{input}_i \\times \\text{other}_i\n\nArgs:\n    input (Tensor): the first multiplicand tensor\n    other (Tensor): the second multiplicand tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 1)\n    >>> a\n    tensor([[ 1.1207],\n            [-0.3137],\n            [ 0.0700],\n            [ 0.8378]])\n    >>> b = torch.randn(1, 4)\n    >>> b\n    tensor([[ 0.5146,  0.1216, -0.5244,  2.2382]])\n    >>> torch.mul(a, b)\n    tensor([[ 0.5767,  0.1363, -0.5877,  2.5083],\n            [-0.1614, -0.0382,  0.1645, -0.7021],\n            [ 0.0360,  0.0085, -0.0367,  0.1567],\n            [ 0.4312,  0.1019, -0.4394,  1.8753]])\n'
        pass
    
    @classmethod
    def multinomial(cls):
        '\nmultinomial(input, num_samples, replacement=False, out=None) -> LongTensor\n\nReturns a tensor where each row contains :attr:`num_samples` indices sampled\nfrom the multinomial probability distribution located in the corresponding row\nof tensor :attr:`input`.\n\n.. note::\n    The rows of :attr:`input` do not need to sum to one (in which case we use\n    the values as weights), but must be non-negative, finite and have\n    a non-zero sum.\n\nIndices are ordered from left to right according to when each was sampled\n(first samples are placed in first column).\n\nIf :attr:`input` is a vector, :attr:`out` is a vector of size :attr:`num_samples`.\n\nIf :attr:`input` is a matrix with `m` rows, :attr:`out` is an matrix of shape\n:math:`(m \\times \\text{num\\_samples})`.\n\nIf replacement is ``True``, samples are drawn with replacement.\n\nIf not, they are drawn without replacement, which means that when a\nsample index is drawn for a row, it cannot be drawn again for that row.\n\n.. note::\n    When drawn without replacement, :attr:`num_samples` must be lower than\n    number of non-zero elements in :attr:`input` (or the min number of non-zero\n    elements in each row of :attr:`input` if it is a matrix).\n\nArgs:\n    input (Tensor): the input tensor containing probabilities\n    num_samples (int): number of samples to draw\n    replacement (bool, optional): whether to draw with replacement or not\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> weights = torch.tensor([0, 10, 3, 0], dtype=torch.float) # create a tensor of weights\n    >>> torch.multinomial(weights, 2)\n    tensor([1, 2])\n    >>> torch.multinomial(weights, 4) # ERROR!\n    RuntimeError: invalid argument 2: invalid multinomial distribution (with replacement=False,\n    not enough non-negative category to sample) at ../aten/src/TH/generic/THTensorRandom.cpp:320\n    >>> torch.multinomial(weights, 4, replacement=True)\n    tensor([ 2,  1,  1,  1])\n'
        pass
    
    @classmethod
    def mv(cls):
        '\nmv(mat, vec, out=None) -> Tensor\n\nPerforms a matrix-vector product of the matrix :attr:`mat` and the vector\n:attr:`vec`.\n\nIf :attr:`mat` is a :math:`(n \\times m)` tensor, :attr:`vec` is a 1-D tensor of\nsize :math:`m`, :attr:`out` will be 1-D of size :math:`n`.\n\n.. note:: This function does not :ref:`broadcast <broadcasting-semantics>`.\n\nArgs:\n    mat (Tensor): matrix to be multiplied\n    vec (Tensor): vector to be multiplied\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> mat = torch.randn(2, 3)\n    >>> vec = torch.randn(3)\n    >>> torch.mv(mat, vec)\n    tensor([ 1.0404, -0.6361])\n'
        pass
    
    @classmethod
    def mvlgamma(cls):
        '\nmvlgamma(input, p) -> Tensor\n\nComputes the multivariate log-gamma function (`[reference]`_) with dimension :math:`p` element-wise, given by\n\n.. math::\n    \\log(\\Gamma_{p}(a)) = C + \\displaystyle \\sum_{i=1}^{p} \\log\\left(\\Gamma\\left(a - \\frac{i - 1}{2}\\right)\\right)\n\nwhere :math:`C = \\log(\\pi) \\times \\frac{p (p - 1)}{4}` and :math:`\\Gamma(\\cdot)` is the Gamma function.\n\nIf any of the elements are less than or equal to :math:`\\frac{p - 1}{2}`, then an error\nis thrown.\n\nArgs:\n    input (Tensor): the tensor to compute the multivariate log-gamma function\n    p (int): the number of dimensions\n\nExample::\n\n    >>> a = torch.empty(2, 3).uniform_(1, 2)\n    >>> a\n    tensor([[1.6835, 1.8474, 1.1929],\n            [1.0475, 1.7162, 1.4180]])\n    >>> torch.mvlgamma(a, 2)\n    tensor([[0.3928, 0.4007, 0.7586],\n            [1.0311, 0.3901, 0.5049]])\n\n.. _`[reference]`: https://en.wikipedia.org/wiki/Multivariate_gamma_function\n'
        pass
    
    @classmethod
    def narrow(cls):
        '\nnarrow(input, dimension, start, length) -> Tensor\n\nReturns a new tensor that is a narrowed version of :attr:`input` tensor. The\ndimension :attr:`dim` is input from :attr:`start` to :attr:`start + length`. The\nreturned tensor and :attr:`input` tensor share the same underlying storage.\n\nArgs:\n    input (Tensor): the tensor to narrow\n    dimension (int): the dimension along which to narrow\n    start (int): the starting dimension\n    length (int): the distance to the ending dimension\n\nExample::\n\n    >>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n    >>> torch.narrow(x, 0, 0, 2)\n    tensor([[ 1,  2,  3],\n            [ 4,  5,  6]])\n    >>> torch.narrow(x, 1, 1, 2)\n    tensor([[ 2,  3],\n            [ 5,  6],\n            [ 8,  9]])\n'
        pass
    
    @classmethod
    def native_batch_norm(cls):
        pass
    
    @classmethod
    def native_norm(cls):
        pass
    
    @classmethod
    def ne(cls):
        '\nne(input, other, out=None) -> Tensor\n\nComputes :math:`input \\neq other` element-wise.\n\nThe second argument can be a number or a tensor whose shape is\n:ref:`broadcastable <broadcasting-semantics>` with the first argument.\n\nArgs:\n    input (Tensor): the tensor to compare\n    other (Tensor or float): the tensor or value to compare\n    out (Tensor, optional): the output tensor that must be a `ByteTensor`\n\nReturns:\n    Tensor: A ``torch.ByteTensor`` containing a 1 at each location where comparison is true.\n\nExample::\n\n    >>> torch.ne(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))\n    tensor([[ 0,  1],\n            [ 1,  0]], dtype=torch.uint8)\n'
        pass
    
    @classmethod
    def neg(cls):
        '\nneg(input, out=None) -> Tensor\n\nReturns a new tensor with the negative of the elements of :attr:`input`.\n\n.. math::\n    \\text{out} = -1 \\times \\text{input}\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(5)\n    >>> a\n    tensor([ 0.0090, -0.2262, -0.0682, -0.2866,  0.3940])\n    >>> torch.neg(a)\n    tensor([-0.0090,  0.2262,  0.0682,  0.2866, -0.3940])\n'
        pass
    
    @classmethod
    def neg_(cls):
        pass
    
    @classmethod
    def nonzero(cls):
        '\nnonzero(input, out=None) -> LongTensor\n\nReturns a tensor containing the indices of all non-zero elements of\n:attr:`input`.  Each row in the result contains the indices of a non-zero\nelement in :attr:`input`. The result is sorted lexicographically, with\nthe last index changing the fastest (C-style).\n\nIf :attr:`input` has `n` dimensions, then the resulting indices tensor\n:attr:`out` is of size :math:`(z \\times n)`, where :math:`z` is the total number of\nnon-zero elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n    out (LongTensor, optional): the output tensor containing indices\n\nExample::\n\n    >>> torch.nonzero(torch.tensor([1, 1, 1, 0, 1]))\n    tensor([[ 0],\n            [ 1],\n            [ 2],\n            [ 4]])\n    >>> torch.nonzero(torch.tensor([[0.6, 0.0, 0.0, 0.0],\n                                    [0.0, 0.4, 0.0, 0.0],\n                                    [0.0, 0.0, 1.2, 0.0],\n                                    [0.0, 0.0, 0.0,-0.4]]))\n    tensor([[ 0,  0],\n            [ 1,  1],\n            [ 2,  2],\n            [ 3,  3]])\n'
        pass
    
    @classmethod
    def norm(cls):
        pass
    
    @classmethod
    def norm_except_dim(cls):
        pass
    
    @classmethod
    def normal(cls):
        "\n.. function:: normal(mean, std, out=None) -> Tensor\n\nReturns a tensor of random numbers drawn from separate normal distributions\nwhose mean and standard deviation are given.\n\nThe :attr:`mean` is a tensor with the mean of\neach output element's normal distribution\n\nThe :attr:`std` is a tensor with the standard deviation of\neach output element's normal distribution\n\nThe shapes of :attr:`mean` and :attr:`std` don't need to match, but the\ntotal number of elements in each tensor need to be the same.\n\n.. note:: When the shapes do not match, the shape of :attr:`mean`\n          is used as the shape for the returned output tensor\n\nArgs:\n    mean (Tensor): the tensor of per-element means\n    std (Tensor): the tensor of per-element standard deviations\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.normal(mean=torch.arange(1., 11.), std=torch.arange(1, 0, -0.1))\n    tensor([  1.0425,   3.5672,   2.7969,   4.2925,   4.7229,   6.2134,\n              8.0505,   8.1408,   9.0563,  10.0566])\n\n.. function:: normal(mean=0.0, std, out=None) -> Tensor\n\nSimilar to the function above, but the means are shared among all drawn\nelements.\n\nArgs:\n    mean (float, optional): the mean for all distributions\n    std (Tensor): the tensor of per-element standard deviations\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.normal(mean=0.5, std=torch.arange(1., 6.))\n    tensor([-1.2793, -1.0732, -2.0687,  5.1177, -1.2303])\n\n.. function:: normal(mean, std=1.0, out=None) -> Tensor\n\nSimilar to the function above, but the standard-deviations are shared among\nall drawn elements.\n\nArgs:\n    mean (Tensor): the tensor of per-element means\n    std (float, optional): the standard deviation for all distributions\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.normal(mean=torch.arange(1., 6.))\n    tensor([ 1.1552,  2.6148,  2.6535,  5.8318,  4.2361])\n"
        pass
    
    @classmethod
    def nuclear_norm(cls):
        pass
    
    @classmethod
    def numel(cls):
        '\nnumel(input) -> int\n\nReturns the total number of elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> a = torch.randn(1, 2, 3, 4, 5)\n    >>> torch.numel(a)\n    120\n    >>> a = torch.zeros(4,4)\n    >>> torch.numel(a)\n    16\n\n'
        pass
    
    @classmethod
    def ones(cls):
        '\nones(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with the scalar value `1`, with the shape defined\nby the variable argument :attr:`sizes`.\n\nArgs:\n    sizes (int...): a sequence of integers defining the shape of the output tensor.\n        Can be a variable number of arguments or a collection like a list or tuple.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.ones(2, 3)\n    tensor([[ 1.,  1.,  1.],\n            [ 1.,  1.,  1.]])\n\n    >>> torch.ones(5)\n    tensor([ 1.,  1.,  1.,  1.,  1.])\n\n'
        pass
    
    @classmethod
    def ones_like(cls):
        '\nones_like(input, dtype=None, layout=None, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with the scalar value `1`, with the same size as\n:attr:`input`. ``torch.ones_like(input)`` is equivalent to\n``torch.ones(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)``.\n\n.. warning::\n    As of 0.4, this function does not support an :attr:`out` keyword. As an alternative,\n    the old ``torch.ones_like(input, out=output)`` is equivalent to\n    ``torch.ones(input.size(), out=output)``.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> input = torch.empty(2, 3)\n    >>> torch.ones_like(input)\n    tensor([[ 1.,  1.,  1.],\n            [ 1.,  1.,  1.]])\n'
        pass
    
    @classmethod
    def orgqr(cls):
        '\norgqr(a, tau) -> Tensor\n\nComputes the orthogonal matrix `Q` of a QR factorization, from the `(a, tau)`\ntuple returned by :func:`torch.geqrf`.\n\nThis directly calls the underlying LAPACK function `?orgqr`.\nSee `LAPACK documentation for orgqr`_ for further details.\n\nArgs:\n    a (Tensor): the `a` from :func:`torch.geqrf`.\n    tau (Tensor): the `tau` from :func:`torch.geqrf`.\n\n.. _LAPACK documentation for orgqr:\n    https://software.intel.com/en-us/mkl-developer-reference-c-orgqr\n\n'
        pass
    
    @classmethod
    def ormqr(cls):
        '\normqr(a, tau, mat, left=True, transpose=False) -> Tensor\n\nMultiplies `mat` by the orthogonal `Q` matrix of the QR factorization\nformed by :func:`torch.geqrf` that is represented by `(a, tau)`.\n\nThis directly calls the underlying LAPACK function `?ormqr`.\nSee `LAPACK documentation for ormqr`_ for further details.\n\nArgs:\n    a (Tensor): the `a` from :func:`torch.geqrf`.\n    tau (Tensor): the `tau` from :func:`torch.geqrf`.\n    mat (Tensor): the matrix to be multiplied.\n\n.. _LAPACK documentation for ormqr:\n    https://software.intel.com/en-us/mkl-developer-reference-c-ormqr\n\n'
        pass
    
    @classmethod
    def pairwise_distance(cls):
        pass
    
    @classmethod
    def pdist(cls):
        "\npdist(input, p=2) -> Tensor\n\nComputes the p-norm distance between every pair of row vectors in the input.\nThis is identical to the upper triangular portion, excluding the diagonal, of\n`torch.norm(input[:, None] - input, dim=2, p=p)`. This function will be faster\nif the rows are contiguous.\n\nIf input has shape :math:`N \\times M` then the output will have shape\n:math:`\\frac{1}{2} N (N - 1)`.\n\nThis function is equivalent to `scipy.spatial.distance.pdist(input,\n'minkowski', p=p)` if :math:`p \\in (0, \\infty)`. When :math:`p = 0` it is\nequivalent to `scipy.spatial.distance.pdist(input, 'hamming') * M`.\nWhen :math:`p = \\infty`, the closest scipy function is\n`scipy.spatial.distance.pdist(xn, lambda x, y: np.abs(x - y).max())`.\n\nArgs:\n    input: input tensor of shape :math:`N \\times M`.\n    p: p value for the p-norm distance to calculate between each vector pair\n        :math:`\\in [0, \\infty]`.\n"
        pass
    
    @classmethod
    def pin_memory(cls):
        pass
    
    @classmethod
    def pinverse(cls):
        '\npinverse(input, rcond=1e-15) -> Tensor\n\nCalculates the pseudo-inverse (also known as the Moore-Penrose inverse) of a 2D tensor.\nPlease look at `Moore-Penrose inverse`_ for more details\n\n.. note::\n    This method is implemented using the Singular Value Decomposition.\n\n.. note::\n    The pseudo-inverse is not necessarily a continuous function in the elements of the matrix `[1]`_.\n    Therefore, derivatives are not always existent, and exist for a constant rank only `[2]`_.\n    However, this method is backprop-able due to the implementation by using SVD results, and\n    could be unstable. Double-backward will also be unstable due to the usage of SVD internally.\n    See :meth:`~torch.svd` for more details.\n\nArguments:\n    input (Tensor): The input 2D tensor of dimensions :math:`m \\times n`\n    rcond (float): A floating point value to determine the cutoff for small singular values.\n                   Default: 1e-15\n\nReturns:\n    The pseudo-inverse of :attr:`input` of dimensions :math:`n \\times m`\n\nExample::\n\n    >>> input = torch.randn(3, 5)\n    >>> input\n    tensor([[ 0.5495,  0.0979, -1.4092, -0.1128,  0.4132],\n            [-1.1143, -0.3662,  0.3042,  1.6374, -0.9294],\n            [-0.3269, -0.5745, -0.0382, -0.5922, -0.6759]])\n    >>> torch.pinverse(input)\n    tensor([[ 0.0600, -0.1933, -0.2090],\n            [-0.0903, -0.0817, -0.4752],\n            [-0.7124, -0.1631, -0.2272],\n            [ 0.1356,  0.3933, -0.5023],\n            [-0.0308, -0.1725, -0.5216]])\n\n.. _Moore-Penrose inverse: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse\n\n.. _[1]: https://epubs.siam.org/doi/10.1137/0117004\n\n.. _[2]: https://www.jstor.org/stable/2156365\n'
        pass
    
    @classmethod
    def pixel_shuffle(cls):
        '\nRearranges elements in a tensor of shape :math:`(*, C \\times r^2, H, W)` to a\ntensor of shape :math:`(*, C, H \\times r, W \\times r)`.\n\nSee :class:`~torch.nn.PixelShuffle` for details.\n\nArgs:\n    input (Tensor): the input tensor\n    upscale_factor (int): factor to increase spatial resolution by\n\nExamples::\n\n    >>> input = torch.randn(1, 9, 4, 4)\n    >>> output = torch.nn.functional.pixel_shuffle(input, 3)\n    >>> print(output.size())\n    torch.Size([1, 1, 12, 12])\n'
        pass
    
    @classmethod
    def poisson(cls):
        pass
    
    @classmethod
    def polygamma(cls):
        pass
    
    @classmethod
    def pow(cls):
        '\n.. function:: pow(input, exponent, out=None) -> Tensor\n\nTakes the power of each element in :attr:`input` with :attr:`exponent` and\nreturns a tensor with the result.\n\n:attr:`exponent` can be either a single ``float`` number or a `Tensor`\nwith the same number of elements as :attr:`input`.\n\nWhen :attr:`exponent` is a scalar value, the operation applied is:\n\n.. math::\n    \\text{out}_i = x_i ^ \\text{exponent}\n\nWhen :attr:`exponent` is a tensor, the operation applied is:\n\n.. math::\n    \\text{out}_i = x_i ^ {\\text{exponent}_i}\n\nWhen :attr:`exponent` is a tensor, the shapes of :attr:`input`\nand :attr:`exponent` must be :ref:`broadcastable <broadcasting-semantics>`.\n\nArgs:\n    input (Tensor): the input tensor\n    exponent (float or tensor): the exponent value\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.4331,  1.2475,  0.6834, -0.2791])\n    >>> torch.pow(a, 2)\n    tensor([ 0.1875,  1.5561,  0.4670,  0.0779])\n    >>> exp = torch.arange(1., 5.)\n\n    >>> a = torch.arange(1., 5.)\n    >>> a\n    tensor([ 1.,  2.,  3.,  4.])\n    >>> exp\n    tensor([ 1.,  2.,  3.,  4.])\n    >>> torch.pow(a, exp)\n    tensor([   1.,    4.,   27.,  256.])\n\n.. function:: pow(base, input, out=None) -> Tensor\n\n:attr:`base` is a scalar ``float`` value, and :attr:`input` is a tensor.\nThe returned tensor :attr:`out` is of the same shape as :attr:`input`\n\nThe operation applied is:\n\n.. math::\n    out_i = base ^ {input_i}\n\nArgs:\n    base (float): the scalar base value for the power operation\n    input (Tensor): the exponent tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> exp = torch.arange(1., 5.)\n    >>> base = 2\n    >>> torch.pow(base, exp)\n    tensor([  2.,   4.,   8.,  16.])\n'
        pass
    
    @classmethod
    def prelu(cls):
        pass
    
    @classmethod
    def prod(cls):
        '\n.. function:: prod(input, dtype=None) -> Tensor\n\nReturns the product of all elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        If specified, the input tensor is casted to :attr:`dtype` before the operation\n        is performed. This is useful for preventing data type overflows. Default: None.\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[-0.8020,  0.5428, -1.5854]])\n    >>> torch.prod(a)\n    tensor(0.6902)\n\n.. function:: prod(input, dim, keepdim=False, dtype=None) -> Tensor\n\nReturns the product of each row of the :attr:`input` tensor in the given\ndimension :attr:`dim`.\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size\nas :attr:`input` except in the dimension :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in\nthe output tensor having 1 fewer dimension than :attr:`input`.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the dimension to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        If specified, the input tensor is casted to :attr:`dtype` before the operation\n        is performed. This is useful for preventing data type overflows. Default: None.\n\nExample::\n\n    >>> a = torch.randn(4, 2)\n    >>> a\n    tensor([[ 0.5261, -0.3837],\n            [ 1.1857, -0.2498],\n            [-1.1646,  0.0705],\n            [ 1.1131, -1.0629]])\n    >>> torch.prod(a, 1)\n    tensor([-0.2018, -0.2962, -0.0821, -1.1831])\n'
        pass
    
    @classmethod
    def pstrf(cls):
        pass
    
    @classmethod
    def q_scale(cls):
        pass
    
    @classmethod
    def q_zero_point(cls):
        pass
    
    @classmethod
    def qr(cls):
        '\nqr(input, out=None) -> (Tensor, Tensor)\n\nComputes the QR decomposition of a matrix :attr:`input`, and returns a namedtuple\n(Q, R) of matrices such that :math:`\\text{input} = Q R`, with :math:`Q` being an\northogonal matrix and :math:`R` being an upper triangular matrix.\n\nThis returns the thin (reduced) QR factorization.\n\n.. note:: precision may be lost if the magnitudes of the elements of :attr:`input`\n          are large\n\n.. note:: While it should always give you a valid decomposition, it may not\n          give you the same one across platforms - it will depend on your\n          LAPACK implementation.\n\n.. note:: Irrespective of the original strides, the returned matrix :math:`Q` will be\n          transposed, i.e. with strides `(1, m)` instead of `(m, 1)`.\n\nArgs:\n    input (Tensor): the input 2-D tensor\n    out (tuple, optional): tuple of `Q` and `R` tensors\n\nExample::\n\n    >>> a = torch.tensor([[12., -51, 4], [6, 167, -68], [-4, 24, -41]])\n    >>> q, r = torch.qr(a)\n    >>> q\n    tensor([[-0.8571,  0.3943,  0.3314],\n            [-0.4286, -0.9029, -0.0343],\n            [ 0.2857, -0.1714,  0.9429]])\n    >>> r\n    tensor([[ -14.0000,  -21.0000,   14.0000],\n            [   0.0000, -175.0000,   70.0000],\n            [   0.0000,    0.0000,  -35.0000]])\n    >>> torch.mm(q, r).round()\n    tensor([[  12.,  -51.,    4.],\n            [   6.,  167.,  -68.],\n            [  -4.,   24.,  -41.]])\n    >>> torch.mm(q.t(), q).round()\n    tensor([[ 1.,  0.,  0.],\n            [ 0.,  1., -0.],\n            [ 0., -0.,  1.]])\n'
        pass
    
    @classmethod
    def quantize_linear(cls):
        pass
    
    @classmethod
    def quantized_gru_cell(cls):
        pass
    
    @classmethod
    def quantized_lstm(cls):
        pass
    
    @classmethod
    def quantized_lstm_cell(cls):
        pass
    
    @classmethod
    def quantized_rnn_relu_cell(cls):
        pass
    
    @classmethod
    def quantized_rnn_tanh_cell(cls):
        pass
    
    @classmethod
    def rand(cls):
        '\nrand(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with random numbers from a uniform distribution\non the interval :math:`[0, 1)`\n\nThe shape of the tensor is defined by the variable argument :attr:`sizes`.\n\nArgs:\n    sizes (int...): a sequence of integers defining the shape of the output tensor.\n        Can be a variable number of arguments or a collection like a list or tuple.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.rand(4)\n    tensor([ 0.5204,  0.2503,  0.3525,  0.5673])\n    >>> torch.rand(2, 3)\n    tensor([[ 0.8237,  0.5781,  0.6879],\n            [ 0.3816,  0.7249,  0.0998]])\n'
        pass
    
    @classmethod
    def rand_like(cls):
        '\nrand_like(input, dtype=None, layout=None, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor with the same size as :attr:`input` that is filled with\nrandom numbers from a uniform distribution on the interval :math:`[0, 1)`.\n``torch.rand_like(input)`` is equivalent to\n``torch.rand(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)``.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\n'
        pass
    
    @classmethod
    def randint(cls):
        '\nrandint(low=0, high, size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with random integers generated uniformly\nbetween :attr:`low` (inclusive) and :attr:`high` (exclusive).\n\nThe shape of the tensor is defined by the variable argument :attr:`size`.\n\n.. note:\n    With the global dtype default (`torch.float32`), this function returns\n    a tensor with dtype `torch.int64`.\n\nArgs:\n    low (int, optional): Lowest integer to be drawn from the distribution. Default: 0.\n    high (int): One above the highest integer to be drawn from the distribution.\n    size (tuple): a tuple defining the shape of the output tensor.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.randint(3, 5, (3,))\n    tensor([4, 3, 4])\n\n\n    >>> torch.randint(10, (2, 2))\n    tensor([[0, 2],\n            [5, 5]])\n\n\n    >>> torch.randint(3, 10, (2, 2))\n    tensor([[4, 5],\n            [6, 7]])\n\n\n'
        pass
    
    @classmethod
    def randint_like(cls):
        '\nrandint_like(input, low=0, high, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor with the same shape as Tensor :attr:`input` filled with\nrandom integers generated uniformly between :attr:`low` (inclusive) and\n:attr:`high` (exclusive).\n\n.. note:\n    With the global dtype default (`torch.float32`), this function returns\n    a tensor with dtype `torch.int64`.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    low (int, optional): Lowest integer to be drawn from the distribution. Default: 0.\n    high (int): One above the highest integer to be drawn from the distribution.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\n'
        pass
    
    @classmethod
    def randn(cls):
        '\nrandn(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with random numbers from a normal distribution\nwith mean `0` and variance `1` (also called the standard normal\ndistribution).\n\n.. math::\n    \\text{out}_{i} \\sim \\mathcal{N}(0, 1)\n\nThe shape of the tensor is defined by the variable argument :attr:`sizes`.\n\nArgs:\n    sizes (int...): a sequence of integers defining the shape of the output tensor.\n        Can be a variable number of arguments or a collection like a list or tuple.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.randn(4)\n    tensor([-2.1436,  0.9966,  2.3426, -0.6366])\n    >>> torch.randn(2, 3)\n    tensor([[ 1.5954,  2.8929, -1.0923],\n            [ 1.1719, -0.4709, -0.1996]])\n'
        pass
    
    @classmethod
    def randn_like(cls):
        '\nrandn_like(input, dtype=None, layout=None, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor with the same size as :attr:`input` that is filled with\nrandom numbers from a normal distribution with mean 0 and variance 1.\n``torch.randn_like(input)`` is equivalent to\n``torch.randn(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)``.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\n'
        pass
    
    @classmethod
    def randperm(cls):
        '\nrandperm(n, out=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False) -> LongTensor\n\nReturns a random permutation of integers from ``0`` to ``n - 1``.\n\nArgs:\n    n (int): the upper bound (exclusive)\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: ``torch.int64``.\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.randperm(4)\n    tensor([2, 1, 0, 3])\n'
        pass
    
    @classmethod
    def range(cls):
        '\nrange(start=0, end, step=1, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a 1-D tensor of size :math:`\\left\\lfloor \\frac{\\text{end} - \\text{start}}{\\text{step}} \\right\\rfloor + 1`\nwith values from :attr:`start` to :attr:`end` with step :attr:`step`. Step is\nthe gap between two values in the tensor.\n\n.. math::\n    \\text{out}_{i+1} = \\text{out}_i + \\text{step}.\n\n.. warning::\n    This function is deprecated in favor of :func:`torch.arange`.\n\nArgs:\n    start (float): the starting value for the set of points. Default: ``0``.\n    end (float): the ending value for the set of points\n    step (float): the gap between each pair of adjacent points. Default: ``1``.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`). If `dtype` is not given, infer the data type from the other input\n        arguments. If any of `start`, `end`, or `stop` are floating-point, the\n        `dtype` is inferred to be the default dtype, see\n        :meth:`~torch.get_default_dtype`. Otherwise, the `dtype` is inferred to\n        be `torch.int64`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.range(1, 4)\n    tensor([ 1.,  2.,  3.,  4.])\n    >>> torch.range(1, 4, 0.5)\n    tensor([ 1.0000,  1.5000,  2.0000,  2.5000,  3.0000,  3.5000,  4.0000])\n'
        pass
    
    @classmethod
    def reciprocal(cls):
        '\nreciprocal(input, out=None) -> Tensor\n\nReturns a new tensor with the reciprocal of the elements of :attr:`input`\n\n.. math::\n    \\text{out}_{i} = \\frac{1}{\\text{input}_{i}}\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.4595, -2.1219, -1.4314,  0.7298])\n    >>> torch.reciprocal(a)\n    tensor([-2.1763, -0.4713, -0.6986,  1.3702])\n'
        pass
    
    @classmethod
    def reciprocal_(cls):
        pass
    
    @classmethod
    def relu(cls):
        pass
    
    @classmethod
    def relu_(cls):
        '\nrelu_(input) -> Tensor\n\nIn-place version of :func:`~relu`.\n'
        pass
    
    @classmethod
    def remainder(cls):
        '\nremainder(input, divisor, out=None) -> Tensor\n\nComputes the element-wise remainder of division.\n\nThe divisor and dividend may contain both for integer and floating point\nnumbers. The remainder has the same sign as the divisor.\n\nWhen :attr:`divisor` is a tensor, the shapes of :attr:`input` and\n:attr:`divisor` must be :ref:`broadcastable <broadcasting-semantics>`.\n\nArgs:\n    input (Tensor): the dividend\n    divisor (Tensor or float): the divisor that may be either a number or a\n                               Tensor of the same shape as the dividend\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> torch.remainder(torch.tensor([-3., -2, -1, 1, 2, 3]), 2)\n    tensor([ 1.,  0.,  1.,  1.,  0.,  1.])\n    >>> torch.remainder(torch.tensor([1., 2, 3, 4, 5]), 1.5)\n    tensor([ 1.0000,  0.5000,  0.0000,  1.0000,  0.5000])\n\n.. seealso::\n\n        :func:`torch.fmod`, which computes the element-wise remainder of\n        division equivalently to the C library function ``fmod()``.\n'
        pass
    
    @classmethod
    def renorm(cls):
        '\nrenorm(input, p, dim, maxnorm, out=None) -> Tensor\n\nReturns a tensor where each sub-tensor of :attr:`input` along dimension\n:attr:`dim` is normalized such that the `p`-norm of the sub-tensor is lower\nthan the value :attr:`maxnorm`\n\n.. note:: If the norm of a row is lower than `maxnorm`, the row is unchanged\n\nArgs:\n    input (Tensor): the input tensor\n    p (float): the power for the norm computation\n    dim (int): the dimension to slice over to get the sub-tensors\n    maxnorm (float): the maximum norm to keep each sub-tensor under\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> x = torch.ones(3, 3)\n    >>> x[1].fill_(2)\n    tensor([ 2.,  2.,  2.])\n    >>> x[2].fill_(3)\n    tensor([ 3.,  3.,  3.])\n    >>> x\n    tensor([[ 1.,  1.,  1.],\n            [ 2.,  2.,  2.],\n            [ 3.,  3.,  3.]])\n    >>> torch.renorm(x, 1, 0, 5)\n    tensor([[ 1.0000,  1.0000,  1.0000],\n            [ 1.6667,  1.6667,  1.6667],\n            [ 1.6667,  1.6667,  1.6667]])\n'
        pass
    
    @classmethod
    def repeat_interleave(cls):
        '\n.. function:: repeat_interleave(input, repeats, dim=None) -> Tensor\n\nRepeat elements of a tensor.\n\n.. warning::\n\n    This is different from :func:`torch.repeat` but similar to `numpy.repeat`.\n\nArgs:\n    input (Tensor): The input tensor\n    repeats (Tensor or int): The number of repetitions for each element.\n        repeats is broadcasted to fit the shape of the given axis.\n    dim (int, optional): The dimension along which to repeat values.\n        By default, use the flattened input array, and return a flat output\n        array.\n\nReturns:\n    Tensor: Repeated tensor which has the same shape as input, except along the\n     given axis.\n\nExample::\n\n    >>> x = torch.tensor([1, 2, 3])\n    >>> x.repeat_interleave(2)\n    tensor([1, 1, 2, 2, 3, 3])\n    >>> y = torch.tensor([[1, 2], [3, 4]])\n    >>> torch.repeat_interleave(y, 2)\n    tensor([1, 1, 2, 2, 3, 3, 4, 4])\n    >>> torch.repeat_interleave(y, 3, dim=1)\n    tensor([[1, 1, 1, 2, 2, 2],\n            [3, 3, 3, 4, 4, 4]])\n    >>> torch.repeat_interleave(y, torch.tensor([1, 2]), dim=0)\n    tensor([[1, 2],\n            [3, 4],\n            [3, 4]])\n\n.. function:: repeat_interleave(repeats) -> Tensor\n\nIf the `repeats` is `tensor([n1, n2, n3, ...])`, then the output will be\n`tensor([0, 0, ..., 1, 1, ..., 2, 2, ..., ...])` where `0` appears `n1` times,\n`1` appears `n2` times, `2` appears `n3` times, etc.\n'
        pass
    
    @classmethod
    def reshape(cls):
        "\nreshape(input, shape) -> Tensor\n\nReturns a tensor with the same data and number of elements as :attr:`input`,\nbut with the specified shape. When possible, the returned tensor will be a view\nof :attr:`input`. Otherwise, it will be a copy. Contiguous inputs and inputs\nwith compatible strides can be reshaped without copying, but you should not\ndepend on the copying vs. viewing behavior.\n\nSee :meth:`torch.Tensor.view` on when it is possible to return a view.\n\nA single dimension may be -1, in which case it's inferred from the remaining\ndimensions and the number of elements in :attr:`input`.\n\nArgs:\n    input (Tensor): the tensor to be reshaped\n    shape (tuple of ints): the new shape\n\nExample::\n\n    >>> a = torch.arange(4.)\n    >>> torch.reshape(a, (2, 2))\n    tensor([[ 0.,  1.],\n            [ 2.,  3.]])\n    >>> b = torch.tensor([[0, 1], [2, 3]])\n    >>> torch.reshape(b, (-1,))\n    tensor([ 0,  1,  2,  3])\n"
        pass
    
    @classmethod
    def resize_as_(cls):
        pass
    
    @classmethod
    def rfft(cls):
        '\nrfft(input, signal_ndim, normalized=False, onesided=True) -> Tensor\n\nReal-to-complex Discrete Fourier Transform\n\nThis method computes the real-to-complex discrete Fourier transform. It is\nmathematically equivalent with :func:`~torch.fft` with differences only in\nformats of the input and output.\n\nThis method supports 1D, 2D and 3D real-to-complex transforms, indicated\nby :attr:`signal_ndim`. :attr:`input` must be a tensor with at least\n``signal_ndim`` dimensions with optionally arbitrary number of leading batch\ndimensions. If :attr:`normalized` is set to ``True``, this normalizes the result\nby dividing it with :math:`\\sqrt{\\prod_{i=1}^K N_i}` so that the operator is\nunitary, where :math:`N_i` is the size of signal dimension :math:`i`.\n\nThe real-to-complex Fourier transform results follow conjugate symmetry:\n\n.. math::\n    X[\\omega_1, \\dots, \\omega_d] = X^*[N_1 - \\omega_1, \\dots, N_d - \\omega_d],\n\nwhere the index arithmetic is computed modulus the size of the corresponding\ndimension, :math:`\\ ^*` is the conjugate operator, and\n:math:`d` = :attr:`signal_ndim`. :attr:`onesided` flag controls whether to avoid\nredundancy in the output results. If set to ``True`` (default), the output will\nnot be full complex result of shape :math:`(*, 2)`, where :math:`*` is the shape\nof :attr:`input`, but instead the last dimension will be halfed as of size\n:math:`\\lfloor \\frac{N_d}{2} \\rfloor + 1`.\n\nThe inverse of this function is :func:`~torch.irfft`.\n\n.. note::\n    For CUDA tensors, an LRU cache is used for cuFFT plans to speed up\n    repeatedly running FFT methods on tensors of same geometry with same\n    configuration. See :ref:`cufft-plan-cache` for more details on how to\n    monitor and control the cache.\n\n.. warning::\n    For CPU tensors, this method is currently only available with MKL. Use\n    :func:`torch.backends.mkl.is_available` to check if MKL is installed.\n\nArguments:\n    input (Tensor): the input tensor of at least :attr:`signal_ndim` dimensions\n    signal_ndim (int): the number of dimensions in each signal.\n        :attr:`signal_ndim` can only be 1, 2 or 3\n    normalized (bool, optional): controls whether to return normalized results.\n        Default: ``False``\n    onesided (bool, optional): controls whether to return half of results to\n        avoid redundancy. Default: ``True``\n\nReturns:\n    Tensor: A tensor containing the real-to-complex Fourier transform result\n\nExample::\n\n    >>> x = torch.randn(5, 5)\n    >>> torch.rfft(x, 2).shape\n    torch.Size([5, 3, 2])\n    >>> torch.rfft(x, 2, onesided=False).shape\n    torch.Size([5, 5, 2])\n\n'
        pass
    
    @classmethod
    def rnn_relu(cls):
        pass
    
    @classmethod
    def rnn_relu_cell(cls):
        pass
    
    @classmethod
    def rnn_tanh(cls):
        pass
    
    @classmethod
    def rnn_tanh_cell(cls):
        pass
    
    @classmethod
    def roll(cls):
        '\nroll(input, shifts, dims=None) -> Tensor\n\nRoll the tensor along the given dimension(s). Elements that are shifted beyond the\nlast position are re-introduced at the first position. If a dimension is not\nspecified, the tensor will be flattened before rolling and then restored\nto the original shape.\n\nArgs:\n    input (Tensor): the input tensor\n    shifts (int or tuple of ints): The number of places by which the elements\n        of the tensor are shifted. If shifts is a tuple, dims must be a tuple of\n        the same size, and each dimension will be rolled by the corresponding\n        value\n    dims (int or tuple of ints): Axis along which to roll\n\nExample::\n\n    >>> x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8]).view(4, 2)\n    >>> x\n    tensor([[1, 2],\n            [3, 4],\n            [5, 6],\n            [7, 8]])\n    >>> torch.roll(x, 1, 0)\n    tensor([[7, 8],\n            [1, 2],\n            [3, 4],\n            [5, 6]])\n    >>> torch.roll(x, -1, 0)\n    tensor([[3, 4],\n            [5, 6],\n            [7, 8],\n            [1, 2]])\n    >>> torch.roll(x, shifts=(2, 1), dims=(0, 1))\n    tensor([[6, 5],\n            [8, 7],\n            [2, 1],\n            [4, 3]])\n'
        pass
    
    @classmethod
    def rot90(cls):
        '\nrot90(input, k, dims) -> Tensor\n\nRotate a n-D tensor by 90 degrees in the plane specified by dims axis.\nRotation direction is from the first towards the second axis if k > 0, and from the second towards the first for k < 0.\n\nArgs:\n    input (Tensor): the input tensor\n    k (int): number of times to rotate\n    dims (a list or tuple): axis to rotate\n\nExample::\n\n    >>> x = torch.arange(4).view(2, 2)\n    >>> x\n    tensor([[0, 1],\n            [2, 3]])\n    >>> torch.rot90(x, 1, [0, 1])\n    tensor([[1, 3],\n            [0, 2]])\n\n    >>> x = torch.arange(8).view(2, 2, 2)\n    >>> x\n    tensor([[[0, 1],\n             [2, 3]],\n\n            [[4, 5],\n             [6, 7]]])\n    >>> torch.rot90(x, 1, [1, 2])\n    tensor([[[1, 3],\n             [0, 2]],\n\n            [[5, 7],\n             [4, 6]]])\n'
        pass
    
    @classmethod
    def round(cls):
        '\nround(input, out=None) -> Tensor\n\nReturns a new tensor with each of the elements of :attr:`input` rounded\nto the closest integer.\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.9920,  0.6077,  0.9734, -1.0362])\n    >>> torch.round(a)\n    tensor([ 1.,  1.,  1., -1.])\n'
        pass
    
    @classmethod
    def round_(cls):
        pass
    
    @classmethod
    def rrelu(cls):
        pass
    
    @classmethod
    def rrelu_(cls):
        '\nrrelu_(input, lower=1./8, upper=1./3, training=False) -> Tensor\n\nIn-place version of :func:`~rrelu`.\n'
        pass
    
    @classmethod
    def rsqrt(cls):
        '\nrsqrt(input, out=None) -> Tensor\n\nReturns a new tensor with the reciprocal of the square-root of each of\nthe elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\frac{1}{\\sqrt{\\text{input}_{i}}}\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.0370,  0.2970,  1.5420, -0.9105])\n    >>> torch.rsqrt(a)\n    tensor([    nan,  1.8351,  0.8053,     nan])\n'
        pass
    
    @classmethod
    def rsqrt_(cls):
        pass
    
    @classmethod
    def rsub(cls):
        pass
    
    @classmethod
    def s_copy_(cls):
        pass
    
    @classmethod
    def s_native_addmm(cls):
        pass
    
    @classmethod
    def s_native_addmm_(cls):
        pass
    
    @classmethod
    def saddmm(cls):
        pass
    
    @classmethod
    def scalar_tensor(cls):
        pass
    
    @classmethod
    def scatter(cls):
        pass
    
    @classmethod
    def scatter_add(cls):
        pass
    
    @classmethod
    def select(cls):
        pass
    
    @classmethod
    def selu(cls):
        pass
    
    @classmethod
    def selu_(cls):
        '\nselu_(input) -> Tensor\n\nIn-place version of :func:`~selu`.\n'
        pass
    
    @classmethod
    def sigmoid(cls):
        '\nsigmoid(input, out=None) -> Tensor\n\nReturns a new tensor with the sigmoid of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\frac{1}{1 + e^{-\\text{input}_{i}}}\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.9213,  1.0887, -0.8858, -1.7683])\n    >>> torch.sigmoid(a)\n    tensor([ 0.7153,  0.7481,  0.2920,  0.1458])\n'
        pass
    
    @classmethod
    def sigmoid_(cls):
        pass
    
    @classmethod
    def sign(cls):
        '\nsign(input, out=None) -> Tensor\n\nReturns a new tensor with the sign of the elements of :attr:`input`.\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.tensor([0.7, -1.2, 0., 2.3])\n    >>> a\n    tensor([ 0.7000, -1.2000,  0.0000,  2.3000])\n    >>> torch.sign(a)\n    tensor([ 1., -1.,  0.,  1.])\n'
        pass
    
    @classmethod
    def sin(cls):
        '\nsin(input, out=None) -> Tensor\n\nReturns a new tensor with the sine of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\sin(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-0.5461,  0.1347, -2.7266, -0.2746])\n    >>> torch.sin(a)\n    tensor([-0.5194,  0.1343, -0.4032, -0.2711])\n'
        pass
    
    @classmethod
    def sin_(cls):
        pass
    
    @classmethod
    def sinh(cls):
        '\nsinh(input, out=None) -> Tensor\n\nReturns a new tensor with the hyperbolic sine of the elements of\n:attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\sinh(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.5380, -0.8632, -0.1265,  0.9399])\n    >>> torch.sinh(a)\n    tensor([ 0.5644, -0.9744, -0.1268,  1.0845])\n'
        pass
    
    @classmethod
    def sinh_(cls):
        pass
    
    @classmethod
    def slogdet(cls):
        "\nslogdet(A) -> (Tensor, Tensor)\n\nCalculates the sign and log value of a 2D square tensor's determinant.\n\n.. note::\n    If ``A`` has zero determinant, this returns ``(0, -inf)``.\n\n.. note::\n    Backward through :meth:`slogdet` internally uses SVD results when :attr:`A`\n    is not invertible. In this case, double backward through :meth:`slogdet`\n    will be unstable in when :attr:`A` doesn't have distinct singular values.\n    See :meth:`~torch.svd` for details.\n\nArguments:\n    A (Tensor): The input 2D square tensor\n\nReturns:\n    A namedtuple (sign, logabsdet) containing the sign of the determinant, and the log\n    value of the absolute determinant.\n\nExample::\n\n    >>> A = torch.randn(3, 3)\n    >>> A\n    tensor([[ 0.0032, -0.2239, -1.1219],\n            [-0.6690,  0.1161,  0.4053],\n            [-1.6218, -0.9273, -0.0082]])\n    >>> torch.det(A)\n    tensor(-0.7576)\n    >>> torch.logdet(A)\n    tensor(nan)\n    >>> torch.slogdet(A)\n    torch.return_types.slogdet(sign=tensor(-1.), logabsdet=tensor(-0.2776))\n"
        pass
    
    @classmethod
    def smm(cls):
        pass
    
    @classmethod
    def softmax(cls):
        pass
    
    @classmethod
    def solve(cls):
        '\ntorch.solve(B, A, out=None) -> (Tensor, Tensor)\n\nThis function returns the solution to the system of linear\nequations represented by :math:`AX = B` and the LU factorization of\nA, in order as a namedtuple `solution, LU`.\n\n`LU` contains `L` and `U` factors for LU factorization of `A`.\n\n`torch.solve(B, A)` can take in 2D inputs `B, A` or inputs that are\nbatches of 2D matrices. If the inputs are batches, then returns\nbatched outputs `solution, LU`.\n\n.. note::\n\n    Irrespective of the original strides, the returned matrices\n    `solution` and `LU` will be transposed, i.e. with strides like\n    `B.contiguous().transpose(-1, -2).strides()` and\n    `A.contiguous().transpose(-1, -2).strides()` respectively.\n\nArgs:\n    B (Tensor): input matrix of size :math:`(*, m, k)` , where :math:`*`\n                is zero or more batch dimensions.\n    A (Tensor): input square matrix of size :math:`(*, m, m)`, where\n                :math:`*` is zero or more batch dimensions.\n    out ((Tensor, Tensor), optional): optional output tuple.\n\nExample::\n\n    >>> A = torch.tensor([[6.80, -2.11,  5.66,  5.97,  8.23],\n                          [-6.05, -3.30,  5.36, -4.44,  1.08],\n                          [-0.45,  2.58, -2.70,  0.27,  9.04],\n                          [8.32,  2.71,  4.35,  -7.17,  2.14],\n                          [-9.67, -5.14, -7.26,  6.08, -6.87]]).t()\n    >>> B = torch.tensor([[4.02,  6.19, -8.22, -7.57, -3.03],\n                          [-1.56,  4.00, -8.67,  1.75,  2.86],\n                          [9.81, -4.09, -4.57, -8.61,  8.99]]).t()\n    >>> X, LU = torch.solve(B, A)\n    >>> torch.dist(B, torch.mm(A, X))\n    tensor(1.00000e-06 *\n           7.0977)\n\n    >>> # Batched solver example\n    >>> A = torch.randn(2, 3, 1, 4, 4)\n    >>> B = torch.randn(2, 3, 1, 4, 6)\n    >>> X, LU = torch.solve(B, A)\n    >>> torch.dist(B, A.matmul(X))\n    tensor(1.00000e-06 *\n       3.6386)\n\n'
        pass
    
    @classmethod
    def sort(cls):
        '\nsort(input, dim=-1, descending=False, out=None) -> (Tensor, LongTensor)\n\nSorts the elements of the :attr:`input` tensor along a given dimension\nin ascending order by value.\n\nIf :attr:`dim` is not given, the last dimension of the `input` is chosen.\n\nIf :attr:`descending` is ``True`` then the elements are sorted in descending\norder by value.\n\nA namedtuple of (values, indices) is returned, where the `values` are the\nsorted values and `indices` are the indices of the elements in the original\n`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int, optional): the dimension to sort along\n    descending (bool, optional): controls the sorting order (ascending or descending)\n    out (tuple, optional): the output tuple of (`Tensor`, `LongTensor`) that can\n        be optionally given to be used as output buffers\n\nExample::\n\n    >>> x = torch.randn(3, 4)\n    >>> sorted, indices = torch.sort(x)\n    >>> sorted\n    tensor([[-0.2162,  0.0608,  0.6719,  2.3332],\n            [-0.5793,  0.0061,  0.6058,  0.9497],\n            [-0.5071,  0.3343,  0.9553,  1.0960]])\n    >>> indices\n    tensor([[ 1,  0,  2,  3],\n            [ 3,  1,  0,  2],\n            [ 0,  3,  1,  2]])\n\n    >>> sorted, indices = torch.sort(x, 0)\n    >>> sorted\n    tensor([[-0.5071, -0.2162,  0.6719, -0.5793],\n            [ 0.0608,  0.0061,  0.9497,  0.3343],\n            [ 0.6058,  0.9553,  1.0960,  2.3332]])\n    >>> indices\n    tensor([[ 2,  0,  0,  1],\n            [ 0,  1,  1,  2],\n            [ 1,  2,  2,  0]])\n'
        pass
    
    @classmethod
    def sparse_coo_tensor(cls):
        "\nsparse_coo_tensor(indices, values, size=None, dtype=None, device=None, requires_grad=False) -> Tensor\n\nConstructs a sparse tensors in COO(rdinate) format with non-zero elements at the given :attr:`indices`\nwith the given :attr:`values`. A sparse tensor can be `uncoalesced`, in that case, there are duplicate\ncoordinates in the indices, and the value at that index is the sum of all duplicate value entries:\n`torch.sparse`_.\n\nArgs:\n    indices (array_like): Initial data for the tensor. Can be a list, tuple,\n        NumPy ``ndarray``, scalar, and other types. Will be cast to a :class:`torch.LongTensor`\n        internally. The indices are the coordinates of the non-zero values in the matrix, and thus\n        should be two-dimensional where the first dimension is the number of tensor dimensions and\n        the second dimension is the number of non-zero values.\n    values (array_like): Initial values for the tensor. Can be a list, tuple,\n        NumPy ``ndarray``, scalar, and other types.\n    size (list, tuple, or :class:`torch.Size`, optional): Size of the sparse tensor. If not\n        provided the size will be inferred as the minimum size big enough to hold all non-zero\n        elements.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if None, infers data type from :attr:`values`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if None, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\n\nExample::\n\n    >>> i = torch.tensor([[0, 1, 1],\n                          [2, 0, 2]])\n    >>> v = torch.tensor([3, 4, 5], dtype=torch.float32)\n    >>> torch.sparse_coo_tensor(i, v, [2, 4])\n    tensor(indices=tensor([[0, 1, 1],\n                           [2, 0, 2]]),\n           values=tensor([3., 4., 5.]),\n           size=(2, 4), nnz=3, layout=torch.sparse_coo)\n\n    >>> torch.sparse_coo_tensor(i, v)  # Shape inference\n    tensor(indices=tensor([[0, 1, 1],\n                           [2, 0, 2]]),\n           values=tensor([3., 4., 5.]),\n           size=(2, 3), nnz=3, layout=torch.sparse_coo)\n\n    >>> torch.sparse_coo_tensor(i, v, [2, 4],\n                                dtype=torch.float64,\n                                device=torch.device('cuda:0'))\n    tensor(indices=tensor([[0, 1, 1],\n                           [2, 0, 2]]),\n           values=tensor([3., 4., 5.]),\n           device='cuda:0', size=(2, 4), nnz=3, dtype=torch.float64,\n           layout=torch.sparse_coo)\n\n    # Create an empty sparse tensor with the following invariants:\n    #   1. sparse_dim + dense_dim = len(SparseTensor.shape)\n    #   2. SparseTensor._indices().shape = (sparse_dim, nnz)\n    #   3. SparseTensor._values().shape = (nnz, SparseTensor.shape[sparse_dim:])\n    #\n    # For instance, to create an empty sparse tensor with nnz = 0, dense_dim = 0 and\n    # sparse_dim = 1 (hence indices is a 2D tensor of shape = (1, 0))\n    >>> S = torch.sparse_coo_tensor(torch.empty([1, 0]), [], [1])\n    tensor(indices=tensor([], size=(1, 0)),\n           values=tensor([], size=(0,)),\n           size=(1,), nnz=0, layout=torch.sparse_coo)\n\n    # and to create an empty sparse tensor with nnz = 0, dense_dim = 1 and\n    # sparse_dim = 1\n    >>> S = torch.sparse_coo_tensor(torch.empty([1, 0]), torch.empty([0, 2]), [1, 2])\n    tensor(indices=tensor([], size=(1, 0)),\n           values=tensor([], size=(0, 2)),\n           size=(1, 2), nnz=0, layout=torch.sparse_coo)\n\n.. _torch.sparse: https://pytorch.org/docs/stable/sparse.html\n"
        pass
    
    @classmethod
    def split(cls):
        pass
    
    @classmethod
    def split_with_sizes(cls):
        pass
    
    @classmethod
    def spmm(cls):
        pass
    
    @classmethod
    def sqrt(cls):
        '\nsqrt(input, out=None) -> Tensor\n\nReturns a new tensor with the square-root of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\sqrt{\\text{input}_{i}}\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-2.0755,  1.0226,  0.0831,  0.4806])\n    >>> torch.sqrt(a)\n    tensor([    nan,  1.0112,  0.2883,  0.6933])\n'
        pass
    
    @classmethod
    def sqrt_(cls):
        pass
    
    @classmethod
    def squeeze(cls):
        '\nsqueeze(input, dim=None, out=None) -> Tensor\n\nReturns a tensor with all the dimensions of :attr:`input` of size `1` removed.\n\nFor example, if `input` is of shape:\n:math:`(A \\times 1 \\times B \\times C \\times 1 \\times D)` then the `out` tensor\nwill be of shape: :math:`(A \\times B \\times C \\times D)`.\n\nWhen :attr:`dim` is given, a squeeze operation is done only in the given\ndimension. If `input` is of shape: :math:`(A \\times 1 \\times B)`,\n``squeeze(input, 0)`` leaves the tensor unchanged, but ``squeeze(input, 1)``\nwill squeeze the tensor to the shape :math:`(A \\times B)`.\n\n.. note:: The returned tensor shares the storage with the input tensor,\n          so changing the contents of one will change the contents of the other.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int, optional): if given, the input will be squeezed only in\n           this dimension\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> x = torch.zeros(2, 1, 2, 1, 2)\n    >>> x.size()\n    torch.Size([2, 1, 2, 1, 2])\n    >>> y = torch.squeeze(x)\n    >>> y.size()\n    torch.Size([2, 2, 2])\n    >>> y = torch.squeeze(x, 0)\n    >>> y.size()\n    torch.Size([2, 1, 2, 1, 2])\n    >>> y = torch.squeeze(x, 1)\n    >>> y.size()\n    torch.Size([2, 2, 1, 2])\n'
        pass
    
    @classmethod
    def sspaddmm(cls):
        pass
    
    @classmethod
    def stack(cls):
        '\nstack(seq, dim=0, out=None) -> Tensor\n\nConcatenates sequence of tensors along a new dimension.\n\nAll tensors need to be of the same size.\n\nArguments:\n    seq (sequence of Tensors): sequence of tensors to concatenate\n    dim (int): dimension to insert. Has to be between 0 and the number\n        of dimensions of concatenated tensors (inclusive)\n    out (Tensor, optional): the output tensor\n'
        pass
    
    @classmethod
    def std(cls):
        "\n.. function:: std(input, unbiased=True) -> Tensor\n\nReturns the standard-deviation of all elements in the :attr:`input` tensor.\n\nIf :attr:`unbiased` is ``False``, then the standard-deviation will be calculated\nvia the biased estimator. Otherwise, Bessel's correction will be used.\n\nArgs:\n    input (Tensor): the input tensor\n    unbiased (bool): whether to use the unbiased estimation or not\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[-0.8166, -1.3802, -0.3560]])\n    >>> torch.std(a)\n    tensor(0.5130)\n\n.. function:: std(input, dim, keepdim=False, unbiased=True, out=None) -> Tensor\n\nReturns the standard-deviation of each row of the :attr:`input` tensor in the\ndimension :attr:`dim`. If :attr:`dim` is a list of dimensions,\nreduce over all of them.\n\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size\nas :attr:`input` except in the dimension(s) :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in the\noutput tensor having 1 (or ``len(dim)``) fewer dimension(s).\n\n\nIf :attr:`unbiased` is ``False``, then the standard-deviation will be calculated\nvia the biased estimator. Otherwise, Bessel's correction will be used.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int or tuple of ints): the dimension or dimensions to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    unbiased (bool): whether to use the unbiased estimation or not\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 0.2035,  1.2959,  1.8101, -0.4644],\n            [ 1.5027, -0.3270,  0.5905,  0.6538],\n            [-1.5745,  1.3330, -0.5596, -0.6548],\n            [ 0.1264, -0.5080,  1.6420,  0.1992]])\n    >>> torch.std(a, dim=1)\n    tensor([ 1.0311,  0.7477,  1.2204,  0.9087])\n"
        pass
    
    @classmethod
    def stft(cls):
        pass
    
    @classmethod
    def sub(cls):
        pass
    
    @classmethod
    def sum(cls):
        '\n.. function:: sum(input, dtype=None) -> Tensor\n\nReturns the sum of all elements in the :attr:`input` tensor.\n\nArgs:\n    input (Tensor): the input tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        If specified, the input tensor is casted to :attr:`dtype` before the operation\n        is performed. This is useful for preventing data type overflows. Default: None.\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[ 0.1133, -0.9567,  0.2958]])\n    >>> torch.sum(a)\n    tensor(-0.5475)\n\n.. function:: sum(input, dim, keepdim=False, dtype=None) -> Tensor\n\nReturns the sum of each row of the :attr:`input` tensor in the given\ndimension :attr:`dim`. If :attr:`dim` is a list of dimensions,\nreduce over all of them.\n\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size\nas :attr:`input` except in the dimension(s) :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in the\noutput tensor having 1 (or ``len(dim)``) fewer dimension(s).\n\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int or tuple of ints): the dimension or dimensions to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        If specified, the input tensor is casted to :attr:`dtype` before the operation\n        is performed. This is useful for preventing data type overflows. Default: None.\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[ 0.0569, -0.2475,  0.0737, -0.3429],\n            [-0.2993,  0.9138,  0.9337, -1.6864],\n            [ 0.1132,  0.7892, -0.1003,  0.5688],\n            [ 0.3637, -0.9906, -0.4752, -1.5197]])\n    >>> torch.sum(a, 1)\n    tensor([-0.4598, -0.1381,  1.3708, -2.6217])\n    >>> b = torch.arange(4 * 5 * 6).view(4, 5, 6)\n    >>> torch.sum(b, (2, 1))\n    tensor([  435.,  1335.,  2235.,  3135.])\n'
        pass
    
    @classmethod
    def svd(cls):
        "\nsvd(input, some=True, compute_uv=True, out=None) -> (Tensor, Tensor, Tensor)\n\n``svd(A)`` returns a namedtuple ``(U, S, V)`` which the singular value\ndecomposition of a input real matrix `A` of size `(n x m)` such that\n:math:`A = USV^T`.\n\n`U` is of shape :math:`(n \\times n)`.\n\n`S` is a diagonal matrix of shape :math:`(n \\times m)`, represented as a vector\nof size :math:`\\min(n, m)` containing the non-negative diagonal entries.\n\n`V` is of shape :math:`(m \\times m)`.\n\nIf :attr:`some` is ``True`` (default), the returned `U` and `V` matrices will\ncontain only :math:`min(n, m)` orthonormal columns.\n\nIf :attr:`compute_uv` is ``False``, the returned `U` and `V` matrices will be zero matrices\nof shape :math:`(n \\times n)` and :math:`(m \\times m)` respectively. :attr:`some` will be ignored here.\n\n.. note:: The implementation of SVD on CPU uses the LAPACK routine `?gesdd` (a divide-and-conquer\n          algorithm) instead of `?gesvd` for speed. Analogously, the SVD on GPU uses the MAGMA routine\n          `gesdd` as well.\n\n.. note:: Irrespective of the original strides, the returned matrix `U`\n          will be transposed, i.e. with strides `(1, n)` instead of `(n, 1)`.\n\n.. note:: Extra care needs to be taken when backward through `U` and `V`\n          outputs. Such operation is really only stable when :attr:`input` is\n          full rank with all distinct singular values. Otherwise, ``NaN`` can\n          appear as the gradients are not properly defined. Also, notice that\n          double backward will usually do an additional backward through `U` and\n          `V` even if the original backward is only on `S`.\n\n.. note:: When :attr:`some` = ``False``, the gradients on ``U[:, min(n, m):]``\n          and ``V[:, min(n, m):]`` will be ignored in backward as those vectors\n          can be arbitrary bases of the subspaces.\n\n.. note:: When :attr:`compute_uv` = ``False``, backward cannot be performed since ``U`` and ``V``\n          from the forward pass is required for the backward operation.\n\nArgs:\n    input (Tensor): the input 2-D tensor\n    some (bool, optional): controls the shape of returned `U` and `V`\n    out (tuple, optional): the output tuple of tensors\n\nExample::\n\n    >>> a = torch.tensor([[8.79,  6.11, -9.15,  9.57, -3.49,  9.84],\n                          [9.93,  6.91, -7.93,  1.64,  4.02,  0.15],\n                          [9.83,  5.04,  4.86,  8.83,  9.80, -8.99],\n                          [5.45, -0.27,  4.85,  0.74, 10.00, -6.02],\n                          [3.16,  7.98,  3.01,  5.80,  4.27, -5.31]]).t()\n\n    >>> torch.svd(a).__class__\n    <class 'torch.return_types.svd'>\n    >>> u, s, v = torch.svd(a)\n    >>> u\n    tensor([[-0.5911,  0.2632,  0.3554,  0.3143,  0.2299],\n            [-0.3976,  0.2438, -0.2224, -0.7535, -0.3636],\n            [-0.0335, -0.6003, -0.4508,  0.2334, -0.3055],\n            [-0.4297,  0.2362, -0.6859,  0.3319,  0.1649],\n            [-0.4697, -0.3509,  0.3874,  0.1587, -0.5183],\n            [ 0.2934,  0.5763, -0.0209,  0.3791, -0.6526]])\n    >>> s\n    tensor([ 27.4687,  22.6432,   8.5584,   5.9857,   2.0149])\n    >>> v\n    tensor([[-0.2514,  0.8148, -0.2606,  0.3967, -0.2180],\n            [-0.3968,  0.3587,  0.7008, -0.4507,  0.1402],\n            [-0.6922, -0.2489, -0.2208,  0.2513,  0.5891],\n            [-0.3662, -0.3686,  0.3859,  0.4342, -0.6265],\n            [-0.4076, -0.0980, -0.4933, -0.6227, -0.4396]])\n    >>> torch.dist(a, torch.mm(torch.mm(u, torch.diag(s)), v.t()))\n    tensor(1.00000e-06 *\n           9.3738)\n"
        pass
    
    @classmethod
    def symeig(cls):
        "\nsymeig(input, eigenvectors=False, upper=True, out=None) -> (Tensor, Tensor)\n\nThis function returns eigenvalues and eigenvectors\nof a real symmetric matrix :attr:`input`, represented by a namedtuple\n(eigenvalues, eigenvectors).\n\n:attr:`input` and :math:`V` are :math:`(m \\times m)` matrices and :math:`e` is a\n:math:`m` dimensional vector.\n\nThis function calculates all eigenvalues (and vectors) of :attr:`input`\nsuch that :math:`\\text{input} = V \\text{diag}(e) V^T`.\n\nThe boolean argument :attr:`eigenvectors` defines computation of\neigenvectors or eigenvalues only.\n\nIf it is ``False``, only eigenvalues are computed. If it is ``True``,\nboth eigenvalues and eigenvectors are computed.\n\nSince the input matrix :attr:`input` is supposed to be symmetric,\nonly the upper triangular portion is used by default.\n\nIf :attr:`upper` is ``False``, then lower triangular portion is used.\n\n.. note:: Irrespective of the original strides, the returned matrix `V` will\n          be transposed, i.e. with strides `(1, m)` instead of `(m, 1)`.\n\n.. note:: Extra care needs to be taken when backward through outputs. Such\n          operation is really only stable when all eigenvalues are distinct.\n          Otherwise, ``NaN`` can appear as the gradients are not properly defined.\n\nArgs:\n    input (Tensor): the input symmetric matrix\n    eigenvectors(boolean, optional): controls whether eigenvectors have to be computed\n    upper(boolean, optional): controls whether to consider upper-triangular or lower-triangular region\n    out (tuple, optional): the output tuple of (Tensor, Tensor)\n\nReturns:\n    (Tensor, Tensor): A namedtuple (eigenvalues, eigenvectors) containing\n\n        - **eigenvalues** (*Tensor*): Shape :math:`(m)`. Each element is an eigenvalue of ``input``,\n          The eigenvalues are in ascending order.\n        - **eigenvectors** (*Tensor*): Shape :math:`(m \\times m)`.\n          If ``eigenvectors=False``, it's a tensor filled with zeros.\n          Otherwise, this tensor contains the orthonormal eigenvectors of the ``input``.\n\nExamples::\n\n\n    >>> a = torch.tensor([[ 1.96,  0.00,  0.00,  0.00,  0.00],\n                          [-6.49,  3.80,  0.00,  0.00,  0.00],\n                          [-0.47, -6.39,  4.17,  0.00,  0.00],\n                          [-7.20,  1.50, -1.51,  5.70,  0.00],\n                          [-0.65, -6.34,  2.67,  1.80, -7.10]]).t()\n    >>> e, v = torch.symeig(a, eigenvectors=True)\n    >>> e\n    tensor([-11.0656,  -6.2287,   0.8640,   8.8655,  16.0948])\n    >>> v\n    tensor([[-0.2981, -0.6075,  0.4026, -0.3745,  0.4896],\n            [-0.5078, -0.2880, -0.4066, -0.3572, -0.6053],\n            [-0.0816, -0.3843, -0.6600,  0.5008,  0.3991],\n            [-0.0036, -0.4467,  0.4553,  0.6204, -0.4564],\n            [-0.8041,  0.4480,  0.1725,  0.3108,  0.1622]])\n"
        pass
    
    @classmethod
    def t(cls):
        '\nt(input) -> Tensor\n\nExpects :attr:`input` to be <= 2-D tensor and transposes dimensions 0\nand 1.\n\n0-D and 1-D tensors are returned as it is and\n2-D tensor can be seen as a short-hand function for ``transpose(input, 0, 1)``.\n\nArgs:\n    input (Tensor): the input tensor\n\nExample::\n\n    >>> x = torch.randn(())\n    >>> x\n    tensor(0.1995)\n    >>> torch.t(x)\n    tensor(0.1995)\n    >>> x = torch.randn(3)\n    >>> x\n    tensor([ 2.4320, -0.4608,  0.7702])\n    >>> torch.t(x)\n    tensor([.2.4320,.-0.4608,..0.7702])\n    >>> x = torch.randn(2, 3)\n    >>> x\n    tensor([[ 0.4875,  0.9158, -0.5872],\n            [ 0.3938, -0.6929,  0.6932]])\n    >>> torch.t(x)\n    tensor([[ 0.4875,  0.3938],\n            [ 0.9158, -0.6929],\n            [-0.5872,  0.6932]])\n'
        pass
    
    @classmethod
    def take(cls):
        '\ntake(input, indices) -> Tensor\n\nReturns a new tensor with the elements of :attr:`input` at the given indices.\nThe input tensor is treated as if it were viewed as a 1-D tensor. The result\ntakes the same shape as the indices.\n\nArgs:\n    input (Tensor): the input tensor\n    indices (LongTensor): the indices into tensor\n\nExample::\n\n    >>> src = torch.tensor([[4, 3, 5],\n                            [6, 7, 8]])\n    >>> torch.take(src, torch.tensor([0, 2, 5]))\n    tensor([ 4,  5,  8])\n'
        pass
    
    @classmethod
    def tan(cls):
        '\ntan(input, out=None) -> Tensor\n\nReturns a new tensor with the tangent of the elements of :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\tan(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([-1.2027, -1.7687,  0.4412, -1.3856])\n    >>> torch.tan(a)\n    tensor([-2.5930,  4.9859,  0.4722, -5.3366])\n'
        pass
    
    @classmethod
    def tan_(cls):
        pass
    
    @classmethod
    def tanh(cls):
        '\ntanh(input, out=None) -> Tensor\n\nReturns a new tensor with the hyperbolic tangent of the elements\nof :attr:`input`.\n\n.. math::\n    \\text{out}_{i} = \\tanh(\\text{input}_{i})\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 0.8986, -0.7279,  1.1745,  0.2611])\n    >>> torch.tanh(a)\n    tensor([ 0.7156, -0.6218,  0.8257,  0.2553])\n'
        pass
    
    @classmethod
    def tanh_(cls):
        pass
    
    @classmethod
    def tensor(cls):
        "\ntensor(data, dtype=None, device=None, requires_grad=False, pin_memory=False) -> Tensor\n\nConstructs a tensor with :attr:`data`.\n\n.. warning::\n\n    :func:`torch.tensor` always copies :attr:`data`. If you have a Tensor\n    ``data`` and want to avoid a copy, use :func:`torch.Tensor.requires_grad_`\n    or :func:`torch.Tensor.detach`.\n    If you have a NumPy ``ndarray`` and want to avoid a copy, use\n    :func:`torch.as_tensor`.\n\n.. warning::\n\n    When data is a tensor `x`, :func:`torch.tensor` reads out 'the data' from whatever it is passed,\n    and constructs a leaf variable. Therefore ``torch.tensor(x)`` is equivalent to ``x.clone().detach()``\n    and ``torch.tensor(x, requires_grad=True)`` is equivalent to ``x.clone().detach().requires_grad_(True)``.\n    The equivalents using ``clone()`` and ``detach()`` are recommended.\n\nArgs:\n    data (array_like): Initial data for the tensor. Can be a list, tuple,\n        NumPy ``ndarray``, scalar, and other types.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, infers data type from :attr:`data`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n    pin_memory (bool, optional): If set, returned tensor would be allocated in\n        the pinned memory. Works only for CPU tensors. Default: ``False``.\n\n\nExample::\n\n    >>> torch.tensor([[0.1, 1.2], [2.2, 3.1], [4.9, 5.2]])\n    tensor([[ 0.1000,  1.2000],\n            [ 2.2000,  3.1000],\n            [ 4.9000,  5.2000]])\n\n    >>> torch.tensor([0, 1])  # Type inference on data\n    tensor([ 0,  1])\n\n    >>> torch.tensor([[0.11111, 0.222222, 0.3333333]],\n                     dtype=torch.float64,\n                     device=torch.device('cuda:0'))  # creates a torch.cuda.DoubleTensor\n    tensor([[ 0.1111,  0.2222,  0.3333]], dtype=torch.float64, device='cuda:0')\n\n    >>> torch.tensor(3.14159)  # Create a scalar (zero-dimensional tensor)\n    tensor(3.1416)\n\n    >>> torch.tensor([])  # Create an empty tensor (of size (0,))\n    tensor([])\n"
        pass
    
    @classmethod
    def tensordot(cls):
        pass
    
    @classmethod
    def threshold(cls):
        pass
    
    @classmethod
    def threshold_(cls):
        '\nthreshold_(input, threshold, value) -> Tensor\n\nIn-place version of :func:`~threshold`.\n'
        pass
    
    @classmethod
    def topk(cls):
        '\ntopk(input, k, dim=None, largest=True, sorted=True, out=None) -> (Tensor, LongTensor)\n\nReturns the :attr:`k` largest elements of the given :attr:`input` tensor along\na given dimension.\n\nIf :attr:`dim` is not given, the last dimension of the `input` is chosen.\n\nIf :attr:`largest` is ``False`` then the `k` smallest elements are returned.\n\nA namedtuple of `(values, indices)` is returned, where the `indices` are the indices\nof the elements in the original `input` tensor.\n\nThe boolean option :attr:`sorted` if ``True``, will make sure that the returned\n`k` elements are themselves sorted\n\nArgs:\n    input (Tensor): the input tensor\n    k (int): the k in "top-k"\n    dim (int, optional): the dimension to sort along\n    largest (bool, optional): controls whether to return largest or\n           smallest elements\n    sorted (bool, optional): controls whether to return the elements\n           in sorted order\n    out (tuple, optional): the output tuple of (Tensor, LongTensor) that can be\n        optionally given to be used as output buffers\n\nExample::\n\n    >>> x = torch.arange(1., 6.)\n    >>> x\n    tensor([ 1.,  2.,  3.,  4.,  5.])\n    >>> torch.topk(x, 3)\n    torch.return_types.topk(values=tensor([5., 4., 3.]), indices=tensor([4, 3, 2]))\n'
        pass
    
    @classmethod
    def trace(cls):
        '\ntrace(input) -> Tensor\n\nReturns the sum of the elements of the diagonal of the input 2-D matrix.\n\nExample::\n\n    >>> x = torch.arange(1., 10.).view(3, 3)\n    >>> x\n    tensor([[ 1.,  2.,  3.],\n            [ 4.,  5.,  6.],\n            [ 7.,  8.,  9.]])\n    >>> torch.trace(x)\n    tensor(15.)\n'
        pass
    
    @classmethod
    def transpose(cls):
        "\ntranspose(input, dim0, dim1) -> Tensor\n\nReturns a tensor that is a transposed version of :attr:`input`.\nThe given dimensions :attr:`dim0` and :attr:`dim1` are swapped.\n\nThe resulting :attr:`out` tensor shares it's underlying storage with the\n:attr:`input` tensor, so changing the content of one would change the content\nof the other.\n\nArgs:\n    input (Tensor): the input tensor\n    dim0 (int): the first dimension to be transposed\n    dim1 (int): the second dimension to be transposed\n\nExample::\n\n    >>> x = torch.randn(2, 3)\n    >>> x\n    tensor([[ 1.0028, -0.9893,  0.5809],\n            [-0.1669,  0.7299,  0.4942]])\n    >>> torch.transpose(x, 0, 1)\n    tensor([[ 1.0028, -0.1669],\n            [-0.9893,  0.7299],\n            [ 0.5809,  0.4942]])\n"
        pass
    
    @classmethod
    def triangular_solve(cls):
        '\ntriangular_solve(b, A, upper=True, transpose=False, unitriangular=False) -> (Tensor, Tensor)\n\nSolves a system of equations with a triangular coefficient matrix :math:`A`\nand multiple right-hand sides :attr:`b`.\n\nIn particular, solves :math:`AX = b` and assumes :math:`A` is upper-triangular\nwith the default keyword arguments.\n\n`torch.triangular_solve(b, A)` can take in 2D inputs `b, A` or inputs that are\nbatches of 2D matrices. If the inputs are batches, then returns\nbatched outputs `X`\n\n.. note::\n\n    The :attr:`out` keyword only supports 2D matrix inputs, that is,\n    `b, A` must be 2D matrices.\n\nArgs:\n    A (Tensor): the input triangular coefficient matrix of size :math:`(*, m, m)`\n                where :math:`*` is zero or more batch dimensions\n    b (Tensor): multiple right-hand sides of size :math:`(*, m, k)` where\n                :math:`*` is zero of more batch dimensions\n    upper (bool, optional): whether to solve the upper-triangular system\n        of equations (default) or the lower-triangular system of equations. Default: ``True``.\n    transpose (bool, optional): whether :math:`A` should be transposed before\n        being sent into the solver. Default: ``False``.\n    unitriangular (bool, optional): whether :math:`A` is unit triangular.\n        If True, the diagonal elements of :math:`A` are assumed to be\n        1 and not referenced from :math:`A`. Default: ``False``.\n\nReturns:\n    A namedtuple :math:`(solution, cloned_coefficient)` where :math:`cloned_coefficient`\n    is a clone of :math:`A` and :math:`solution` is the solution :math:`X` to :math:`AX = b`\n    (or whatever variant of the system of equations, depending on the keyword arguments.)\n\nExamples::\n\n    >>> A = torch.randn(2, 2).triu()\n    >>> A\n    tensor([[ 1.1527, -1.0753],\n            [ 0.0000,  0.7986]])\n    >>> b = torch.randn(2, 3)\n    >>> b\n    tensor([[-0.0210,  2.3513, -1.5492],\n            [ 1.5429,  0.7403, -1.0243]])\n    >>> torch.triangular_solve(b, A)\n    torch.return_types.triangular_solve(\n    solution=tensor([[ 1.7841,  2.9046, -2.5405],\n            [ 1.9320,  0.9270, -1.2826]]),\n    cloned_coefficient=tensor([[ 1.1527, -1.0753],\n            [ 0.0000,  0.7986]]))\n'
        pass
    
    @classmethod
    def tril(cls):
        '\ntril(input, diagonal=0, out=None) -> Tensor\n\nReturns the lower triangular part of the matrix (2-D tensor) or batch of matrices\n:attr:`input`, the other elements of the result tensor :attr:`out` are set to 0.\n\nThe lower triangular part of the matrix is defined as the elements on and\nbelow the diagonal.\n\nThe argument :attr:`diagonal` controls which diagonal to consider. If\n:attr:`diagonal` = 0, all elements on and below the main diagonal are\nretained. A positive value includes just as many diagonals above the main\ndiagonal, and similarly a negative value excludes just as many diagonals below\nthe main diagonal. The main diagonal are the set of indices\n:math:`\\lbrace (i, i) \\rbrace` for :math:`i \\in [0, \\min\\{d_{1}, d_{2}\\} - 1]` where\n:math:`d_{1}, d_{2}` are the dimensions of the matrix.\n\nArgs:\n    input (Tensor): the input tensor\n    diagonal (int, optional): the diagonal to consider\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(3, 3)\n    >>> a\n    tensor([[-1.0813, -0.8619,  0.7105],\n            [ 0.0935,  0.1380,  2.2112],\n            [-0.3409, -0.9828,  0.0289]])\n    >>> torch.tril(a)\n    tensor([[-1.0813,  0.0000,  0.0000],\n            [ 0.0935,  0.1380,  0.0000],\n            [-0.3409, -0.9828,  0.0289]])\n\n    >>> b = torch.randn(4, 6)\n    >>> b\n    tensor([[ 1.2219,  0.5653, -0.2521, -0.2345,  1.2544,  0.3461],\n            [ 0.4785, -0.4477,  0.6049,  0.6368,  0.8775,  0.7145],\n            [ 1.1502,  3.2716, -1.1243, -0.5413,  0.3615,  0.6864],\n            [-0.0614, -0.7344, -1.3164, -0.7648, -1.4024,  0.0978]])\n    >>> torch.tril(b, diagonal=1)\n    tensor([[ 1.2219,  0.5653,  0.0000,  0.0000,  0.0000,  0.0000],\n            [ 0.4785, -0.4477,  0.6049,  0.0000,  0.0000,  0.0000],\n            [ 1.1502,  3.2716, -1.1243, -0.5413,  0.0000,  0.0000],\n            [-0.0614, -0.7344, -1.3164, -0.7648, -1.4024,  0.0000]])\n    >>> torch.tril(b, diagonal=-1)\n    tensor([[ 0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000],\n            [ 0.4785,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000],\n            [ 1.1502,  3.2716,  0.0000,  0.0000,  0.0000,  0.0000],\n            [-0.0614, -0.7344, -1.3164,  0.0000,  0.0000,  0.0000]])\n'
        pass
    
    @classmethod
    def tril_indices(cls):
        "\ntril_indices(row, column, offset=0, dtype=torch.long, device='cpu', layout=torch.strided) -> Tensor\n\nReturns the indices of the lower triangular part of a :attr:`row`-by-\n:attr:`column` matrix in a 2-by-N Tensor, where the first row contains row\ncoordinates of all indices and the second row contains column coordinates.\nIndices are ordered based on rows and then columns.\n\nThe lower triangular part of the matrix is defined as the elements on and\nbelow the diagonal.\n\nThe argument :attr:`offset` controls which diagonal to consider. If\n:attr:`offset` = 0, all elements on and below the main diagonal are\nretained. A positive value includes just as many diagonals above the main\ndiagonal, and similarly a negative value excludes just as many diagonals below\nthe main diagonal. The main diagonal are the set of indices\n:math:`\\lbrace (i, i) \\rbrace` for :math:`i \\in [0, \\min\\{d_{1}, d_{2}\\} - 1]`\nwhere :math:`d_{1}, d_{2}` are the dimensions of the matrix.\n\nNOTE: when running on 'cuda', row * col must be less than :math:`2^{59}` to\nprevent overflow during calculation.\n\nArgs:\n    row (``int``): number of rows in the 2-D matrix.\n    column (``int``): number of columns in the 2-D matrix.\n    offset (``int``): diagonal offset from the main diagonal.\n        Default: if not provided, 0.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, ``torch.long``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    layout (:class:`torch.layout`, optional): currently only support ``torch.strided``.\n\nExample::\n    >>> a = torch.tril_indices(3, 3)\n    >>> a\n    tensor([[0, 1, 1, 2, 2, 2],\n            [0, 0, 1, 0, 1, 2]])\n\n    >>> a = torch.tril_indices(4, 3, -1)\n    >>> a\n    tensor([[1, 2, 2, 3, 3, 3],\n            [0, 0, 1, 0, 1, 2]])\n\n    >>> a = torch.tril_indices(4, 3, 1)\n    >>> a\n    tensor([[0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3],\n            [0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2]])\n"
        pass
    
    @classmethod
    def triplet_margin_loss(cls):
        pass
    
    @classmethod
    def triu(cls):
        '\ntriu(input, diagonal=0, out=None) -> Tensor\n\nReturns the upper triangular part of a matrix (2-D tensor) or batch of matrices\n:attr:`input`, the other elements of the result tensor :attr:`out` are set to 0.\n\nThe upper triangular part of the matrix is defined as the elements on and\nabove the diagonal.\n\nThe argument :attr:`diagonal` controls which diagonal to consider. If\n:attr:`diagonal` = 0, all elements on and below the main diagonal are\nretained. A positive value excludes just as many diagonals above the main\ndiagonal, and similarly a negative value includes just as many diagonals below\nthe main diagonal. The main diagonal are the set of indices\n:math:`\\lbrace (i, i) \\rbrace` for :math:`i \\in [0, \\min\\{d_{1}, d_{2}\\} - 1]` where\n:math:`d_{1}, d_{2}` are the dimensions of the matrix.\n\nArgs:\n    input (Tensor): the input tensor\n    diagonal (int, optional): the diagonal to consider\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(3, 3)\n    >>> a\n    tensor([[ 0.2309,  0.5207,  2.0049],\n            [ 0.2072, -1.0680,  0.6602],\n            [ 0.3480, -0.5211, -0.4573]])\n    >>> torch.triu(a)\n    tensor([[ 0.2309,  0.5207,  2.0049],\n            [ 0.0000, -1.0680,  0.6602],\n            [ 0.0000,  0.0000, -0.4573]])\n    >>> torch.triu(a, diagonal=1)\n    tensor([[ 0.0000,  0.5207,  2.0049],\n            [ 0.0000,  0.0000,  0.6602],\n            [ 0.0000,  0.0000,  0.0000]])\n    >>> torch.triu(a, diagonal=-1)\n    tensor([[ 0.2309,  0.5207,  2.0049],\n            [ 0.2072, -1.0680,  0.6602],\n            [ 0.0000, -0.5211, -0.4573]])\n\n    >>> b = torch.randn(4, 6)\n    >>> b\n    tensor([[ 0.5876, -0.0794, -1.8373,  0.6654,  0.2604,  1.5235],\n            [-0.2447,  0.9556, -1.2919,  1.3378, -0.1768, -1.0857],\n            [ 0.4333,  0.3146,  0.6576, -1.0432,  0.9348, -0.4410],\n            [-0.9888,  1.0679, -1.3337, -1.6556,  0.4798,  0.2830]])\n    >>> torch.triu(b, diagonal=1)\n    tensor([[ 0.0000, -0.0794, -1.8373,  0.6654,  0.2604,  1.5235],\n            [ 0.0000,  0.0000, -1.2919,  1.3378, -0.1768, -1.0857],\n            [ 0.0000,  0.0000,  0.0000, -1.0432,  0.9348, -0.4410],\n            [ 0.0000,  0.0000,  0.0000,  0.0000,  0.4798,  0.2830]])\n    >>> torch.triu(b, diagonal=-1)\n    tensor([[ 0.5876, -0.0794, -1.8373,  0.6654,  0.2604,  1.5235],\n            [-0.2447,  0.9556, -1.2919,  1.3378, -0.1768, -1.0857],\n            [ 0.0000,  0.3146,  0.6576, -1.0432,  0.9348, -0.4410],\n            [ 0.0000,  0.0000, -1.3337, -1.6556,  0.4798,  0.2830]])\n'
        pass
    
    @classmethod
    def triu_indices(cls):
        "\ntriu_indices(row, column, offset=0, dtype=torch.long, device='cpu', layout=torch.strided) -> Tensor\n\nReturns the indices of the upper triangular part of a :attr:`row` by\n:attr:`column` matrix in a 2-by-N Tensor, where the first row contains row\ncoordinates of all indices and the second row contains column coordinates.\nIndices are ordered based on rows and then columns.\n\nThe upper triangular part of the matrix is defined as the elements on and\nabove the diagonal.\n\nThe argument :attr:`offset` controls which diagonal to consider. If\n:attr:`offset` = 0, all elements on and above the main diagonal are\nretained. A positive value excludes just as many diagonals above the main\ndiagonal, and similarly a negative value includes just as many diagonals below\nthe main diagonal. The main diagonal are the set of indices\n:math:`\\lbrace (i, i) \\rbrace` for :math:`i \\in [0, \\min\\{d_{1}, d_{2}\\} - 1]`\nwhere :math:`d_{1}, d_{2}` are the dimensions of the matrix.\n\nNOTE: when running on 'cuda', row * col must be less than :math:`2^{59}` to\nprevent overflow during calculation.\n\nArgs:\n    row (``int``): number of rows in the 2-D matrix.\n    column (``int``): number of columns in the 2-D matrix.\n    offset (``int``): diagonal offset from the main diagonal.\n        Default: if not provided, 0.\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, ``torch.long``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    layout (:class:`torch.layout`, optional): currently only support ``torch.strided``.\n\nExample::\n    >>> a = torch.triu_indices(3, 3)\n    >>> a\n    tensor([[0, 0, 0, 1, 1, 2],\n            [0, 1, 2, 1, 2, 2]])\n\n    >>> a = torch.triu_indices(4, 3, -1)\n    >>> a\n    tensor([[0, 0, 0, 1, 1, 1, 2, 2, 3],\n            [0, 1, 2, 0, 1, 2, 1, 2, 2]])\n\n    >>> a = torch.triu_indices(4, 3, 1)\n    >>> a\n    tensor([[0, 0, 1],\n            [1, 2, 2]])\n"
        pass
    
    @classmethod
    def trunc(cls):
        '\ntrunc(input, out=None) -> Tensor\n\nReturns a new tensor with the truncated integer values of\nthe elements of :attr:`input`.\n\nArgs:\n    input (Tensor): the input tensor\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4)\n    >>> a\n    tensor([ 3.4742,  0.5466, -0.8008, -0.9079])\n    >>> torch.trunc(a)\n    tensor([ 3.,  0., -0., -0.])\n'
        pass
    
    @classmethod
    def trunc_(cls):
        pass
    
    @classmethod
    def unbind(cls):
        '\nunbind(tensor, dim=0) -> seq\n\nRemoves a tensor dimension.\n\nReturns a tuple of all slices along a given dimension, already without it.\n\nArguments:\n    tensor (Tensor): the tensor to unbind\n    dim (int): dimension to remove\n\nExample::\n\n    >>> torch.unbind(torch.tensor([[1, 2, 3],\n    >>>                            [4, 5, 6],\n    >>>                            [7, 8, 9]]))\n    (tensor([1, 2, 3]), tensor([4, 5, 6]), tensor([7, 8, 9]))\n'
        pass
    
    @classmethod
    def unique_consecutive(cls):
        pass
    
    @classmethod
    def unique_dim(cls):
        pass
    
    @classmethod
    def unsqueeze(cls):
        '\nunsqueeze(input, dim, out=None) -> Tensor\n\nReturns a new tensor with a dimension of size one inserted at the\nspecified position.\n\nThe returned tensor shares the same underlying data with this tensor.\n\nA :attr:`dim` value within the range ``[-input.dim() - 1, input.dim() + 1)``\ncan be used. Negative :attr:`dim` will correspond to :meth:`unsqueeze`\napplied at :attr:`dim` = ``dim + input.dim() + 1``.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int): the index at which to insert the singleton dimension\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> x = torch.tensor([1, 2, 3, 4])\n    >>> torch.unsqueeze(x, 0)\n    tensor([[ 1,  2,  3,  4]])\n    >>> torch.unsqueeze(x, 1)\n    tensor([[ 1],\n            [ 2],\n            [ 3],\n            [ 4]])\n'
        pass
    
    @classmethod
    def var(cls):
        "\n.. function:: var(input, unbiased=True) -> Tensor\n\nReturns the variance of all elements in the :attr:`input` tensor.\n\nIf :attr:`unbiased` is ``False``, then the variance will be calculated via the\nbiased estimator. Otherwise, Bessel's correction will be used.\n\nArgs:\n    input (Tensor): the input tensor\n    unbiased (bool): whether to use the unbiased estimation or not\n\nExample::\n\n    >>> a = torch.randn(1, 3)\n    >>> a\n    tensor([[-0.3425, -1.2636, -0.4864]])\n    >>> torch.var(a)\n    tensor(0.2455)\n\n\n.. function:: var(input, dim, keepdim=False, unbiased=True, out=None) -> Tensor\n\nReturns the variance of each row of the :attr:`input` tensor in the given\ndimension :attr:`dim`.\n\n\nIf :attr:`keepdim` is ``True``, the output tensor is of the same size\nas :attr:`input` except in the dimension(s) :attr:`dim` where it is of size 1.\nOtherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting in the\noutput tensor having 1 (or ``len(dim)``) fewer dimension(s).\n\n\nIf :attr:`unbiased` is ``False``, then the variance will be calculated via the\nbiased estimator. Otherwise, Bessel's correction will be used.\n\nArgs:\n    input (Tensor): the input tensor\n    dim (int or tuple of ints): the dimension or dimensions to reduce\n    keepdim (bool): whether the output tensor has :attr:`dim` retained or not\n    unbiased (bool): whether to use the unbiased estimation or not\n    out (Tensor, optional): the output tensor\n\nExample::\n\n    >>> a = torch.randn(4, 4)\n    >>> a\n    tensor([[-0.3567,  1.7385, -1.3042,  0.7423],\n            [ 1.3436, -0.1015, -0.9834, -0.8438],\n            [ 0.6056,  0.1089, -0.3112, -1.4085],\n            [-0.7700,  0.6074, -0.1469,  0.7777]])\n    >>> torch.var(a, 1)\n    tensor([ 1.7444,  1.1363,  0.7356,  0.5112])\n"
        pass
    
    @classmethod
    def where(cls):
        '\nwhere(condition, x, y) -> Tensor\n\nReturn a tensor of elements selected from either :attr:`x` or :attr:`y`, depending on :attr:`condition`.\n\nThe operation is defined as:\n\n.. math::\n    out_i = \\begin{cases}\n        x_i & \\text{if } \\text{condition}_i \\\\\n        y_i & \\text{otherwise} \\\\\n    \\end{cases}\n\n.. note::\n    The tensors :attr:`condition`, :attr:`x`, :attr:`y` must be :ref:`broadcastable <broadcasting-semantics>`.\n\nArguments:\n    condition (ByteTensor): When True (nonzero), yield x, otherwise yield y\n    x (Tensor): values selected at indices where :attr:`condition` is ``True``\n    y (Tensor): values selected at indices where :attr:`condition` is ``False``\n\nReturns:\n    Tensor: A tensor of shape equal to the broadcasted shape of :attr:`condition`, :attr:`x`, :attr:`y`\n\nExample::\n\n    >>> x = torch.randn(3, 2)\n    >>> y = torch.ones(3, 2)\n    >>> x\n    tensor([[-0.4620,  0.3139],\n            [ 0.3898, -0.7197],\n            [ 0.0478, -0.1657]])\n    >>> torch.where(x > 0, x, y)\n    tensor([[ 1.0000,  0.3139],\n            [ 0.3898,  1.0000],\n            [ 0.0478,  1.0000]])\n'
        pass
    
    @classmethod
    def zero_(cls):
        pass
    
    @classmethod
    def zeros(cls):
        '\nzeros(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with the scalar value `0`, with the shape defined\nby the variable argument :attr:`sizes`.\n\nArgs:\n    sizes (int...): a sequence of integers defining the shape of the output tensor.\n        Can be a variable number of arguments or a collection like a list or tuple.\n    out (Tensor, optional): the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned tensor.\n        Default: if ``None``, uses a global default (see :func:`torch.set_default_tensor_type`).\n    layout (:class:`torch.layout`, optional): the desired layout of returned Tensor.\n        Default: ``torch.strided``.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, uses the current device for the default tensor type\n        (see :func:`torch.set_default_tensor_type`). :attr:`device` will be the CPU\n        for CPU tensor types and the current CUDA device for CUDA tensor types.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> torch.zeros(2, 3)\n    tensor([[ 0.,  0.,  0.],\n            [ 0.,  0.,  0.]])\n\n    >>> torch.zeros(5)\n    tensor([ 0.,  0.,  0.,  0.,  0.])\n'
        pass
    
    @classmethod
    def zeros_like(cls):
        '\nzeros_like(input, dtype=None, layout=None, device=None, requires_grad=False) -> Tensor\n\nReturns a tensor filled with the scalar value `0`, with the same size as\n:attr:`input`. ``torch.zeros_like(input)`` is equivalent to\n``torch.zeros(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)``.\n\n.. warning::\n    As of 0.4, this function does not support an :attr:`out` keyword. As an alternative,\n    the old ``torch.zeros_like(input, out=output)`` is equivalent to\n    ``torch.zeros(input.size(), out=output)``.\n\nArgs:\n    input (Tensor): the size of :attr:`input` will determine size of the output tensor\n    dtype (:class:`torch.dtype`, optional): the desired data type of returned Tensor.\n        Default: if ``None``, defaults to the dtype of :attr:`input`.\n    layout (:class:`torch.layout`, optional): the desired layout of returned tensor.\n        Default: if ``None``, defaults to the layout of :attr:`input`.\n    device (:class:`torch.device`, optional): the desired device of returned tensor.\n        Default: if ``None``, defaults to the device of :attr:`input`.\n    requires_grad (bool, optional): If autograd should record operations on the\n        returned tensor. Default: ``False``.\n\nExample::\n\n    >>> input = torch.empty(2, 3)\n    >>> torch.zeros_like(input)\n    tensor([[ 0.,  0.,  0.],\n            [ 0.,  0.,  0.]])\n'
        pass
    

__doc__ = None
__file__ = '/home/enliai/anaconda3/envs/py36/lib/python3.6/site-packages/torch/_C.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'torch._C'
__package__ = 'torch'
def _add_docstr():
    pass

def _autograd_init():
    pass

def _broadcast(arg0, arg1: List[int]):
    '_broadcast(arg0: at::Tensor, arg1: List[int]) -> List[at::Tensor]\n'
    pass

def _broadcast_coalesced(tensors: List[at::Tensor], devices: List[int], buffer_size: int):
    '_broadcast_coalesced(tensors: List[at::Tensor], devices: List[int], buffer_size: int) -> List[List[at::Tensor]]\n'
    pass

def _c10d_init():
    pass

def _crash_if_aten_asan():
    pass

def _crash_if_csrc_asan():
    pass

def _crash_if_csrc_ubsan():
    pass

def _create_function_from_graph(arg0: str, arg1: torch._C.Graph):
    '_create_function_from_graph(arg0: str, arg1: torch._C.Graph) -> torch._C.Function\n'
    pass

def _create_function_from_trace(arg0: str, arg1: function, arg2: tuple, arg3: function, arg4: bool):
    '_create_function_from_trace(arg0: str, arg1: function, arg2: tuple, arg3: function, arg4: bool) -> torch._C.Function\n'
    pass

def _cuda_cudaHostAllocator():
    pass

def _cuda_emptyCache():
    pass

def _cuda_getCompiledVersion():
    pass

def _cuda_getCurrentBlasHandle():
    pass

def _cuda_getCurrentStream():
    pass

def _cuda_getDefaultStream():
    pass

def _cuda_getDevice():
    pass

def _cuda_getDeviceCount():
    pass

def _cuda_getDriverVersion():
    pass

def _cuda_getRNGState():
    pass

def _cuda_init():
    pass

def _cuda_initialSeed():
    pass

def _cuda_ipc_collect():
    pass

def _cuda_isDriverSufficient():
    pass

def _cuda_lock_mutex():
    pass

def _cuda_manualSeed():
    pass

def _cuda_manualSeedAll():
    pass

def _cuda_maxMemoryAllocated():
    pass

def _cuda_maxMemoryCached():
    pass

def _cuda_memoryAllocated():
    pass

def _cuda_memoryCached():
    pass

def _cuda_resetMaxMemoryAllocated():
    pass

def _cuda_resetMaxMemoryCached():
    pass

def _cuda_seed():
    pass

def _cuda_seedAll():
    pass

def _cuda_setDevice():
    pass

def _cuda_setRNGState():
    pass

def _cuda_setStream():
    pass

def _cuda_sleep():
    pass

def _cuda_synchronize():
    pass

def _cuda_unlock_mutex():
    pass

def _cudnn_version():
    pass

def _debug_set_autodiff_subgraph_inlining(arg0: bool):
    '_debug_set_autodiff_subgraph_inlining(arg0: bool) -> None\n'
    pass

def _demangle(arg0: str):
    '_demangle(arg0: str) -> str\n'
    return ''

def _dist_all_gather():
    pass

def _dist_all_gather_multigpu():
    pass

def _dist_all_reduce():
    pass

def _dist_all_reduce_multigpu():
    pass

def _dist_barrier():
    pass

def _dist_broadcast():
    pass

def _dist_broadcast_multigpu():
    pass

def _dist_clear_group_cache():
    pass

def _dist_destroy_process_group():
    pass

def _dist_gather_recv():
    pass

def _dist_gather_send():
    pass

def _dist_get_num_processes():
    pass

def _dist_get_rank():
    pass

def _dist_init_extension():
    pass

def _dist_init_process_group():
    pass

def _dist_irecv():
    pass

def _dist_isend():
    pass

def _dist_new_group():
    pass

def _dist_recv():
    pass

def _dist_recv_any_source():
    pass

def _dist_reduce():
    pass

def _dist_reduce_multigpu():
    pass

def _dist_register_stream():
    pass

def _dist_request_is_completed():
    pass

def _dist_request_wait():
    pass

def _dist_scatter_recv():
    pass

def _dist_scatter_send():
    pass

def _dist_send():
    pass

def _error_if_any_worker_fails():
    pass

def _from_dlpack():
    pass

def _gather(tensors: List[at::Tensor], dim: int, destination_index: Optional[int]):
    '_gather(tensors: List[at::Tensor], dim: int, destination_index: Optional[int]) -> at::Tensor\n'
    pass

def _get_backcompat_broadcast_warn():
    pass

def _get_backcompat_keepdim_warn():
    pass

def _get_cudnn_benchmark():
    pass

def _get_cudnn_deterministic():
    pass

def _get_cudnn_enabled():
    pass

def _get_tracing_state():
    '_get_tracing_state() -> torch._C.TracingState\n'
    pass

def _get_value_trace(arg0):
    '_get_value_trace(arg0: torch::autograd::Variable) -> torch._C.Value\n'
    pass

def _has_distributed():
    pass

def _infer_size():
    pass

def _initExtension():
    pass

def _init_names():
    pass

def _is_default_type_cuda():
    pass

def _jit_assert_is_instance(arg0: object, arg1):
    '_jit_assert_is_instance(arg0: object, arg1: c10::Type) -> None\n'
    pass

def _jit_check_alias_annotation(arg0, arg1: tuple, arg2: str):
    '_jit_check_alias_annotation(arg0: torch::jit::Graph, arg1: tuple, arg2: str) -> None\n'
    pass

def _jit_clear_class_registry():
    '_jit_clear_class_registry() -> None\n'
    pass

def _jit_debug_fuser_num_cached_kernel_specs():
    '_jit_debug_fuser_num_cached_kernel_specs() -> int\n'
    return 1

def _jit_differentiate(arg0):
    '_jit_differentiate(arg0: torch::jit::Graph) -> torch::jit::Gradient\n'
    pass

def _jit_flatten(arg0: handle):
    '_jit_flatten(arg0: handle) -> Tuple[List[torch::autograd::Variable], torch._C.IODescriptor]\n'
    pass

def _jit_fuser_get_fused_kernel_code(arg0, arg1: List[at::Tensor]):
    '_jit_fuser_get_fused_kernel_code(arg0: torch::jit::Graph, arg1: List[at::Tensor]) -> str\n'
    return ''

def _jit_get_operation(qualified_name: str):
    '_jit_get_operation(qualified_name: str) -> cpp_function\n'
    pass

def _jit_get_schemas_for_operator(arg0: str):
    '_jit_get_schemas_for_operator(arg0: str) -> List[torch._C.FunctionSchema]\n'
    pass

def _jit_import_functions(arg0: torch._C.CompilationUnit, arg1: str, arg2: List[at::Tensor], arg3):
    '_jit_import_functions(arg0: torch._C.CompilationUnit, arg1: str, arg2: List[at::Tensor], arg3: Callable[[torch._C.Value], torch::jit::script::SugaredValue]) -> None\n'
    pass

def _jit_init():
    '_jit_init() -> bool\n'
    return True

def _jit_override_can_fuse_on_cpu(arg0: bool):
    '_jit_override_can_fuse_on_cpu(arg0: bool) -> None\n'
    pass

def _jit_pass_canonicalize(arg0):
    '_jit_pass_canonicalize(arg0: torch::jit::Graph) -> torch::jit::Graph\n'
    pass

def _jit_pass_canonicalize_ops(arg0):
    '_jit_pass_canonicalize_ops(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_complete_shape_analysis(arg0, arg1: tuple, arg2: bool):
    '_jit_pass_complete_shape_analysis(arg0: torch::jit::Graph, arg1: tuple, arg2: bool) -> None\n'
    pass

def _jit_pass_constant_pooling(arg0):
    '_jit_pass_constant_pooling(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_constant_propagation(arg0):
    '_jit_pass_constant_propagation(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_create_autodiff_subgraphs(arg0):
    '_jit_pass_create_autodiff_subgraphs(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_cse(arg0):
    '_jit_pass_cse(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_dce(arg0):
    '_jit_pass_dce(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_erase_number_types(arg0):
    '_jit_pass_erase_number_types(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_erase_shape_information(arg0):
    '_jit_pass_erase_shape_information(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_fixup_onnx_loops(arg0):
    '_jit_pass_fixup_onnx_loops(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_fold_quant_inputs(arg0):
    '_jit_pass_fold_quant_inputs(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_fuse(arg0):
    '_jit_pass_fuse(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_inline_fork_wait(arg0):
    '_jit_pass_inline_fork_wait(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_insert_observers(arg0, arg1: function):
    '_jit_pass_insert_observers(arg0: torch::jit::Graph, arg1: function) -> None\n'
    pass

def _jit_pass_insert_quantdequant(arg0):
    '_jit_pass_insert_quantdequant(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_lint(arg0):
    '_jit_pass_lint(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_loop_unrolling(arg0):
    '_jit_pass_loop_unrolling(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_lower_all_tuples(arg0):
    '_jit_pass_lower_all_tuples(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_onnx(arg0, arg1: torch._C._onnx.OperatorExportTypes):
    '_jit_pass_onnx(arg0: torch::jit::Graph, arg1: torch._C._onnx.OperatorExportTypes) -> torch::jit::Graph\n'
    pass

def _jit_pass_onnx_block(arg0, arg1, arg2: torch._C._onnx.OperatorExportTypes, arg3):
    '_jit_pass_onnx_block(arg0: torch::jit::Block, arg1: torch::jit::Block, arg2: torch._C._onnx.OperatorExportTypes, arg3: Dict[torch::jit::Value, torch::jit::Value]) -> None\n'
    pass

def _jit_pass_onnx_constant_fold(arg0, arg1: Dict[str,at::Tensor]):
    '_jit_pass_onnx_constant_fold(arg0: torch::jit::Graph, arg1: Dict[str, at::Tensor]) -> Dict[str, at::Tensor]\n'
    pass

def _jit_pass_onnx_peephole(arg0):
    '_jit_pass_onnx_peephole(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_peephole(graph, addmm_fusion_enabled: bool=False):
    '_jit_pass_peephole(graph: torch::jit::Graph, addmm_fusion_enabled: bool = False) -> None\n'
    pass

def _jit_pass_prepare_division_for_onnx(arg0):
    '_jit_pass_prepare_division_for_onnx(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_propagate_qinfo(arg0):
    '_jit_pass_propagate_qinfo(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_quantlint(arg0):
    '_jit_pass_quantlint(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_remove_expands(arg0):
    '_jit_pass_remove_expands(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_remove_inplace_ops(arg0):
    '_jit_pass_remove_inplace_ops(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_pass_specialize_autogradzero(arg0):
    '_jit_pass_specialize_autogradzero(arg0: torch::jit::Graph) -> None\n'
    pass

def _jit_python_print(arg0: object):
    '_jit_python_print(arg0: object) -> Tuple[str, List[at::Tensor]]\n'
    pass

def _jit_run_cpp_tests(run_cuda: bool):
    '_jit_run_cpp_tests(run_cuda: bool) -> None\n'
    pass

def _jit_script_class_compile(arg0: torch._C._jit_tree_views.ClassDef, arg1: Callable[[str],function]):
    '_jit_script_class_compile(arg0: torch._C._jit_tree_views.ClassDef, arg1: Callable[[str], function]) -> None\n'
    pass

def _jit_script_compile(arg0: torch._C._jit_tree_views.Def, arg1: Callable[[str],function], arg2: Dict[str,object]):
    '_jit_script_compile(arg0: torch._C._jit_tree_views.Def, arg1: Callable[[str], function], arg2: Dict[str, object]) -> torch._C.Function\n'
    pass

def _jit_set_emit_hooks(arg0: Callable[[torch._C.ScriptModule],None], arg1: Callable[[torch._C.Function],None]):
    '_jit_set_emit_hooks(arg0: Callable[[torch._C.ScriptModule], None], arg1: Callable[[torch._C.Function], None]) -> None\n'
    pass

def _jit_unflatten(arg0, arg1: torch._C.IODescriptor):
    '_jit_unflatten(arg0: List[torch::autograd::Variable], arg1: torch._C.IODescriptor) -> object\n'
    pass

def _last_executed_optimized_graph():
    '_last_executed_optimized_graph() -> torch._C.Graph\n\nRetrieve the optimized graph that was run the last time the graph executor ran on this thread\n'
    pass

def _logging_set_logger(arg0):
    '_logging_set_logger(arg0: torch::jit::logging::LoggerBase) -> torch::jit::logging::LoggerBase\n'
    pass

def _multiprocessing_init():
    pass

def _nccl_all_gather():
    pass

def _nccl_all_reduce():
    pass

def _nccl_broadcast():
    pass

def _nccl_init_rank():
    pass

def _nccl_reduce():
    pass

def _nccl_reduce_scatter():
    pass

def _nccl_unique_id():
    pass

def _nccl_version():
    pass

def _propagate_and_assign_input_and_output_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor], arg2: List[at::Tensor], arg3: bool, arg4: bool):
    '_propagate_and_assign_input_and_output_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor], arg2: List[at::Tensor], arg3: bool, arg4: bool) -> torch._C.Graph\n'
    pass

def _propagate_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor], arg2: bool):
    '_propagate_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor], arg2: bool) -> torch._C.Graph\n'
    pass

def _remove_worker_pids():
    pass

def _safe_call():
    pass

def _scatter(tensor, devices: List[int], chunk_sizes: Optional[List[int]], dim: int, streams: Optional[object]):
    '_scatter(tensor: at::Tensor, devices: List[int], chunk_sizes: Optional[List[int]], dim: int, streams: Optional[object]) -> List[at::Tensor]\n'
    pass

def _set_backcompat_broadcast_warn():
    pass

def _set_backcompat_keepdim_warn():
    pass

def _set_cudnn_benchmark():
    pass

def _set_cudnn_deterministic():
    pass

def _set_cudnn_enabled():
    pass

def _set_default_dtype():
    pass

def _set_default_tensor_type():
    pass

def _set_tracing_state(arg0: torch._C.TracingState):
    '_set_tracing_state(arg0: torch._C.TracingState) -> None\n'
    pass

def _set_value_trace(arg0, arg1: torch._C.Value):
    '_set_value_trace(arg0: torch::autograd::Variable, arg1: torch._C.Value) -> None\n'
    pass

def _set_worker_pids():
    pass

def _set_worker_signal_handlers():
    pass

def _show_config():
    pass

def _tensor_impl_raw_handle(arg0):
    '_tensor_impl_raw_handle(arg0: torch::autograd::Variable) -> capsule\n'
    pass

def _to_dlpack():
    pass

def _tracer_abandon():
    '_tracer_abandon() -> None\n'
    pass

def _tracer_enter(*args):
    '_tracer_enter(*args) -> Tuple[torch._C.TracingState, List[IValue]]\n'
    pass

def _tracer_exit(arg0: tuple):
    '_tracer_exit(arg0: tuple) -> None\n'
    pass

def _tracer_set_force_outplace(arg0: bool):
    '_tracer_set_force_outplace(arg0: bool) -> None\n'
    pass

def _tracer_set_get_unique_name_fn(arg0: function):
    '_tracer_set_get_unique_name_fn(arg0: function) -> None\n'
    pass

def _tracer_warn_use_python():
    '_tracer_warn_use_python() -> None\n'
    pass

def _wrap_tensor_impl(arg0: capsule):
    '_wrap_tensor_impl(arg0: capsule) -> object\n'
    pass

default_generator = Generator()
device = _mod_torch.device
dtype = _mod_torch.dtype
finfo = _mod_torch.finfo
def fork(*args):
    'fork(*args) -> torch._C.Future\n'
    pass

def get_default_dtype():
    '\nget_default_dtype() -> torch.dtype\n\nGet the current default floating point :class:`torch.dtype`.\n\nExample::\n\n    >>> torch.get_default_dtype()  # initial default for floating point is torch.float32\n    torch.float32\n    >>> torch.set_default_dtype(torch.float64)\n    >>> torch.get_default_dtype()  # default is now changed to torch.float64\n    torch.float64\n    >>> torch.set_default_tensor_type(torch.FloatTensor)  # setting tensor type also affects this\n    >>> torch.get_default_dtype()  # changed to torch.float32, the dtype for torch.FloatTensor\n    torch.float32\n\n'
    pass

def get_num_threads():
    '\nget_num_threads() -> int\n\nGets the number of threads used for parallelizing CPU operations\n'
    pass

has_cuda = True
has_cudnn = True
has_lapack = True
has_mkl = True
has_mkldnn = True
has_openmp = True
iinfo = _mod_torch.iinfo
def import_ir_module(arg0: Callable[[List[str]],torch._C.ScriptModule], arg1: str, arg2: object, arg3: torch._C.ExtraFilesMap):
    'import_ir_module(arg0: Callable[[List[str]], torch._C.ScriptModule], arg1: str, arg2: object, arg3: torch._C.ExtraFilesMap) -> None\n'
    pass

def import_ir_module_from_buffer(arg0: Callable[[List[str]],torch._C.ScriptModule], arg1: str, arg2: object, arg3: torch._C.ExtraFilesMap):
    'import_ir_module_from_buffer(arg0: Callable[[List[str]], torch._C.ScriptModule], arg1: str, arg2: object, arg3: torch._C.ExtraFilesMap) -> None\n'
    pass

def is_anomaly_enabled():
    pass

def is_grad_enabled():
    pass

layout = _mod_torch.layout
def merge_type_from_type_comment(arg0: torch._C._jit_tree_views.Decl, arg1: torch._C._jit_tree_views.Decl, arg2: bool):
    'merge_type_from_type_comment(arg0: torch._C._jit_tree_views.Decl, arg1: torch._C._jit_tree_views.Decl, arg2: bool) -> torch._C._jit_tree_views.Decl\n'
    pass

def parse_ir(arg0: str):
    'parse_ir(arg0: str) -> torch::jit::Graph\n'
    pass

def parse_type_comment(arg0: str):
    'parse_type_comment(arg0: str) -> torch._C._jit_tree_views.Decl\n'
    pass

def set_anomaly_enabled():
    pass

def set_flush_denormal():
    '\nset_flush_denormal(mode) -> bool\n\nDisables denormal floating numbers on CPU.\n\nReturns ``True`` if your system supports flushing denormal numbers and it\nsuccessfully configures flush denormal mode.  :meth:`~torch.set_flush_denormal`\nis only supported on x86 architectures supporting SSE3.\n\nArgs:\n    mode (bool): Controls whether to enable flush denormal mode or not\n\nExample::\n\n    >>> torch.set_flush_denormal(True)\n    True\n    >>> torch.tensor([1e-323], dtype=torch.float64)\n    tensor([ 0.], dtype=torch.float64)\n    >>> torch.set_flush_denormal(False)\n    True\n    >>> torch.tensor([1e-323], dtype=torch.float64)\n    tensor(9.88131e-324 *\n           [ 1.0000], dtype=torch.float64)\n'
    pass

def set_grad_enabled():
    pass

def set_num_threads():
    '\nset_num_threads(int)\n\nSets the number of threads used for parallelizing CPU operations.\nWARNING:\nTo ensure that the correct number of threads is used, set_num_threads\nmust be called before running eager, JIT or autograd code.\n'
    pass

def wait(arg0: torch._C.Future):
    'wait(arg0: torch._C.Future) -> IValue\n'
    pass

