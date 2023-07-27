from copy import deepcopy
from io import BytesIO
from PIL import Image

from ..exceptions import ErrorConvertFile


class Img:
    can_converts_to: list
    format: str
    img: Image.Image

    def __init__(self, img_or_path: str|Image.Image|BytesIO) -> None:
        if isinstance(img_or_path, Image.Image):
            self.img = img_or_path.convert('RGBA')
        elif isinstance(img_or_path, BytesIO) or isinstance(img_or_path, str):
            self.img = Image.open(img_or_path).convert('RGBA')
        else:
            raise ValueError("Invalid image type, it must be filepath, BytesIO or Pillow Image")
        
        self._create_conversion_functions()

    def _create_conversion_functions(self) -> None:
        for conversion_type in self.can_converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type: str):
        def conversion_func() -> BytesIO:
            format = 'JPEG' if conversion_type == 'jpg' else conversion_type.upper()
            output = BytesIO()
            try:
                if format == 'JPEG':
                    self.img = self.img.convert('RGB')
                self.img.save(output, format=format)
            except Exception as exc:
                raise ErrorConvertFile(str(exc))
            else:
                output.seek(0)
                return output
        return conversion_func
    
    def convert_to(self, format:str) -> BytesIO:
        format = 'JPEG' if format.lower() == 'jpg' else format.upper()
        # if format not in self.can_converts_to:
        #     raise ValueError("Invalid format type")
        
        output = BytesIO()
        try:
            if format == 'JPEG':
                self.img = self.img.convert('RGB')
            self.img.save(output, format=format)
        except Exception as exc:
            raise ErrorConvertFile(str(exc))
        else:
            output.seek(0)
            return output
    

class Imgs:
    can_converts_to: list
    imgs: list[Image.Image]

    def _create_conversion_functions(self) -> None:
        for conversion_type in self.can_converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type):
        def conversion_func() -> BytesIO:
            format = conversion_type.upper()
            tmp_imgs = [ _.img for _ in self.imgs ]
            output = BytesIO()
            img = tmp_imgs.pop(0)
            img.save(output, save_all=True, append_images=tmp_imgs, format=format)
            return output
        return conversion_func
    
    def convert_to(self, format:str) -> BytesIO:
        if format.lower() not in self.can_converts_to:
            raise ValueError("Invalid format type")
        
        tmp_imgs = [ _.img for _ in self.imgs ]
        output = BytesIO()
        img = tmp_imgs.pop(0)
        img.save(output, save_all=True, append_images=tmp_imgs, format=format.upper())
        return output