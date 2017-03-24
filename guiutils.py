import cv2
import numpy as np

class colorSel:
    def __init__(self, image, channel, hLow=0, sLow=0, vLow=0, hHigh=0, sHigh=0, vHigh=0):
        self.image = image
        self.channel = channel
        self._hLow = hLow
        self._sLow = sLow
        self._vLow = vLow
        self._hHigh = hHigh
        self._sHigh = sHigh
        self._vHigh = vHigh

        def onchangeHLow(pos):
            self._hLow = pos
            self._render(channel)

        def onchangeSLow(pos):
            self._sLow = pos
            self._render(channel)

        def onchangeVLow(pos):
            self._vLow = pos
            self._render(channel)

        def onchangeHHigh(pos):
            self._hHigh = pos
            self._render(channel)

        def onchangeSHigh(pos):
            self._sHigh = pos
            self._render(channel)

        def onchangeVHigh(pos):
            self._vHigh = pos
            self._render(channel)

        cv2.namedWindow('cSel')

        if channel == 'hsv':
            cv2.createTrackbar('H low', 'cSel', self._hLow, 180, onchangeHLow)
            cv2.createTrackbar('S low', 'cSel', self._sLow, 255, onchangeSLow)
            cv2.createTrackbar('V low', 'cSel', self._vLow, 255, onchangeVLow)
            cv2.createTrackbar('H high', 'cSel', self._hHigh, 180, onchangeHHigh)
            cv2.createTrackbar('S hgh', 'cSel', self._sHigh, 255, onchangeSHigh)
            cv2.createTrackbar('V high', 'cSel', self._vHigh, 255, onchangeVHigh)
        elif channel == 'hls':
            cv2.createTrackbar('H low', 'cSel', self._hLow, 180, onchangeHLow)
            cv2.createTrackbar('L low', 'cSel', self._sLow, 255, onchangeSLow)
            cv2.createTrackbar('S low', 'cSel', self._vLow, 255, onchangeVLow)
            cv2.createTrackbar('H high', 'cSel', self._hHigh, 180, onchangeHHigh)
            cv2.createTrackbar('L high', 'cSel', self._sHigh, 255, onchangeSHigh)
            cv2.createTrackbar('S high', 'cSel', self._vHigh, 255, onchangeVHigh)

        self._render(channel)

        print("Adjust the parameters as desired.  Hit any key to close.")

        cv2.waitKey(0)

        cv2.destroyWindow('cSel')

    def hLow(self):
        return self._hLow

    def sLow(self):
        return self._sLow

    def vLow(self):
        return self._vLow

    def hHigh(self):
        return self._hHigh

    def sHigh(self):
        return self._sHigh

    def vHigh(self):
        return self._vHigh

    def cSelImage(self):
        return self._hsv_img

    def _render(self, channel):
        low = np.array([ self._hLow, self._sLow, self._vLow])
        high = np.array([ self._hHigh, self._sHigh, self._vHigh])
        mask = cv2.inRange(self.image, low, high)
        self._hsv_img = cv2.bitwise_and(self.image, self.image, mask=mask)
        if channel == 'hsv':
            cv2.imshow('cSel', cv2.cvtColor(self._hsv_img, cv2.COLOR_HSV2BGR))
        elif channel == 'hls':
            cv2.imshow('cSel', cv2.cvtColor(self._hsv_img, cv2.COLOR_HLS2BGR))



