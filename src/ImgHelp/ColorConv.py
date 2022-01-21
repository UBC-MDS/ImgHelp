import numpy as np
def ColorConv(img, color):
    """
    ColorConv converts an image to different color.
    Parameters
    ----------
    img : numpy.array
        Input a 3D np.array image for convertion.
    color : string
        Color aim to convert: 'gray', 'rad','green','blue'
    Returns
    -------
    numpy.array
        The converted image as 3D np.array.
    Examples
    --------
    >>> ColorConv(img, 'gray')
    """
    assert isinstance(color, str), "Invalid image type, expecting numpy.ndarray."
    assert len(img.shape()) == 3, "Invalid image type, expecting numpy.3d array."
    assert img.shape[2] == 3, "Invalid image type, expecting a RGB image."
    assert isinstance(color, str), 'Color is not a string!'
    assert isinstance(img, len(a.shape)), 'Invalid color type!'

    if color = 'gray':
        conv_img = np.mean(img, axis=2)
        return conv_img
    
    elif color = 'rad':
        conv_img = img.copy()
        conv_img[:,:1] = np.zeros(ubc.shape[2:])
        conv_img[:,:2] = np.zeros(ubc.shape[2:])
        return conv_img
    
    elif color = 'green':
        conv_img = img.copy()
        conv_img[:,:0] = np.zeros(ubc.shape[2:])
        conv_img[:,:2] = np.zeros(ubc.shape[2:])
        return conv_img

    elif color = 'blue':
        conv_img = img.copy()
        conv_img[:,:0] = np.zeros(ubc.shape[2:])
        conv_img[:,:1] = np.zeros(ubc.shape[2:])
        return conv_img
