from PIL import Image
import os

class RemovExif:
    def remove_exif_directory(self, directory_path, new_directory=None, extension=(".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"), exif=None):
        files = os.listdir(directory_path)
        extensions = [file for file in files if file.lower().endswith(extension)]

        for ext in extensions:
            image_path = os.path.join(directory_path, ext)
            if(new_directory is not None):
                dir = new_directory + image_path[:image_path.rfind(".")][image_path[:image_path.rfind(".")].rfind("/") + 1:]
            else:
                dir = directory_path + image_path[:image_path.rfind(".")][image_path[:image_path.rfind(".")].rfind("/") + 1:]
            self.remove_exif_single_file(image_path[:image_path.rfind(".")], ext[ext.rfind("."):], dir, exif)
            
        return

    def remove_exif_single_file(self, file_path, extension, new_directoy=None, exif=None):
        if(extension is None):
            raise ValueError("Extension not provided, provide the image extension from the following choices: .png, .jpg, .jpeg")
        
        if(new_directoy is None):
            new_directoy = file_path

        try:
            image = Image.open(file_path + extension)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {file_path}{extension}\nCheck the file path!") from e
        self._clean_exif(image)
        self._add_exif(image, exif)
        self._export_new_image(image, new_directoy, extension, exif)
        return


    def _clean_exif(self, image, fields_to_keep=[]):
        exif = image.getexif()
        if exif is not None:
            for k in list(exif.keys()):
                if k not in fields_to_keep:
                    del exif[k]
        return

    def _add_exif(self, image, new_exif):
        exif = image.getexif()
        if exif is not None and new_exif is not None:
            exif.update(new_exif)
            image.info["exif"] = exif
    
    def _export_new_image(self, image, new_directory, extension, exif):
        data = list(image.getdata())
        image_output = Image.new(image.mode, image.size)
        image_output.putdata(data)

        if(exif is not None):
            self._add_exif(image, exif)
            image_output.save(f"{new_directory}_clean{extension}", exif=image.info["exif"])
            return
        image_output.save(f"{new_directory}_clean{extension}")
