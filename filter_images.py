import os
import random as r

#* Path to the directory containing the data
data_directory = "C:/AI4ALL/ASL_Alphabet_Dataset/asl_alphabet_train"

#* Path to the directory where the filtered images will be saved
DATA_DIR = './Filtered_Images'
#* Create the directory if it does not exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#* List to store the labels for each sign (Subdirectories in the data directory)
signs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U','V','W','X','Y','Z']

for sign in signs:
    if not os.path.exists(os.path.join(DATA_DIR, signs[j])):
        os.makedirs(os.path.join(DATA_DIR, signs[j]))

    print('Collecting data for class {}'.format(signs[j]))


#! This file is used to apply the landmarks to the images in the dataset
#! The landmarks are then saved to a pickle file to be used in the model training

#* Path to the directory containing the data
data_directory = "C:/AI4ALL/ASL_Alphabet_Dataset/asl_alphabet_train"

#* Set random seed
r.seed(414411)

#* Loop through each individual sign directory in the data directory
for dir in os.listdir(data_directory):
    #* Loop through each image in the sign directory
    for img_path in os.listdir(os.path.join(data_directory, dir))[1]:
        if labels.count(dir) < 300: #* Check if you have processed 300 images for the current sign

            #* limit the number of images to 10% of original dataset ~ 300 images per sign
            #* this is to reduce the size of the dataset to make it easier to work with
            #* 10% of original dataset per hand sign
            if (r.random() > 0.2):
                continue

                #* Append the labels list to the data list
                data.append(coords)
                labels.append(dir)
        else: #* Break out of the loop and move to next sign directory if 300 images have been processed
            break
