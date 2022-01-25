from imghelp.colorconv import ColorConv
from numpy import random
import numpy as np

def test_ColorConv():
    '''
    Test ColorConv returns the expected converted color imgage.
    '''
    test_img = random.random((50, 50, 3))
    assert ColorConv(test_img, 'gray').any() == np.mean(test_img, axis=2).any(),"Image is not gray."

    assert ColorConv(test_img, 'red')[:,:,1].any() == np.zeros(test_img.shape[:2]).any(),"Green channel did not turn off for red image."
    assert ColorConv(test_img, 'red')[:,:,2].any() == np.zeros(test_img.shape[:2]).any(),"Blue channel did not turn off for red image."


    assert ColorConv(test_img, 'green')[:,:,0].any() == np.zeros(test_img.shape[:2]).any(),"Red channel did not turn off for green image."
    assert ColorConv(test_img, 'green')[:,:,2].any() == np.zeros(test_img.shape[:2]).any(),"Blue channel did not turn off for green image."

    assert ColorConv(test_img, 'blue')[:,:,0].any() == np.zeros(test_img.shape[:2]).any(),"Red channel did not turn off for blue image."
    assert ColorConv(test_img, 'blue')[:,:,1].any() == np.zeros(test_img.shape[:2]).any(),"Green channel did not turn off for blue image."
