#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Motaz Atallah
# DATE CREATED: 5/16/2024                                
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether the pet image label is of-a-dog,
#          and to indicate whether the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names, then the label
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively, one
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            - The results' dictionary as results_dic within adjust_results4_isadog
#             function and results for the function call within main.
#            - The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results' dictionary. You will be adding the
#           whether the pet image label is of-a-dog as the item at index
#           3 of the list and whether the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
        results_dic - Dictionary with 'key' as image filename and 'value' as a
                        List. Where the list will contain the following items:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int)  where 1 = match between pet image
                        and classifier labels and 0 = no match between labels
                    ------ where index 3 & index 4 are added by this function -----
                     NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                                0 = pet Image 'is-NOT-a' dog.
                     NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image
                                'as-a' dog and 0 = Classifier classifies image
                                'as-NOT-a' dog.
        dogfile - A text file that contains names of all dogs from the classifier
                   function and dog names from the pet image files. This file has
                   one dog name per line dog names are all in lowercase with
                   spaces separating the distinct words of the dog name. Dog names
                   from the classifier function can be a string of dog names separated
                   by commas when a particular breed of dog has multiple dog names
                   associated with that breed (ex. maltese dog, maltese terrier,
                   maltese) (string - indicates text file's filename)
    Returns:
        None - results_dic is mutable data type so no return needed.
    """
    # Creates empty dictionary named dognames_dic to store dog names from the dog file
    dognames_dic = dict()

    # Read dog names from the dog file and populate the dictionary &
    # automatically closes file
    with open(dogfile, 'r') as file:

        # Processes each line in file until reaching EOF (end-of-file) by
        # processing line and adding dognames to dognames_dic with while loop
        for dog_name_line in file:

            # Process line by striping newline from line
            dog_name = dog_name_line.rstrip()

            # Adds dogname(line) to dogsnames_dic if it doesn't already exist, otherwise print warning
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(
                    f"** Warning: {dog_name} dog name already exists in dognames_dic with value = {dognames_dic[dog_name]}")

    # Iterate through each entry value in the results dictionary to extend the dog classification 
    # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    for value in results_dic.values():
        # Extract labels values from the results dic and assign the variables
        pet_image_label, classifier_labels = value[0], value[1]

        # Check if pet label is a dog then 1, otherwise 0
        match_pet_image_label = 1 if pet_image_label in dognames_dic else 0

        # Check if classifier label is a dog then 1, otherwise 0
        match_classifier_labels = 1 if classifier_labels in dognames_dic else 0

        # Add new indices to the value list indicating dog classification
        value.extend([match_pet_image_label, match_classifier_labels])
