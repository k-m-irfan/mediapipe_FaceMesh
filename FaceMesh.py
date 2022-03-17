#python version 3.9.7
#opncv-python version = 4.5.4.60
#mediapipe version = 0.8.9.1

import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
# cam = cv2.VideoCapture("http://192.168.1.2:4747/video")# connecting to ip cam
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(width,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceMesh = mp.solutions.face_mesh.FaceMesh(False,1,True,0.5,0.5)
mpDraw = mp.solutions.drawing_utils
drawSpecCircle = mpDraw.DrawingSpec(thickness=1,circle_radius = 1, color=(0,255,0))
drawSpecLine = mpDraw.DrawingSpec(thickness=1,circle_radius = 1,color=(255,0,0))

while True:
    _, frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(frameRGB)
    if results.multi_face_landmarks != None:
        for faceLandmarks in results.multi_face_landmarks:
            # connections= mp.solutions.face_mesh_connections.FACEMESH_LIPS
            # connections= mp.solutions.face_mesh_connections.FACEMESH_LEFT_EYE
            # connections= mp.solutions.face_mesh_connections.FACEMESH_LEFT_IRIS
            # connections= mp.solutions.face_mesh_connections.FACEMESH_LEFT_EYEBROW
            # connections= mp.solutions.face_mesh_connections.FACEMESH_RIGHT_EYE
            # connections= mp.solutions.face_mesh_connections.FACEMESH_RIGHT_IRIS
            # connections= mp.solutions.face_mesh_connections.FACEMESH_RIGHT_EYEBROW
            # connections= mp.solutions.face_mesh_connections.FACEMESH_FACE_OVAL
            connections= mp.solutions.face_mesh_connections.FACEMESH_TESSELATION
            mpDraw.draw_landmarks(frame,faceLandmarks,connections,drawSpecCircle,drawSpecLine)
    cv2.imshow('Mesh', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        print('end')
        break
cam.release()
cv2.destroyAllWindows()
