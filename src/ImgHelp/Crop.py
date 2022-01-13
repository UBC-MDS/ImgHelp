def crop(image, width, height):
    """
    This function crops image based on the input width and height.
      Arguments
      ---------
          image : numpy.ndarray
              An image, which is represented as a 3D numpy array in python
          width : int
              The desired width of the output image
          height : int
              The desired height of the output image
      Returns
      -------
          numpy array
              croped image as 3D array
      Examples
      -------
      >>> crop(image, width = 10, height = 10)
      """
