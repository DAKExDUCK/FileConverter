import subprocess
from io import BytesIO

from ..exceptions import ErrorConvertFile
from ..utils.tmp_file_manager import TmpFileManager as TFM


class Document:
    can_converts_to: list
    format: str
    doc: BytesIO

    def __init__(self, bytes_or_path: str|BytesIO) -> None:
        if isinstance(bytes_or_path, str):
            with open(bytes_or_path, 'rb') as file:
                self.doc = BytesIO(file.read())
        elif isinstance(bytes_or_path, BytesIO):
            self.doc = bytes_or_path
        else:
            raise ValueError("Invalid file type, it must be filepath or BytesIO")
        
        self._create_conversion_functions()

    def _create_conversion_functions(self) -> None:
        for conversion_type in self.can_converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type):
        def conversion_func() -> BytesIO:
            filepath = TFM.write_tmp_file(self.doc, self.format)
            outdir = filepath.split('.')[0]
            cmd = ['soffice', '--headless', '--convert-to', conversion_type, '--outdir', outdir, filepath]
            result = subprocess.run(
                cmd,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
            if result.stderr != b'':
                raise ErrorConvertFile(result.stderr.decode("utf-8"))

            with open(outdir+'/'+filepath.split('/')[-1].split('.')[0]+'.'+conversion_type, 'rb') as tmp_file:
                output = BytesIO(tmp_file.read())
                output.seek(0)
                return output
        return conversion_func

    def _convert(self, filepath:str, outdir:str, format:str) -> BytesIO:
        cmd = ['soffice', '--headless', '--convert-to', format, '--outdir', outdir, filepath]
        result = subprocess.run(
            cmd,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        if result.stderr != b'':
            raise ErrorConvertFile(result.stderr.decode("utf-8"))
        
        with open(outdir+'/'+filepath.split('/')[-1].split('.')[0]+'.'+format, 'rb') as tmp_file:
            output = BytesIO(tmp_file.read())
            output.seek(0)
            return output

    def convert_to(self, format:str) -> BytesIO:
        format = format.lower()
        # if format not in self.can_converts_to:
            # raise ValueError("Invalid format type")

        tmp_filename = TFM.write_tmp_file(self.doc, self.format)
        outdir = tmp_filename.split('.')[0]
        return self._convert(tmp_filename, outdir, format)
    