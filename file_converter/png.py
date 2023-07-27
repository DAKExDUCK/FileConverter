from io import BytesIO
from PIL import Image

from .types.image import Img, Imgs


class PNG(Img):
    can_converts_to = [
        'jpg',
        'bmp',
        'tiff'
    ]
    format = 'png'

    def convert_to_jpg() -> BytesIO: ...
    def convert_to_bmp() -> BytesIO: ...
    def convert_to_tiff() -> BytesIO: ...


class PNGs(Imgs):
    can_converts_to = [
        'pdf'
    ]
    format = 'png'

    def __init__(self, imgs_or_paths: list[str|Image.Image|BytesIO]) -> None:
        self.imgs = [ PNG(_) for _ in imgs_or_paths ]
        self._create_conversion_functions()

    def convert_to_pdf(self) -> BytesIO: ...
