from collections import deque
import numpy as np
import cv2
#Orange colour has been commented out because skin on the hands was also being classified as orange.
lower = {'red':(166, 84, 100), 'green':(66, 122, 129), 'blue':(90, 100, 117), 'yellow':(23, 59, 119)}#,'orange':(0, 50, 100)}
upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(130,255,255), 'yellow':(54,255,255)}#,'orange':(20,255,255)}

colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217)}#, 'orange':(0,140,255)}

camera = cv2.VideoCapture(0)

filename = './output.mp4'
codec = cv2.VideoWriter_fourcc('X','V','I','D')
framerate = 30
resolution = 640,480
output = cv2.VideoWriter(filename,codec,framerate,resolution)

def main():

    if camera.isOpened():
        ret, frame = camera.read()
    else:
        ret = False
    while ret:
        ret, frame = camera.read()
        frame = cv2.flip(frame, flipCode=1)

        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        for key, value in upper.items():
            kernel = np.ones((9,9),np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            c = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            if len(c) > 0:
                c = max(c, key=cv2.contourArea)

                hull = cv2.convexHull(c,returnPoints = False)
                defects = cv2.convexityDefects(c,hull)
                if(defects is not None):
                    for i in range(defects.shape[0]):
                        s,e,f,d = defects[i,0]
                        start = tuple(c[s][0])
                        end = tuple(c[e][0])
                        far = tuple(c[f][0])
                        cv2.line(frame,start,end,colors[key],2)
                        #cv2.circle(frame,far,5,colors[key],-1)

                #cv2.drawContours(frame, c, -1, colors[key], 4)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                # M = cv2.moments(c)
                # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                # cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                cv2.putText(frame,key, (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)

                fps = camera.get(cv2.CAP_PROP_FPS)
                cv2.putText(frame,str(int(fps))+" FPS",(int(camera.get(3))-150,int(camera.get(4))-50),cv2.QT_FONT_NORMAL,1,(0,0,255))

        cv2.imshow("Frame", frame)
        output.write(frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    camera.release()
    output.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