class singleSobel:
    def __init__(self, image, kSize=3, xLow=0,  xHigh=0, yLow=0, yHigh=0):
        self.image = image
        self._kSize = kSize
        self._xLow = xLow
        self._yLow = yLow
        self._xHigh = xHigh
        self._yHigh = yHigh

        def onchangeKernelSize(pos):
            if pos == 0 or pos == 2 or pos == 4 or pos == 6:
                pass
            else:
                self._kernelSize = pos
                self._render()

        def onchangeXLow(pos):
            self._xLow = pos
            self._render()

        def onchangeYLow(pos):
            self._yLow = pos
            self._render()

        def onchangeXHigh(pos):
            self._xHigh = pos
            self._render()

        def onchangeYHigh(pos):
            self._yHigh = pos
            self._render()

        cv2.namedWindow('sSob')

        cv2.createTrackbar('kernelSize', 'sSob', self._kSize, 7, onchangeKernelSize)
        cv2.createTrackbar('xLow', 'sSob', self._xLow, 255, onchangeXLow)
        cv2.createTrackbar('xHigh', 'sSob', self._xHigh, 255, onchangeXHigh)
        cv2.createTrackbar('yLow', 'sSob', self._yLow, 255, onchangeYLow)
        cv2.createTrackbar('yHigh', 'sSob', self._yHigh, 255, onchangeYHigh)

        self._render()

        print("Adjust the parameters as desired.  Hit any key to close.")

        cv2.waitKey(0)

        cv2.destroyWindow('sSob')

    def kernelSize(self):
        return self._kernelSize

    def xLow(self):
        return self._xLow

    def yLow(self):
        return self._yLow

    def xHigh(self):
        return self._xHigh

    def yHigh(self):
        return self._yHigh

    def sSobImage(self):
        return self._sSob_img

    def _render(self):
        sobelx = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, ksize=self._kSize) # Take the derivative in x
        abs_sobelx = np.absolute(sobelx) # Absolute x derivative to accentuate lines away from horizontal
        scaled_sobel = np.uint8(255*abs_sobelx/np.max(abs_sobelx))

        sxbinary = np.zeros_like(scaled_sobel)
        sxbinary[(scaled_sobel >= self._xLow) & (scaled_sobel <= self._xHigh)] = 255

        sobely = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize=self._kSize) # Take the derivative in x
        abs_sobely = np.absolute(sobely) # Absolute x derivative to accentuate lines away from horizontal
        scaled_sobel = np.uint8(255*abs_sobely/np.max(abs_sobely))

        sybinary = np.zeros_like(scaled_sobel)
        sybinary[(scaled_sobel >= self._yLow) & (scaled_sobel <= self._yHigh)] = 255

        color_binary = np.dstack(( np.zeros_like(sxbinary), sxbinary, sybinary))
        #color_binary = np.dstack(( np.zeros_like(sxbinary), sxbinary, np.zeros_like(sxbinary)))

        self._sSob_img = cv2.cvtColor(color_binary, cv2.COLOR_BGR2RGB)
        cv2.imshow('sSob', self._sSob_img)


