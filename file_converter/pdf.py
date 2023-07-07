from io import BytesIO

from .types.document import Document


class PDF(Document):
    can_converts_to = [
        'html'
    ]
    format = 'pdf'

    def convert_to_docx() -> BytesIO: ...
    # def convert_to_pngs() -> BytesIO: ...
    