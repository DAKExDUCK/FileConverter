import io
import os
import shutil
import tempfile


class TmpFileManager:
    tmp_dir = tempfile.mkdtemp()

    @classmethod
    def if_file_exists(cls, filename):
        return os.path.exists(cls.tmp_dir+filename)

    @classmethod
    def write_tmp_file(cls, bytes_io: io.BytesIO, format: str):
        if not cls.tmp_dir:
            cls.create_temp_dir()

        with tempfile.NamedTemporaryFile(suffix=f".{format}", dir=cls.tmp_dir, delete=False) as tmp_file:
            tmp_file.write(bytes_io.getbuffer())
            return tmp_file.name

    @classmethod
    def read_tmp_file(cls, filename):
        if not cls.if_file_exists(filename):
            return None
        
        with open(cls.tmp_dir+filename, 'rb') as tmp_file:
            return io.BytesIO(tmp_file.read())

    @classmethod
    def delete_tmp_file(cls, filename):
        if os.path.exists(cls.tmp_dir+filename):
            os.remove(cls.tmp_dir+filename)

    @classmethod
    def delete_temp_dir(cls):
        if cls.tmp_dir and os.path.exists(cls.tmp_dir):
            shutil.rmtree(cls.tmp_dir)
            cls.tmp_dir = None

