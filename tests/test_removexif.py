import unittest
from unittest.mock import patch, Mock, MagicMock
from PIL import Image
from removexif import RemovExif

class TestRemovExif(unittest.TestCase):
    def setUp(self):
        self.remov_exif = RemovExif()

    @patch("removexif.os.listdir")
    @patch("removexif.RemovExif.remove_exif_single_file")
    def test_remove_exif_directory(self, mock_remove_exif_single_file, mock_listdir):
        mock_listdir.return_value = ["image1.png", "image2.jpg", "image3.jpeg"]

        mock_remove_exif_single_file.side_effect = lambda *args, **kwargs: None

        self.remov_exif.remove_exif_directory("/fake/directory/", extension=(".png", ".jpg", ".jpeg"), exif=None)

        expected_calls = [
            unittest.mock.call("/fake/directory/image1", ".png", "/fake/directory/image1", None),
            unittest.mock.call("/fake/directory/image2", ".jpg", "/fake/directory/image2", None),
            unittest.mock.call("/fake/directory/image3", ".jpeg", "/fake/directory/image3", None),
        ]
        mock_remove_exif_single_file.assert_has_calls(expected_calls)

    @patch("removexif.os.listdir")
    @patch("removexif.RemovExif.remove_exif_single_file")
    def test_remove_exif_directory_with_new_directory(self, mock_remove_exif_single_file, mock_listdir):
        mock_listdir.return_value = ["image1.png", "image2.jpg", "image3.jpeg"]

        mock_remove_exif_single_file.side_effect = lambda *args, **kwargs: None

        self.remov_exif.remove_exif_directory("/fake/directory/", "/fake/new_directory/", extension=(".png", ".jpg", ".jpeg"), exif=None)

        expected_calls = [
            unittest.mock.call("/fake/directory/image1", ".png", "/fake/new_directory/image1", None),
            unittest.mock.call("/fake/directory/image2", ".jpg", "/fake/new_directory/image2", None),
            unittest.mock.call("/fake/directory/image3", ".jpeg", "/fake/new_directory/image3", None),
        ]
        mock_remove_exif_single_file.assert_has_calls(expected_calls)

    @patch("removexif.Image.open")
    @patch("removexif.RemovExif._clean_exif")
    @patch("removexif.RemovExif._add_exif")
    @patch("removexif.Image.new")
    def test_remove_exif_single_file(self, mock_image_new, mock_add_exif, mock_clean_exif, mock_image_open):
        mock_image = MagicMock(spec=Image.Image)
        mock_image.info = {"exif":{"fake_key1": "fake_value1", "fake_key2": "fake_value2"}}
        mock_image.getexif.return_value = {"fake_key1": "fake_value1", "fake_key2": "fake_value2"}
        mock_image_open.return_value = mock_image

        mock_clean_exif.side_effect = lambda *args, **kwargs: None
        mock_add_exif.side_effect = lambda *args, **kwargs: None

        self.remov_exif.remove_exif_single_file("/fake/path", ".png", "/fake/new_directory", exif=None)

        mock_image_open.assert_called_once_with("/fake/path.png")

        mock_clean_exif.assert_called_once_with(mock_image)
        mock_add_exif.assert_called_once_with(mock_image, None)
        mock_image_new.assert_called_once_with(mock_image.mode, mock_image.size)
        self.assertEqual(mock_image.getexif(), {"fake_key1": "fake_value1"})

    # def test_clean_exif(self):
    #     mock_image = MagicMock(spec=Image.Image)
    #     mock_image.info = {"exif":{"fake_key1": "fake_value1", "fake_key2": "fake_value2"}}
    #     mock_image.getexif.return_value = {"fake_key1": "fake_value1", "fake_key2": "fake_value2"}
    #     self.remov_exif.clean_exif(mock_image, fields_to_keep=["fake_key1"])
        
    #     self.assertEqual(mock_image.getexif(), {"fake_key1": "fake_value1"})

    # def test_add_exif(self):
    #     mock_image = MagicMock(spec=Image.Image)
    #     mock_image.info = {"exif": {"existing_key": "existing_value"}}

    #     mock_image.getexif.return_value = {"existing_key": "existing_value"}

    #     new_exif_data = {"new_key": "new_value"}

    #     self.remov_exif.add_exif(mock_image, new_exif_data)

    #     expected_exif = {"existing_key": "existing_value", "new_key": "new_value"}
    #     self.assertEqual(mock_image.getexif(), expected_exif)

if __name__ == "__main__":
    unittest.main()
