# import cv2
#
# frameWidth = 640
# frameHeight = 360
#
# cap =cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     cv2.waitKey(1)


import cvzone
import cv2
from cvzone.ColorModule import ColorFinder
import socket
# frameWidth = 640
# frameHeight = 360

cap = cv2.VideoCapture(00)  # Always set Videocapture to 0
cap.set(3, 1280)
cap.set(4, 720)

success, img = cap.read()
h, w, _ = img.shape

myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 62, 'smin': 80, 'vmin': 172, 'hmax': 96, 'smax': 255, 'vmax': 255}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5053)


while True:
    success, img = cap.read()
    imgColor, mask = myColorFinder.update(img ,hsvVals)
    imgContour, contours =  cvzone.findContours(img, mask, minArea=2000)

    if contours:
        data = contours[0]['center'][0],\
               h-contours[0]['center'][1], \
               int(contours[0]['area'])
        print(data)

        sock.sendto(str.encode(str(data)), serverAddressPort)

    # imgStack = cvzone.stackImages([img, imgColor, mask, imgContour], 2, 0.5)
    # cv2.imshow("Image", imgStack)

    imgContour = cv2.resize(imgContour, (0, 0), None, 0.4, 0.4)
    cv2.imshow("ImageContour", imgContour)
    cv2.waitKey(1)