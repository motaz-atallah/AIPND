#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Motaz Atallah
# DATE CREATED: 5/15/2024                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


#       in the return statement with results_dic dictionary that you create
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Retrieve the filenames from folder
    filename_list = listdir(image_dir)

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for pet_image in filename_list:

        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if pet_image[0] != ".":

            # Get pet image label
            pet_name = get_pet_name(pet_image)

            # If pet image doesn't exist in dictionary add it
            # otherwise print an error message to indicates for a duplicate
            if pet_image not in results_dic:
                results_dic[pet_image] = [pet_name]
            else:
                print(
                    f"** Warning: Key={pet_image} already exists in results_dic with value = {results_dic[pet_image]}")

    # Return the expected results as dic
    return results_dic


def get_pet_name(pet_image):
    """
    Extracts and formats the pet name from the given filename.
    
    Parameters:
        pet_image - The filename of the pet image (string)
    
    Returns:
        pet_name - The formatted pet name (string)
    """
    # Convert filename to lower case and Split the filename by underscores
    list_pet_image = pet_image.lower().split("_")

    # Concatenate alphabetic words to form the pet name
    pet_name = ' '.join([word for word in list_pet_image if word.isalpha()])

    # Strip leading and trailing whitespace characters
    return pet_name.strip()
