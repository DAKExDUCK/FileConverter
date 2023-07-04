# ConvertFilesClass

The main idea is to simplify converting files to another formats

**ONLY LINUX!!!**


For now support:

| From | To |
| --- | ------------- |
| JPG | PNG, BMP, TIFF |
| PNG | JPG, BMP, TIFF |
| DOCX | PDF, ODT, HTML, TXT, RTF |
| PDF | HTML |

> Converting to `HTML` is sometimes looks weird because of `libreoffice` package


#### Preparation
1. Install `libreoffice` Linux package:
    - Arch:
    ```bash
    yay -S libreoffice
    ```
    - Ubuntu, RedHat:
    ```bash
    sudo apt install libreoffice
    ```
2. Install `multi-file-converter`:
    ```bash
    pip install multi-file-converter
    ```

#### Usage

```python
from file_converter import JPG, PNG

jpg = JPG('media/input.jpg') # or io.BytesIO object
png_bytes = jpg.convert_to_png() # convert and return new io.BytesIO object
with open('media/output.png', 'wb') as outfile:
    outfile.write(png_bytes.getbuffer()) # write to file

# show converted image
png = PNG(png_bytes)
png.img.show()
```
