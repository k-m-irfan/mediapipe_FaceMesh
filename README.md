# Mediapipe_FaceMesh

Here -> https://github.com/k-m-irfan/simplified_mediapipe_face_landmarks, I tried to isolate and simplify face landmarks for selecting points around specific facial features (eyes, iris, eyebrows, lips and, face boundary). But there's an inbuilt and easier way. We can use the connections argument of the draw_landmarks function of drawing_utils. We can even manually list the points of interest here.

<p align="center"> <img src="https://user-images.githubusercontent.com/80172338/158805135-9ccb68ad-0d23-4645-8ebf-b8fcdb3eda89.gif"> </p>

<p align="center"> <img src="https://user-images.githubusercontent.com/80172338/158795291-4aa3036f-3fa5-486b-94d1-90a16b4e4aee.png"> </p>

- **For Lips:** ```mp.solutions.face_mesh_connections.FACEMESH_LIPS```

- **Left Eye:** ```mp.solutions.face_mesh_connections.FACEMESH_LEFT_EYE```

- **Left Iris:** ```mp.solutions.face_mesh_connections.FACEMESH_LEFT_IRIS```

- **Left Eyebrow:** ```mp.solutions.face_mesh_connections.FACEMESH_LEFT_EYEBROW```

- **Right Eye:** ```mp.solutions.face_mesh_connections.FACEMESH_RIGHT_EYE```

- **Right Iris:** ```mp.solutions.face_mesh_connections.FACEMESH_RIGHT_IRIS```

- **Right Eyebrow:** ```mp.solutions.face_mesh_connections.FACEMESH_RIGHT_EYEBROW```

- **Face Boundary:** ```mp.solutions.face_mesh_connections.FACEMESH_FACE_OVAL```

- **Full face mesh:** ```mp.solutions.face_mesh_connections.FACEMESH_TESSELATION```

## Environment

 - python version 3.9.7
 - opncv-python version = 4.5.4.6
 - mediapipe version = 0.8.9.1
