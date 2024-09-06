import pickle
import cv2
import mediapipe as mp
import numpy as np

model_dict = pickle.load(open('./model_v1.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)

# labels_dict = {0: '_del', 1: '_space', 2: 'A', 3: 'B', 4: 'C', 
#                5: 'D', 6: 'E', 7: 'F', 8: 'G', 9: 'H', 
#                10: 'I', 11: 'J', 12: 'K', 13: 'L', 14: 'M', 
#                15: 'N', 16: 'O', 17: 'P', 18: 'Q', 19: 'R', 
#                20: 'S', 21: 'T', 22: 'U', 23: 'V', 24: 'W', 
#                25: 'X', 26: 'Y', 27: 'Z'}

while True:

    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        results = hands.process(frame_rgb)
    except:
        results = hands.process(frame_rgb)
        results += [0] * 42
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * W) - 30
        y1 = int(min(y_) * H) - 30

        x2 = int(max(x_) * W) + 30
        y2 = int(max(y_) * H) + 30

        prediction = model.predict([np.asarray(data_aux)])

        #predicted_character = labels_dict[int(prediction[0])]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, prediction[0], (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()