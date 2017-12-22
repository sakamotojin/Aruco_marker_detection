############## Task1.1 - ArUco Detection ##############

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import time

def detect_ArUco(img):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    parameters = aruco.DetectorParameters_create()
    Detected_ArUco_markers= aruco.detectMarkers(gray,aruco_dict, parameters=parameters)
    #print "function 1\n Detected aruco markers\n"
    #print Detected_ArUco_markers
    #print '\n'
    return Detected_ArUco_markers


def Calculate_orientation_in_degree(Detected_ArUco_markers):
    corners, ids, _ = Detected_ArUco_markers
    angle=[0]*len(corners)
    for i in range(0,len(corners)):
        x1=corners[i][0][0][0]
        y1=-corners[i][0][0][1]
        x2=corners[i][0][3][0]
        y2=-corners[i][0][3][1]
        v=(y1-y2)/(x1-x2)
        angle[i]=math.degrees(math.atan(v))
        if (y1-y2)<0 and (x1-x2)<0 :
          angle[i]=180+angle[i]
        elif (y1-y2)>0 and (x1-x2)<0 :
          angle[i]=180 +angle[i]
        elif (y1-y2)<0 and (x1-x2)>0 :
          angle[i]=360+angle[i]
        else :
          angle[i]=angle[i]
            #if()
            #if angle[i]
            #ArUco_marker_angles = {ids[i]:angle}
            #print "\nin angle calculation\n "
            #print  angle
            #print '\n'
    return 	angle

def mark_ArUco(img,Detected_ArUco_markers,angle):
    corners, ids, _ = Detected_ArUco_markers
        #aruco.drawDetectedMarkers(img,corners,ids)
        #c1=corners[0][0][0]
        #print "\n---------------------\n"
        #print c1
        #print "\n---------------------\n"
        #print len(corners)
        #print ids[0][0]
    print angle
    for i in range(0,len(corners)):
        #print corners[i]
        #print len(corners[i])
        #aruco.drawDetectedCornersCharuco(img,corners[i])
        c1=corners[i][0][0]
        c2=corners[i][0][1]
        c3=corners[i][0][2]
        c4=corners[i][0][3]
        cv2.circle(img,(c1[0],c1[1]),5,(125,125,125),-1)
        cv2.circle(img,(c2[0],c2[1]),5,(0,255,0),-1)
        cv2.circle(img,(c3[0],c3[1]),5,(180,105,255),-1)
        cv2.circle(img,(c4[0],c4[1]),5,(255,255,255),-1)
        r1=int((c1[0]+c2[0]+c3[0]+c4[0])/4)
        r2=int((c1[1]+c2[1]+c3[1]+c4[1])/4)
        cv2.circle(img,(r1,r2),5,(0,0,255),-1)
        p2x=int((c1[0]+c2[0])/2)
        p2y=int((c1[1]+c2[1])/2)
        add1=int(math.sqrt(math.pow((r1-c1[0]),2)+math.pow((r2-c1[1]),2)))
        idsprint=str(ids[i][0])
        angleprint=str(int(angle[i]))
        cv2.line(img,(r1,r2),(p2x,p2y),(255,0,0),3)
        cv2.putText(img,idsprint,(r1+int(add1/2),r2),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),3,cv2.LINE_AA)
        cv2.putText(img,angleprint,(r1-int(add1/1.5),r2),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),3,cv2.LINE_AA)
    return img

cam = cv2.VideoCapture(0)
test_num = 1
while(True):
    _,img = cam.read()
    Detected_ArUco_markers = detect_ArUco(img)									## detecting ArUco ids and returning ArUco dictionary
    angle = Calculate_orientation_in_degree(Detected_ArUco_markers)			## finding orientation of aruco with respective to the menitoned scale in Problem_statement.pdf
    rimg = mark_ArUco(img,Detected_ArUco_markers,angle)						## marking the parameters of aruco which are mentioned in the Problem_Statement.pdf
    #result_image = "../Test_images/Result_image"+str(test_num)+".png"
    #cv2.imwrite(result_image,img)
    cv2.imshow('result',rimg)
    cv2.waitKey(27)									## saving the result image
    test_num = test_num +1
cam.release()
cv2.destroyAllWindows()
