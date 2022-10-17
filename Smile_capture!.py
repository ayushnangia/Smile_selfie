

from imutils.video import VideoStream
from imutils import face_utils

import pygame,dlib,time,cv2,os
pygame.init()

shape_predictor="shape_predictor_face_landmarks.dat" 

print("[INFO] loading facial landmark predictor")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)
print("[INFO] camera sensor starting up")
print("[INFO] Please hold your smile for 2 seconds or try again!!")

time.sleep(2.0)


video = VideoStream(src=0).start()
path="./output/"
time.sleep(2.0)
j=0
p=[(0,0)]*68
p1=[(0,0)]*68
d=[(0,0)]*68
dist_smil=0
dist_leyeo=0
dist_reyeo=0
dist_ango=0
dup1,dup2=0,0
diff_chx,diff_chy=0,0
pid=0
count_smile,count_eact,count_be=0,0,0
# loop over the frames from the video stream
while True:
        pic = video.read()
        gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        diff_smile=0
        diff_ang=0
        diff_leye=0
        diff_eye=0
        diff_reye=0
        diff_up=0
        diff_change=0
        if j%2==0:
                p=p1
                p1=[(0,0)]*68
                d=[(0,0)]*68
        cv2.imshow("Frame", pic)
        # loop over the face detections
        x49=0
        y49=0
        x55=0
        y55=0
        x23=0
        y23=0
        x22=0
        y22=0
        x38=0
        y38=0
        x41=0
        y41=0
        x44=0
        y44=0
        x47=0
        y47=0
        print('count_eact,count_smile,count_be',count_eact,count_smile,count_be)
        
        e,s,le,re,be=0,0,0,0,0
        for rect in rects:
               
                

                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                i=1
                print('iter'+str(j))
                x1,y1,w,h=0,0,0,0
                j=j+1
                for (x, y) in shape:
                        
                        cv2.circle(pic, (x, y), 1, (0, 0, 255), -1)

                        
                        if i==1:
                                x1=x
                                y1=y-40
                                
                                
                                if j%2!=0:
                                        dup1=x1
                                        dup2=y1
                                        diff_chx,diff_chy=0,0
                                else:
                                        diff_chx=dup1-x1
                                       
                                        diff_chy=dup2-y1
                                        
                                

                        elif i==9:
                                h=y-y1
                        elif i==17:
                                w=x-x1

                        elif i==20:
                                if j%2!=0:
                                        y_20=y-y1
                                        print(y_20)
                                else:
                                        y20=y-y1
                                        diff_up=y_20-y20
                                        print(y20,diff_up)
                                        
                                
                        
                        elif(i==49):
                                x49=x
                                y49=y
                        elif(i==55):
                                x55=x
                                y55=y

                                dist_smile=((x49-x55)**2+(y49-y55)**2)**0.5
                                print('dist-smile',dist_smile)
                                diff_smile=(dist_smile)-dist_smil
                                if diff_smile<0:
                                        diff_smile*=-1

                                print('diff-smile',diff_smile)
                                
                                print('dist-smilo',dist_smil)
                                if j==1 or diff_smile>15:
                                        dist_smil=dist_smile
                                        
                                        
                                if diff_smile<6:
                                        dist_smil=(dist_smil+dist_smile)//2

                        elif(i==38):
                                x38=x
                                y38=y
                        elif(i==41):
                                x41=x
                                y41=y
                                dist_leye=((x38-x41)**2+(y38-y41)**2)**0.5
                                print('dist-lefteye',dist_leye)
                                diff_leye=(dist_leye)-dist_leyeo

                                if diff_leye<0:
                                        diff_leye=diff_leye*-1

                                print('diff-leye',diff_leye)
                                
                                print('dist-leyeo',dist_leyeo)
                                if j==1 or diff_leye>2:
                                        dist_leyeo=dist_leye
                                        
                                        
                                if diff_leye<1:
                                        dist_leyeo=(dist_leyeo+dist_leye)//2                                
                        elif(i==44):
                                x44=x
                                y44=y
                        elif(i==47):
                                x47=x
                                y47=y
                                dist_reye=((x44-x47)**2+(y44-y47)**2)**0.5
                                print('dist-reye',dist_reye)
                                diff_reye=(dist_reye)-dist_reyeo

                                if diff_reye<0:
                                        diff_reye=diff_reye*-1

                                print('diff-reye',diff_reye)
                                
                                print('dist-reyeo',dist_reyeo)
                                if j==1 or diff_reye>2:
                                        dist_reyeo=dist_reye
                                print('check both')
                                print(diff_leye,diff_reye)
                                diff=(dist_reye-dist_leye)-(dist_reyeo-dist_leyeo)
                                if diff<0:
                                        diff=diff*-1
                                if diff_leye+diff_reye>2 and diff_leye+diff_reye<4 and (diff<0.5):
                                        print('check both')
                                        diff_eye=1
                                        
                                
                                        
                                if diff_reye<1:
                                        dist_reyeo=(dist_reyeo+dist_reye)//2   
        
                        
                        
                       
                        
                        
                        if diff_chx<10 and diff_chy<10:
                                
                                if diff_smile>10 and diff_smile<50 and j!=1:
                                        
                                        s=1
                                        
                                        
                                        
                                        fr = video.read()
                                        cv2.putText(pic,'Smile', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        cv2.imshow("selfie", fr)
                                        cv2.imwrite(path+"selfie"+str(count_smile)+".jpg", fr) 
                                     

                                elif diff_up>3:
##                                        cv2.putText(pic,'eye act', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        e=1

                                elif diff_eye==1:
                                        
                                        #cv2.putText(pic,'Botheye', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        print('Botheye')
                                        be=1

                                       
                                elif diff_leye>2.5 and diff_leye<5:
                                        
                                        pid=os.getpid()
                                        print(pid)
                                        
                                        
                                        le=1
                                        
                                        

                                elif diff_reye>2.5 and diff_reye<5:
                                        
                                        re=1
                                    

                        i=i+1

        if e:
                            
                print('eye act')
                count_eact=count_eact+1
        elif s:
                print('smile')
                count_smile=count_smile+1
        
        elif be:
                print('Bothe')
                count_be=count_be+1
        elif le:
                h=1

        cv2.imshow("Frame", pic)
       
        key = cv2.waitKey(1) & 0xFF
        
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
 
# cleanup
VideoStream(src=0).stop()
cv2.destroyAllWindows()


