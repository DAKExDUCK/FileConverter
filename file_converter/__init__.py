from file_converter.jpg import JPG, JPGs
from file_converter.pdf import PDF
from file_converter.png import PNG, PNGs
from file_converter.docx import DOCX


__all__ = [
    'JPG',
    'JPGs',
    'PNG',
    'PNGs',
    'PDF',
    'DOCX',
]


def define_class_for_format(key:str):
    if key.upper() not in __all__:
        return None
    
    index = __all__.index(key.upper())
    name = __all__[index]
    obj = globals().get(name)
    if isinstance(obj, type):
        return obj
    