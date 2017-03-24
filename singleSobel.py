"""
How to run:
python singleSobel.py <imagefile>
"""

import cv2
import os
import sys


from guiutils import singleSobel


def main():
    fname = sys.argv[1]

    img = cv2.imread(fname)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sSob = singleSobel(img, kSize=3, xLow=0,  xHigh=0, yLow=0, yHigh=0)

    print( "Sobel parameters:")
    print( "kernel: %d" % sSob.kernelSize())
    print( "x low: %f" % sSob.xLow())
    print( "x high: %f" % sSob.xHigh())
    print( "y low: %f" % sSob.yLow())
    print( "y high: %f" % sSob.yHigh())

    outFile = 'gray_k{}xL{}xH{}yL{}yH{}'.format(sSob.kernelSize(),
                sSob.xLow(),sSob.xHigh(),sSob.yLow(),sSob.yHigh())

    cv2.imwrite(fname.replace('.jpg','_{}.jpg'.format(outFile)) , sSob.sSobImage())

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
