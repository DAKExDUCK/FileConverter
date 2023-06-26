from copy import deepcopy
import io
from PIL import Image


class Img:
    can_converts_to: list
    img: Image.Image

    def __init__(self, img_or_path: str|Image.Image|io.BytesIO):
        if isinstance(img_or_path, Image.Image):
            self.img = img_or_path
        elif isinstance(img_or_path, io.BytesIO) or isinstance(img_or_path, str):
            self.img = Image.open(img_or_path).convert('RGB')
        else:
            raise ValueError("Invalid image type, it must be filepath, BytesIO or Pillow Image")
        
        self._create_conversion_functions()

    def _create_conversion_functions(self):
        for conversion_type in self.can_converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type):
        def conversion_func() -> io.BytesIO:
            format = 'JPEG' if conversion_type == 'jpg' else conversion_type.upper()
            output = io.BytesIO()
            self.img.save(output, format=format)
            return output
        return conversion_func
    
    def convert_to(self, format:str):
        if format.lower() not in self.can_converts_to:
            raise ValueError("Invalid format type")
        
        output = io.BytesIO()
        self.img.save(output, format=format.upper())
        return output
    

class Imgs:
    can_converts_to: list
    imgs: list[Image.Image]

    def _create_conversion_functions(self):
        for conversion_type in self.can_converts_to:
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
    
    def convert_to(self, format:str):
        if format.lower() not in self.can_converts_to:
            raise ValueError("Invalid format type")
        
        tmp_imgs = deepcopy(self.imgs)
        output = io.BytesIO()
        img = tmp_imgs.pop(0)
        img.save(output, save_all=True, append_images=tmp_imgs, format=format.upper())
        return output