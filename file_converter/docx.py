import io

from file_converter.types.document import Document


class DOCX(Document):
    can_converts_to = [
        'pdf'
    ]
    format = 'docx'

    def convert_to_docx() -> io.BytesIO: ...
    # def convert_to_pngs() -> io.BytesIO: ...
    