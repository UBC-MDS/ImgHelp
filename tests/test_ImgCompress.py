from imghelp.imgcompress import ImgCompress
import matplotlib.pyplot as plt
import numpy as np

def test_ImgCompress():
    """Test ImgHelp behave as expected"""
    
    #Check if function return correct error message for invalid image size
    img = np.array([])
    try:
        ImgCompress(img, 'resize', 1)
    except AssertionError as e:
        assert e.args[0] == "Input image has invalid dimension. Expecting a 3d array (RGB).", "Error for wrong image size is not working."

    #Check if function return correct error message for invalid image type
    img = [1,2,3]
    try:
        ImgCompress(img, 'resize', 1)
    except AssertionError as e:
        assert e.args[0] == "Invalid image type, expecting numpy.ndarray.", "Error for wrong input type is not working."

    #Check if function return correct error message for wrong level input
    img = np.ones((5, 5, 3))
    try:
        ImgCompress(img, 'resize', 5)
    except AssertionError as e:
        assert e.args[0] == "Invalid level, expecting 1, 2, 3", "Error for wrong input type is not working."
        
    #Check if function return correct error message for wrong level input
    img = np.ones((5, 5, 3))
    try:
        ImgCompress(img, 'apple', 1)
    except AssertionError as e:
        assert e.args[0] == "Invalid method, expecting 'SVD' or 'Resize'.", "Error for wrong input type is not working."

    #Check if function return correct output image for resize method (50%)
    img = np.ones((6, 6, 3))
    img_comp = ImgCompress(img, 'resize', 2)
    assert img_comp.shape == (3, 3, 3), "Resize functionality is not working properly."

    #Check if function return correct output image for svd method.
    pattern = np.array([[0,1,0,1,0,1,0],
                        [1,1,1,1,1,1,1],
                        [0,1,0,1,0,1,0],
                        [0,0,1,1,1,0,0],
                        [0,1,0,1,0,1,0]],dtype="uint8")
    img = np.zeros((5, 7, 3),dtype="uint8")
    img[:,:,0] = pattern*255

    pattern_exp = np.array([[67,199,97,229,97,199,67],
                        [102,48,147,93,147,48,102],
                        [67,199,97,229,97,199,67],
                        [45,134,65,154,65,134,45],
                        [67,199,97,229,97,199,67]], dtype="uint8")
    img_exp = np.zeros((5, 7, 3),dtype="uint8")
    img_exp[:,:,0] = pattern_exp

    img_comp = ImgCompress(img, 'svd', 2)
    plt.imshow(img_comp)
    assert np.sum(img_comp-img_exp) == 0, "SVD functionality is not working properly."