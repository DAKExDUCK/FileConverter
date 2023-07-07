from io import BytesIO

from .types.image import Img, Imgs


class PNG(Img):
    can_converts_to = [
        'pdf',
        'jpg',
        'bmp',
        'tiff'
    ]
    format = 'png'

    def convert_to_pdf() -> BytesIO: ...
    def convert_to_jpg() -> BytesIO: ...
    def convert_to_bmp() -> BytesIO: ...
    def convert_to_tiff() -> BytesIO: ...


class PNGs(Imgs):
    converts_to = [
        'pdf'
    ]

    def convert_to_pdf(self) -> BytesIO: ...
