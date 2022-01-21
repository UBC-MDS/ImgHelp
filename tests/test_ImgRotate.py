from imghelp.Rotate import Rotate
import random
import pytest

def test_ImgRotate():
    """
    Test whether ImgRotate is outputting correctly rotated images.
    """
    # create black image with one RGB pixel
    img = np.zeros((10, 10, 3))
    red = img[0][0][0] = random.random()
    blue = img[0][0][1] = random.random()
    green = img[0][0][2] = random.random()
    
    assert ImgRotate(img, 90)[9][0].sum() == red + blue + green, "Image did not rotate 90 degrees."
    
    assert ImgRotate(img, 180)[9][9].sum() == red + blue + green, "Image did not rotate 180 degrees."
    
    assert ImgRotate(img, 270)[0][9].sum() == red + blue + green, "Image did not rotate 270 degrees."
    
    assert ImgRotate(img, 360)[0][0].sum() == red + blue + green, "Image did not rotate 360 degrees."

