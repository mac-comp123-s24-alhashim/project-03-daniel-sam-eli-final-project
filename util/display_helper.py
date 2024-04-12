"""
This script contains a set of functions to help with displaying images
"""
import time

from util.imageTools import *

DISPLAY_TIME = 2

def display_images(images: list[Picture]) -> None:
    """
    Display passed images after each other for the given amount of time in seconds
    """
    for image in images:
        image.show()
        time.sleep(DISPLAY_TIME)

