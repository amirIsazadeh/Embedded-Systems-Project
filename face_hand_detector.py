import cv2 as cv
import mediapipe as mp

def detect_face():
    mp_face_detection = mp.solutions.face_detection
    mp_hands = mp.solutions.hands
    cam = cv.VideoCapture(0)
    # reading the input using the camera
    _, image = cam.read()
    face = 0
    hand = 0
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.multi_hand_landmarks:
            hand = False
        else:
            hand = True

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        if not results.detections:
            face = 0
        else:
            ditection = results.detections[0]
            face = ditection.location_data.relative_bounding_box.height + ditection.location_data.relative_bounding_box.width
    return hand, face


    
  
    