class dblSobel:
    def __init__(self, imageL, imageS, xLLow=0,  xLHigh=0, yLLow=0, yLHigh=0,
                                       xSLow=0,  xSHigh=0, ySLow=0, ySHigh=0):
        self.imageL = imageL
        self.imageS = imageS
        #self._kSize = kSize
        self._xLLow = xLLow
        self._yLLow = yLLow
        self._xLHigh = xLHigh
        self._yLHigh = yLHigh
        self._xSLow = xSLow
        self._ySLow = ySLow
        self._xSHigh = xSHigh
        self._ySHigh = ySHigh

        # def onchangeKernelSize(pos):
        #     if pos == 0 or pos == 2 or pos == 4 or pos == 6:
        #         pass
        #     else:
        #         self._kernelSize = pos
        #         self._render()

        def onchangeXLLow(pos):
            self._xLLow = pos
            self._render()

        def onchangeYLLow(pos):
            self._ylLow = pos
            self._render()

        def onchangeXLHigh(pos):
            self._xlHigh = pos
            self._render()

        def onchangeYLHigh(pos):
            self._yLHigh = pos
            self._render()

        def onchangeXSLow(pos):
            self._xSLow = pos
            self._render()

        def onchangeYSLow(pos):
            self._ySLow = pos
            self._render()

        def onchangeXSHigh(pos):
            self._xSHigh = pos
            self._render()

        def onchangeYSHigh(pos):
            self._ySHigh = pos
            self._render()

        cv2.namedWindow('dSob')
        cv2.namedWindow('dBars')

        #cv2.createTrackbar('kernelSize', 'sSob', self._kSize, 7, onchangeKernelSize)
        cv2.createTrackbar('xLLow', 'dBars', self._xLLow, 255, onchangeXLLow)
        cv2.createTrackbar('xLHigh', 'dBars', self._xLHigh, 255, onchangeXLHigh)
        cv2.createTrackbar('yLLow', 'dBars', self._yLLow, 255, onchangeYLLow)
        cv2.createTrackbar('yLHigh', 'dBars', self._yLHigh, 255, onchangeYLHigh)
        cv2.createTrackbar('xSLow', 'dBars', self._xSLow, 255, onchangeXSLow)
        cv2.createTrackbar('xSHigh', 'dBars', self._xSHigh, 255, onchangeXSHigh)
        cv2.createTrackbar('ySLow', 'dBars', self._ySLow, 255, onchangeYSLow)
        cv2.createTrackbar('ySHigh', 'dBars', self._ySHigh, 255, onchangeYSHigh)

        self._render()

        print("Adjust the parameters as desired.  Hit any key to close.")

        cv2.waitKey(0)

        cv2.destroyWindow('dBars')
        cv2.destroyWindow('dSob')
        #cv2.destroyWindow('smoothed')

    # def kernelSize(self):
    #     return self._kernelSize

    def xLLow(self):
        return self._xLLow

    def yLLow(self):
        return self._yLLow

    def xLHigh(self):
        return self._xLHigh

    def yLHigh(self):
        return self._yLHigh

    def xSLow(self):
        return self._xSLow

    def ySLow(self):
        return self._ySLow

    def xSHigh(self):
        return self._xSHigh

    def ySHigh(self):
        return self._ySHigh

    def dSobImage(self):
        return self._dSob_img

    def _render(self):
        sobelx = cv2.Sobel(self.imageL, cv2.CV_64F, 1, 0)
        abs_sobelx = np.absolute(sobelx) # Absolute x derivative to accentuate lines away from horizontal
        scaled_sobel = np.uint8(255*abs_sobelx/np.max(abs_sobelx))

        sxbinary = np.zeros_like(scaled_sobel)
        sxbinary[(scaled_sobel >= self._xLLow) & (scaled_sobel <= self._xLHigh)] = 1

        sobely = cv2.Sobel(self.imageL, cv2.CV_64F, 0, 1)
        abs_sobely = np.absolute(sobely) # Absolute x derivative to accentuate lines away from horizontal
        scaled_sobel = np.uint8(255*abs_sobely/np.max(abs_sobely))

        sybinary = np.zeros_like(scaled_sobel)
        sybinary[(scaled_sobel >= self._yLLow) & (scaled_sobel <= self._yLHigh)] = 1

        wraped2 = np.copy(cv2.bitwise_or(sxbinary,sybinary))
        wraped2 *= 255

        sobelx = cv2.Sobel(self.imageS, cv2.CV_64F, 1, 0)
        abs_sobelx = np.absolute(sobelx) # Absolute x derivative to accentuate lines away from horizontal
        scaled_sobel = np.uint8(255*abs_sobelx/np.max(abs_sobelx))

        sxbinary = np.zeros_like(scaled_sobel)
        sxbinary[(scaled_sobel >= self._xSLow) & (scaled_sobel <= self._xSHigh)] = 1

        sobely = cv2.Sobel(self.imageS, cv2.CV_64F, 0, 1)
        abs_sobely = np.absolute(sobely) # Absolute x derivative to accentuate lines away from horizontal
        scaled_sobel = np.uint8(255*abs_sobely/np.max(abs_sobely))

        sybinary = np.zeros_like(scaled_sobel)
        sybinary[(scaled_sobel >= self._ySLow) & (scaled_sobel <= self._ySHigh)] = 1

        wraped3 = np.copy(cv2.bitwise_or(sxbinary,sybinary))
        wraped3 *= 255

        color_binary = np.dstack(( np.zeros_like(wraped2), wraped2, wraped3))

        self._dSob_img = cv2.cvtColor(color_binary, cv2.COLOR_BGR2RGB)
        cv2.imshow('dSob', self._dSob_img)