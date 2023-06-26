import io

from file_converter.types.document import Document


class PDF(Document):
    can_converts_to = [
        'docx'
    ]
    format = 'pdf'

    def convert_to_docx() -> io.BytesIO: ...
    # def convert_to_pngs() -> io.BytesIO: ...
    