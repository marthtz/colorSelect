# colorSelect
Threshold an image interactively (HSV,HSL, Sobel X/Y)

Command line tool to apply thresholding on an image interactively. Requires OpenCV an numpy.
Inspired by a similar tool from P1 that did Canny edge detection.

Supports HSV, HLS and Sobel X/Y.

Usage:
 * Color thresholding on HSV or HLS channel => python colorSelect.py [channel hsv or hls] [RGB image file]
 * Sobel Gradient X/Y on a grayscale image => python singleSobel.py [RGB image file]
 * Sobel Gradient X/Y on L and S channel => python dblSobel.py [RGB image file]
