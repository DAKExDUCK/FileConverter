from io import BytesIO

from file_converter.types.image import Img, Imgs


class JPG(Img):
    can_converts_to = [
        'pdf',
        'png'
    ]

    def convert_to_pdf(self) -> BytesIO: ...
    def convert_to_png(self) -> BytesIO: ...


class JPGs(Imgs):
    converts_to = [
        'pdf'
    ]

    def convert_to_pdf(self) -> BytesIO: ...
