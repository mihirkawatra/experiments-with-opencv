import cv2
import matplotlib.pyplot as plt

def main():

    cap=cv2.VideoCapture(0)
    ret,frame = cap.read()

    while ret:
        ret,frame = cap.read()


        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(gray, 75, 255, 0)

        img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if(len(contours)):
            c = max(contours, key=cv2.contourArea)
        else:
            c = contours
    #    print(contours)
    #    print(hierarchy)

        cv2.drawContours(img, c, -1, (0, 0, 255), 2)

        original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow("ORIGINAL",original)
        cv2.imshow("CONTOURS",img)
if __name__ == "__main__":
    main()
