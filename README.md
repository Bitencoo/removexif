# Removexif

Removexif is an easy to use Python library for dealing with exif metadata. Allowing you to remove, update and add exif metadata to your images.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install removexif.

```bash
pip3 install removexif
```

## Usage

Removing all EXIF metadata from only one image, and saving the new image at the same directory.
```python
from removexif.removexif import RemovExif

# Initialize RemovExif
remov_exif = RemovExif()

# Specify the path to the image file (without the extension of the image)
image_path = "/path/to/your/image"

# A new image with the suffix "_clean" will be created
# containing no Exif metadata.
remov_exif.remove_exif_single_file(image_path, extension=".imageextension", exif=None)
```

If you want to save the new image on a specific directory, you just need to pass the argument "new_directory=/path/to/new/directory".

```python
# This will save the new image at the new_directory path.
remov_exif.remove_exif_single_file(
       image_path,
       new_directoy="/path/to/new/directory/",
       extension=".jpeg",
       exif=None
)
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
