from imghelp.ColorConv import ColorConv
from numpy import random


def test_ColorConv():
    '''
    Test ColorConv returns the expected converted color imgage.
    '''
    test_img = random.random((50, 50, 3))
    assert ColorConv(test_img, 'gray') == np.mean(test_img, axis=2),"Image is not gray."

    assert ColorConv(test_img, 'red')[:,:,1] == np.zeros(test_img.shape[:2]),"Green channel did not turn off for red image."
    assert ColorConv(test_img, 'red')[:,:,2] == np.zeros(test_img.shape[:2]),"Blue channel did not turn off for red image."


    assert ColorConv(test_img, 'green')[:,:,0] == np.zeros(test_img.shape[:2]),"Red channel did not turn off for green image."
    assert ColorConv(test_img, 'green')[:,:,2] == np.zeros(test_img.shape[:2]),"Blue channel did not turn off for green image."

    assert ColorConv(test_img, 'blue')[:,:,0] == np.zeros(test_img.shape[:2]),"Red channel did not turn off for blue image."
    assert ColorConv(test_img, 'blue')[:,:,1] == np.zeros(test_img.shape[:2]),"Green channel did not turn off for blue image."
