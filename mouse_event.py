import cv2
import numpy as np

win = 'Interactive Drawing'
cv2.namedWindow(win)
image = np.zeros((512,512,3),np.uint8)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #cr = tuple(np.random.randint(255,size=3))
        cr = (np.random.randint(255),np.random.randint(255),np.random.randint(255))
        cv2.circle(image, (x,y), 40, cr,-1)

cv2.setMouseCallback(win,draw_circle)

def main():
    while(True):
        cv2.imshow(win, image)
        if(cv2.waitKey(1)>0):
            break

if __name__ == '__main__':
    main()
