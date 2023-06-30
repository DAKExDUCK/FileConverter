from io import BytesIO

from file_converter.types.image import Img, Imgs


class PNG(Img):
    can_converts_to = [
        'pdf',
        'jpg'
    ]

    def convert_to_pdf() -> BytesIO: ...
    def convert_to_jpg() -> BytesIO: ...


class PNGs(Imgs):
    converts_to = [
        'pdf'
    ]

    def convert_to_pdf(self) -> BytesIO: ...
