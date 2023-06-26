import io
import subprocess

from file_converter.utils.tmp_file_manager import TmpFileManager as TFM


class Document:
    can_converts_to: list
    format: str
    doc: io.BytesIO

    def __init__(self, bytes_or_path: str|io.BytesIO):
        if isinstance(bytes_or_path, str):
            with open(bytes_or_path, 'rb') as file:
                self.doc = io.BytesIO(file.read())
        elif isinstance(bytes_or_path, io.BytesIO):
            self.doc = bytes_or_path
        else:
            raise ValueError("Invalid file type, it must be filepath or BytesIO")
        
        self._create_conversion_functions()

    def _create_conversion_functions(self):
        for conversion_type in self.can_converts_to:
            conversion_func_name = f'convert_to_{conversion_type}'
            setattr(self, conversion_func_name, self._create_conversion_func(conversion_type))

    def _create_conversion_func(self, conversion_type):
        def conversion_func():
            filepath = TFM.write_tmp_file(self.doc, self.format)
            outdir = filepath.split('.')[0]
            cmd = ['soffice', '--headless', '--convert-to', conversion_type, '--outdir', outdir, filepath]
            subprocess.call(
                cmd,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
            with open(outdir+'/'+filepath.split('/')[-1].split('.')[0]+'.'+conversion_type, 'rb') as tmp_file:
                return io.BytesIO(tmp_file.read())
        return conversion_func

    def _convert(filepath:str, outdir:str, format:str):
        cmd = ['soffice', '--headless', '--convert-to', format, '--outdir', outdir, filepath]
        subprocess.call(
            cmd,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

    def convert_to(self, format:str):
        format = format.lower()
        if format not in self.can_converts_to:
            raise ValueError("Invalid format type")

        output = io.BytesIO()
        tmp_filename = TFM.write_tmp_file(self.doc)
        outdir = tmp_filename.split('.')[0]
        self._convert(TFM.tmp_dir+tmp_filename, outdir, format)
        return output
    