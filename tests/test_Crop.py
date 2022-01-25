from imghelp.crop import Crop
import pytest
from numpy import random

test_img = random.random((50, 50, 3))
wrong_type = 1
wrong_dim = random.random((10, 10))

def test_crop_output():
    '''
    This function tests the returned image has the
    expected size and type.
    '''
    assert Crop(test_img, 20, 20).shape[0:2] == (5, 5)

    assert Crop(test_img, 15, 15).shape[0:2] == (15, 0)

    assert len(Crop(test_img, 20, 20).shape) == 3

def test_crop_error():
    '''
    This function tests the Crop function returns corresponding
    error message based on different types of wrong input image.
    '''
    with pytest.raises(TypeError):
        Crop(test_img, 5.1, 5)
    with pytest.raises(ValueError):
        Crop(test_img, -1, 1)
    with pytest.raises(ValueError):
        Crop(test_img, 80, 80)
    with pytest.raises(TypeError):
        Crop(wrong_type, 10, 10)
    with pytest.raises(TypeError):
        Crop(wrong_dim, 10, 10)
