#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Motaz Atallah
# DATE CREATED: 5/17/2024                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the program run using the classifier's model
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 

# Imports statistic fields enum
from statistic_fields import StatFields


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """
    # Check if results_dic is empty
    if not results_dic:
        return {}

    # Creates empty dictionary named results_stats_dic to store the results statistics
    results_stats_dic = dict()

    # Calculate counts
    calculate_counts(results_dic, results_stats_dic)

    # Calculate percentages based on counts
    calculate_percentages(results_stats_dic)

    return results_stats_dic


def calculate_counts(results_dic, results_stats_dic):
    """
    Calculate various counts based on the results dictionary.

    Parameters:
      results_dic - A dictionary with image filenames as keys and result lists as values (dict)
      results_stats_dic - A dictionary containing results_stats_dic of various counts with 0 (dict)
    Returns:
      None - results_stats_dic is mutable data type so no return needed.   
    """

    # Initialize counters to zero
    n_correct_dogs = 0
    n_dogs_img = 0
    n_correct_notdogs = 0
    n_notdogs_img = 0
    n_correct_breed = 0
    n_match = 0

    # Iterates through the results_dic to compute the statistics and update counts
    for value in results_dic.values():
        label_matches, pet_is_dog, classifier_is_dog = value[2:]

        # Pet label is a dog
        if pet_is_dog:
            n_dogs_img += 1

            # Both labels are of dogs (Pet and Classifier)
            if classifier_is_dog:
                n_correct_dogs += 1

            # Pet label is a dog & labels match
            if label_matches:
                n_correct_breed += 1

        # Pet label is NOT a dog
        else:
            n_notdogs_img += 1

            # Both labels are NOT of dogs (Pet and Classifier)
            if not classifier_is_dog:
                n_correct_notdogs += 1

        # labels match
        if label_matches:
            n_match += 1

    # Update the dictionary with calculated counts
    results_stats_dic.update({
        StatFields.N_IMAGES.value: len(results_dic),
        StatFields.N_CORRECT_DOGS.value: n_correct_dogs,
        StatFields.N_DOGS_IMG.value: n_dogs_img,
        StatFields.N_CORRECT_NOTDOGS.value: n_correct_notdogs,
        StatFields.N_NOTDOGS_IMG.value: n_notdogs_img,
        StatFields.N_CORRECT_BREED.value: n_correct_breed,
        StatFields.N_MATCH.value: n_match
    })


def calculate_percentages(results_stats_dic):
    """
    Calculate various percentages based on the results_stats_dic.

    Parameters:
       results_stats_dic - A dictionary containing results_stats_dic based upon counters from above (dict)

    Returns:
       None - results_stats_dic is a mutable data type, so no return needed.
    """

    # Calculate the percentage of correctly classified dogs
    pct_correct_dogs = (results_stats_dic[StatFields.N_CORRECT_DOGS.value] / results_stats_dic[
        StatFields.N_DOGS_IMG.value]) * 100.0 if results_stats_dic[StatFields.N_DOGS_IMG.value] > 0 else 0.0

    # Calculate the percentage of correctly classified non-dogs
    pct_correct_notdogs = (results_stats_dic[StatFields.N_CORRECT_NOTDOGS.value] / results_stats_dic[
        StatFields.N_NOTDOGS_IMG.value]) * 100.0 if results_stats_dic[StatFields.N_NOTDOGS_IMG.value] > 0 else 0.0

    # Calculate the percentage of correctly classified dog breeds
    pct_correct_breed = (results_stats_dic[StatFields.N_CORRECT_BREED.value] / results_stats_dic[
        StatFields.N_DOGS_IMG.value]) * 100.0 if results_stats_dic[StatFields.N_DOGS_IMG.value] > 0 else 0.0

    # Calculate the percentage of correct matches
    pct_match = (results_stats_dic[StatFields.N_MATCH.value] / results_stats_dic[
        StatFields.N_IMAGES.value]) * 100 if results_stats_dic[StatFields.N_IMAGES.value] > 0 else 0.0

    # Update the dictionary with calculated percentages
    results_stats_dic.update({
        StatFields.PCT_CORRECT_DOGS.value: round(pct_correct_dogs, 1),
        StatFields.PCT_CORRECT_NOTDOGS.value: round(pct_correct_notdogs, 1),
        StatFields.PCT_CORRECT_BREED.value: round(pct_correct_breed, 1),
        StatFields.PCT_MATCH.value: round(pct_match, 1)
    })
