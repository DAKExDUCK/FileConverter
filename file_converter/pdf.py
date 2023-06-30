from io import BytesIO

from file_converter.types.document import Document


class PDF(Document):
    can_converts_to = [
        'docx'
    ]
    format = 'pdf'

    def convert_to_docx() -> BytesIO: ...
    # def convert_to_pngs() -> BytesIO: ...
    