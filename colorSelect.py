"""
How to run:
python colorSelect.py <channel hsv or hls> <imagefile>
"""

import cv2
import os
import sys


from guiutils import colorSel

def main():
    channel = sys.argv[1]
    fname = sys.argv[2]

    img = cv2.imread(fname)

    if channel == 'hsv':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif channel == 'hls':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    cSel = colorSel(img, channel, hLow=0, sLow=0, vLow=0, hHigh=180, sHigh=255, vHigh=255)

    if channel == 'hsv':
        print( "HSV parameters:")
        print( "H low: %f" % cSel.hLow())
        print( "S low: %f" % cSel.sLow())
        print( "V low: %f" % cSel.vLow())
        print( "H High: %f" % cSel.hHigh())
        print( "S High: %f" % cSel.sHigh())
        print( "V High: %f" % cSel.vHigh())
        outFile = 'hsv_hL{}sL{}vL{}hH{}sH{}vH{}'.format(cSel.hLow(),cSel.sLow(),cSel.vLow(),
                                                        cSel.hHigh(),cSel.sHigh(),cSel.vHigh())
    elif channel == 'hls':
        print( "HLS parameters:")
        print( "H low: %f" % cSel.hLow())
        print( "L low: %f" % cSel.sLow())
        print( "S low: %f" % cSel.vLow())
        print( "H High: %f" % cSel.hHigh())
        print( "L High: %f" % cSel.sHigh())
        print( "S High: %f" % cSel.vHigh())
        outFile = 'hsv_hL{}lL{}sL{}hH{}lH{}sH{}'.format(cSel.hLow(),cSel.sLow(),cSel.vLow(),
                                                        cSel.hHigh(),cSel.sHigh(),cSel.vHigh())

    cv2.imwrite(fname.replace('.jpg','_{}.jpg'.format(outFile)) , cSel.cSelImage())

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
