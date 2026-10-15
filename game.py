import mediapipe as mp
import cv2
import pyautogui

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def is_finger_down(landmarks, finger_tip, finger_mcp):
    return landmarks[finger_tip].y > landmarks[finger_mcp].y
with mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.9, max_num_hands = 1) as hands:
    finger_states = [False] * 5 

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            for h, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                finger_tips = [8, 12, 16, 20]
                finger_mcps = [5, 9, 13, 17] 
                for i in range(4):
                    if i == 0:
                        finger_index = i+h*4
                    if is_finger_down(hand_landmarks.landmark, finger_tips[i], finger_mcps[i]):
                        if not finger_states[finger_index]:
                            finger_states[finger_index] = True
                            pyautogui.press('space')
                    else:
                        if finger_states[finger_index]:
                            finger_states[finger_index] = False
        cv2.imshow("Test", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()