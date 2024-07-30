import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
from datetime import datetime
import streamlit as st
import webbrowser

path = 'images' #training images
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')  #reads img from given path
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    
    for img in images:
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    #Convert BGR and RGB with OpenCV function cvtColor()
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)         
    return encodeList


def markAttendance(name):
    
    p=pd.read_csv('att.csv') #the csv file for marking attendance
    #print(p)
    
    name_idx = p['name'].tolist().index(name)
    p.loc[name_idx, 'attendance'] += 1
    
    now = datetime.now()
    date, time = now.strftime("%d-%m-%Y %H:%M:%S").split(' ')
    p.loc[name_idx, 'time'] = time
    
    if date!=p.loc[name_idx, 'date']:
        p.loc[name_idx, 'date'] = date
        p.loc[name_idx, 'days'] += 1
    
    p.to_csv("att.csv", index=False)


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

c=0
while True:
    name ="UNKNOWN"
    _, img = cap.read()
    matchIndex=-1
    
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS) #Returns an array of bounding boxes of human faces in a image
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame) #Given an image, return the 128-dimension face encoding for each face in the image.

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace) # Compare a list of face encodings against a candidate encoding to see if they match.
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace) # Given a list of face encodings, compare them to a known face encoding and get a euclidean distance for each comparison face. The distance tells you how similar the faces are.
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            c=1

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img,name,(x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Face Recognition Based Attendance System',img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        
        if name !="UNKNOWN":
            print(name)
            webbrowser.open_new_tab("http://localhost:8502/voting")
        else:
            print(name)
            webbrowser.open_new_tab("http://localhost:8501/another_page")
        if c==1:
            markAttendance(name)
           
        cap.release()
        cv2.destroyAllWindows()
        break
   
    

