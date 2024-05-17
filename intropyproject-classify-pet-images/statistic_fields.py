from enum import Enum

class StatFields(Enum):
    """
    Enum for representing various statistics fields that's need for the classification.

    Attributes:
    ----------
    N_IMAGES : str
        Represents the number of images.
    N_DOGS_IMG : str
        Represents the number of dog images.
    N_NOTDOGS_IMG : str
        Represents the number of NON-dog images.
    N_MATCH : str
        Represents the number of matches between pet & classifier labels.
    N_CORRECT_DOGS : str
        Represents the number of correctly classified dog images.
    N_CORRECT_NOTDOGS : str
        Represents the number of correctly classified NON-dog images.
    N_CORRECT_BREED : str
        Represents the number of correctly classified dog breeds.
    PCT_MATCH : str
        Represents the percentage of correct matches between pet labels and classifier labels.
    PCT_CORRECT_DOGS : str
        Represents the percentage of correctly classified dogs.
    PCT_CORRECT_BREED : str
        Represents the percentage of correctly classified dog breeds.
    PCT_CORRECT_NOTDOGS : str
        Represents the percentage of correctly classified NON-dogs.
    """
    
    N_IMAGES = "n_images"
    N_DOGS_IMG = "n_dogs_img"
    N_NOTDOGS_IMG = "n_notdogs_img"
    N_MATCH = "n_match"
    N_CORRECT_DOGS = "n_correct_dogs"
    N_CORRECT_NOTDOGS = "n_correct_notdogs"
    N_CORRECT_BREED = "n_correct_breed"
    PCT_MATCH = "pct_match"
    PCT_CORRECT_DOGS = "pct_correct_dogs"
    PCT_CORRECT_BREED = "pct_correct_breed"
    PCT_CORRECT_NOTDOGS = "pct_correct_notdogs"