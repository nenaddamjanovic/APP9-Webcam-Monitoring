import glob
import os


def clean_folder():
    """
    Funktion cleans folder images of previous images
    :return:
    """
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
