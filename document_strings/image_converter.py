"""
Converts the given images to desired format.
Helps in easier conversion of images at once
"""


def convert_jpg_to_png(path, image_type):
    """
    Converts an image in Jpeg to PNG format

    This method returns the path of the image which can then be used to access the image

    Parameters:
    path (str): The path of the image
    image_type (str): The type of the image

    Returns:
    str: Image location or path of the converted image
    """
    print("Converting JPG to PNG", path, image_type)
