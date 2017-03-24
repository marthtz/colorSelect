"""
How to run:
python dblSobel.py <imagefile>
"""

import cv2
import os
import sys


from guiutils import dblSobel


def main():
    fname = sys.argv[1]

    img = cv2.imread(fname)

    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    imgL = hls[:,:,1]
    imgS = hls[:,:,2]

    dSob = dblSobel(imgL, imgS, xLLow=0,  xLHigh=0, yLLow=0, yLHigh=0,
                                xSLow=0,  xSHigh=0, ySLow=0, ySHigh=0)

    print( "Sobel parameters:")
    #print( "H low: %f" % sSob.hLow())
    print( "xL low: %f" % dSob.xLLow())
    print( "xL high: %f" % dSob.xLHigh())
    print( "yL low: %f" % dSob.yLLow())
    print( "yL high: %f" % dSob.yLHigh())
    print( "xH low: %f" % dSob.xSLow())
    print( "xH high: %f" % dSob.xSHigh())
    print( "yH low: %f" % dSob.ySLow())
    print( "yH high: %f" % dSob.ySHigh())

    outFile = 'dbl_xLL{}xLH{}yLL{}yLH{}_xSL{}xSH{}ySL{}ySH{}'.format(
                dSob.xLLow(),dSob.xLHigh(),dSob.yLLow(),dSob.yLHigh(),
                dSob.xSLow(),dSob.xSHigh(),dSob.ySLow(),dSob.ySHigh())

    cv2.imwrite(fname.replace('.jpg','_{}.jpg'.format(outFile)) , dSob.dSobImage())


    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
