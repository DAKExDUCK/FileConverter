from .jpg import JPG, JPGs
from .pdf import PDF
from .png import PNG, PNGs
from .docx import DOCX


__all__ = [
    'JPG',
    'JPGs',
    'PNG',
    'PNGs',
    'PDF',
    'DOCX',
]


def define_class_for_format(key:str):
    if key not in __all__:
        return None
    
    index = __all__.index(key)
    name = __all__[index]
    obj = globals().get(name)
    if isinstance(obj, type):
        return obj
    