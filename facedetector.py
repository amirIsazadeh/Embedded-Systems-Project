import cv2 as cv
import mediapipe as mp

def detect_face():
    mp_face_detection = mp.solutions.face_detection
    cam = cv.VideoCapture(0)
    # reading the input using the camera
    _, image = cam.read()
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        if not results.detections:
            return 0
        ditection = results.detections[0]
        return (ditection.location_data.relative_bounding_box.height + ditection.location_data.relative_bounding_box.width)