import cv2
import numpy as np

def fun(a):
    pass
def main():
    image = np.zeros((512,512,3),np.uint8)
    win = 'Color Palette'
    cv2.namedWindow(win)

    cv2.createTrackbar('B',win,0,255,fun)
    cv2.createTrackbar('G',win,0,255,fun)
    cv2.createTrackbar('R',win,0,255,fun)

    while(True):
        cv2.imshow(win, image)

        blue = cv2.getTrackbarPos('B',win)
        green = cv2.getTrackbarPos('G',win)
        red = cv2.getTrackbarPos('R',win)
        image[:] = [blue,green,red]
        if(cv2.waitKey(1) == 27):
            break

    #cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
