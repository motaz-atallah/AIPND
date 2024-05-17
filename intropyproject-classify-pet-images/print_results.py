#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Motaz Atallah
# DATE CREATED: 5/17/2024
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    # Print summary information
    print_summary(results_stats_dic, model)
    
    # Print percentage calculations
    print_percentages(results_stats_dic)
    
    # Print misclassified dogs if requested
    if print_incorrect_dogs and results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']:
        print_misclassified_items(results_dic, misclassified_dogs_condition, "\n** Misclassified Dogs: ")
    
    # Print misclassified breeds if requested
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print_misclassified_items(results_dic, misclassified_breeds_condition, "\n** Misclassified Breed's of Dog: ")
    
def print_summary(results_stats_dic, model):
    """
    Prints summary information about the classification results.

    Parameters:
        results_stats_dic - Dictionary containing statistics on the
            results (dict)
        model - Indicates which CNN model architecture was used (str)

    Returns:
        None - Since printing is the main purpose of the function, no return value is needed.
    """

    print(f"\n** Using the {model.title()} CNN Model Architecture: ")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a' Dog Images: {results_stats_dic['n_notdogs_img']}")
    
    
def print_percentages(results_stats_dic):
    """
    Print percentage calculations based on the results statistics.

    Parameters:
        results_stats_dic - A dictionary containing statistics on the results (dict)

    Returns:
        None - Since printing is the main purpose of the function, no return value is needed.
    """
    # Create a mapping dictionary for the desired output names
    mapping = {
            'pct_correct_dogs': "Correct Dogs",
            'pct_correct_breed': "Correct Breed",
            'pct_correct_notdogs': "Correct \"Not-a\" Dog",
            'pct_match': "Match"
            }
    
    print("\n** Percentage Calculations: ")
    for key, value in results_stats_dic.items():
        if key.startswith('pct_'):
            print(f"{value}%  {mapping.get(key)}")
            

def misclassified_dogs_condition(value):
    """
    Condition function to check if the item is a misclassified dog.

    Parameters:
        value - A list containing pet image label, classifier label, match labels, 
            pet image is a dog, classifier is a dog (list)

    Returns:
        bool - True if the item is a misclassified dog, False otherwise.
    """
    return sum(value[3:]) == 1

def misclassified_breeds_condition(value):
    """
    Condition function to check if the item is a misclassified breed.

    Parameters:
        value - A list containing pet image label, classifier label, match labels, 
            pet image is a dog, classifier is a dog (list)
            
    Returns:
        bool - True if the item is a misclassified breed, False otherwise.
    """
    return sum(value[3:]) == 2 and value[2] == 0


def print_misclassified_items(results_dic, condition_func, message):
    """
    Prints misclassified items based on a given condition.

    Parameters:
        results_dic : Dictionary with image filenames as keys and lists
            containing pet image label, classifier label, match status, and
            dog status as values (dict)
        condition_func - A function that takes a value from results_dic
            as arguments and returns True if the item should be printed, False otherwise (function)
        message - Message to print before each misclassified item (str)

    Returns:
        None - Since printing is the main purpose of the function, no return value is needed.
    """

    print(message)
    for value in results_dic.values():
            if condition_func(value):
                    print(f'Pet image label is "{value[0].title()}" and Classifier labels are "{value[1].title()}"')