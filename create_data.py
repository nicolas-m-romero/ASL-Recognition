import os
import pickle
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import random as r

#! This file is used to apply the landmarks to the images in the dataset
#! The landmarks are then saved to a pickle file to be used in the model training

#* Path to the directory containing the data
data_directory = "C:/AI4ALL/ASL_Alphabet_Dataset/asl_alphabet_train"

#* Imports to help draw landmarks on images
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)

#* Set random seed
r.seed(414411)

#* Lists to store the data for the landmarks (x,y) and the labels for each image (sign)
data = []
labels = []

#* Loop through each individual sign directory in the data directory
for dir in os.listdir(data_directory):
    #* Loop through each image in the sign directory
    for img_path in os.listdir(os.path.join(data_directory, dir))[1]:
        if labels.count(dir) < 600: #* Check if you have processed 300 images for the current sign

            #* limit the number of images to 10& of original dataset ~ 300 images per sign
            #* this is to reduce the size of the dataset to make it easier to work with
            #* 10% of original dataset per hnd sign
            if (r.random() > 0.2):
                continue

            #* Temp list to store coordinate pairs for each landmark
            coords = []
            #* List to store the x and y coordinates of each landmark
            x_list = []
            y_list = []

            #* Read in the image and convert to RGB
            img = cv2.imread(os.path.join(data_directory, dir, img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            hands_results = hands.process(img_rgb)
            #* Check if hands were detected in the image
            if hands_results.multi_hand_landmarks:
                #* Loop through each landmark detected on the hand
                for hand_landmarks in hands_results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        #* Get x and y coordinates of each landmark 
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        #* Append the x and y coordinates to the x and y list
                        coords.append(x)
                        coords.append(y)
                    
                    # for i in range(len(hand_landmarks.landmark)):
                    #     x = hand_landmarks.landmark[i].x
                    #     y = hand_landmarks.landmark[i].y

                    #     #* Append the x and y coordinates to the coords list
                    #     coords.append(x - min(x_list))
                    #     coords.append(y - min(y_list))

                #* Append the labels list to the data list
                data.append(coords)
                labels.append(dir)
        else: #* Break out of the loop and move to next sign directory if 300 images have been processed
            break

# p = open("data.pickle", "wb")
# pickle.dump({'data': data, 'labels': labels}, p)
# p.close()