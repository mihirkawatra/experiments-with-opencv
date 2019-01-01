'''
cv2.get(propId) –
Property identifier. It can be one of the following:

CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
CV_CAP_PROP_FPS Frame rate.
CV_CAP_PROP_FOURCC 4-character code of codec.
CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
CV_CAP_PROP_HUE Hue of the image (only for cameras).
CV_CAP_PROP_GAIN Gain of the image (only for cameras).
CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)
'''

import cv2

def main():
    WindowName = "STREAM"
    cap = cv2.VideoCapture(0)
    # cap.set(3,1280)
    # cap.set(4,960)
    # filename = './output.mp4'
    # codec = cv2.VideoWriter_fourcc('X','V','I','D')
    # framerate = 30
    # resolution = 640,480
    # output = cv2.VideoWriter(filename,codec,framerate,resolution)
    if cap.isOpened():
        ret,frame = cap.read()

    else:
        ret = False

    while ret:
        ret,frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)

        fps = cap.get(cv2.CAP_PROP_FPS)
        cv2.putText(frame,str(fps),(int(cap.get(3))-100,int(cap.get(4))-100),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))


        #output.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow(WindowName,frame)
        cv2.imshow('GRAY STREAM',gray)
        if(cv2.waitKey(1)>0):
            break

    cv2.destroyWindow(WindowName)
    cap.release()
    output.release()

if __name__ == '__main__':
    main()
