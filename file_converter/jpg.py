from io import BytesIO

from PIL import Image

from .types.image import Img, Imgs


class JPG(Img):
    can_converts_to = [
        'pdf',
        'png',
        'bmp',
        'tiff'
    ]
    format = 'jpeg'

    def __init__(self, img_or_path: str | Image.Image | BytesIO) -> None:
        super().__init__(img_or_path)
        self.img = self.img.convert('RGB')

    def convert_to_pdf(self) -> BytesIO: ...
    def convert_to_png(self) -> BytesIO: ...
    def convert_to_bmp(self) -> BytesIO: ...
    def convert_to_tiff(self) -> BytesIO: ...


class JPGs(Imgs):
    converts_to = [
        'pdf'
    ]

    def convert_to_pdf(self) -> BytesIO: ...
