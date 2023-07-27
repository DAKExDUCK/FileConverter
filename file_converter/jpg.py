from io import BytesIO

from PIL import Image

from .types.image import Img, Imgs


class JPG(Img):
    can_converts_to = [
        'png',
        'bmp',
        'tiff'
    ]
    format = 'jpeg'

    def __init__(self, img_or_path: str | Image.Image | BytesIO) -> None:
        super().__init__(img_or_path)
        self.img = self.img.convert('RGB')

    def convert_to_png(self) -> BytesIO: ...
    def convert_to_bmp(self) -> BytesIO: ...
    def convert_to_tiff(self) -> BytesIO: ...


class JPGs(Imgs):
    can_converts_to = [
        'pdf'
    ]
    format = 'jpeg'

    def __init__(self, imgs_or_paths: list[str|Image.Image|BytesIO]) -> None:
        self.imgs = [ JPG(_) for _ in imgs_or_paths ]
        self._create_conversion_functions()
    
    def convert_to_pdf(self) -> BytesIO: ...
