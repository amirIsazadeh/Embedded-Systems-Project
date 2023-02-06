import cv2
import mediapipe as mp

def detect_hand():
  mp_hands = mp.solutions.hands
  cam = cv2.VideoCapture(0)
  _, image = cam.read()
  with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
      results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      if not results.multi_hand_landmarks:
        return False
      return True
print(detect_hand())