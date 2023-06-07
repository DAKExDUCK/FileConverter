from copy import deepcopy
import io
from PIL import Image


class PNG:
    can_converts_to = [
        'pdf',
        'jpeg'
    ]

    def convert_to_pdf() -> io.BytesIO: ...
    def convert_to_jpg() -> io.BytesIO: ...

    def __init__(self, img_or_path: str|Image.Image|io.BytesIO):
        if isinstance(img_or_path, Image.Image):
            self.img = img_or_path
        elif isinstance(img_or_path, (str, io.BytesIO)):
            self.img = Image.open(img_or_path).convert('RGB')
        else:
            raise ValueError("Invalid image type, it must be filepath, BytesIO or Pillow Image")
        
        self._create_conversion_functions()

    def _create_conversion_functions(self):
        for conversion_type in self.converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type):
        def conversion_func():
            output = io.BytesIO()
            self.img.save(output, format=conversion_type.upper())
            return output
        return conversion_func
    
    def convert_to(self, format:str):
        output = io.BytesIO()
        self.img.save(output, format=format.upper())
        return output


class PNGs:
    converts_to = [
        'pdf'
    ]

    def convert_to_pdf() -> io.BytesIO: ...

    def __init__(self, imgs_or_paths: list[str|Image.Image|io.BytesIO]):
        self.imgs = [ PNG(img) for img in imgs_or_paths ]

        self._create_conversion_functions()

    def _create_conversion_functions(self):
        for conversion_type in self.converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type):
        def conversion_func():
            format = conversion_type.upper()
            tmp_imgs = deepcopy(self.imgs)
            output = io.BytesIO()
            img = tmp_imgs.pop(0)
            img.save(output, save_all=True, append_images=tmp_imgs, format=format)
            return output
        return conversion_func
    