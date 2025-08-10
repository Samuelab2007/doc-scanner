import cv2 as cv
import numpy as np

def binarize(img):
    assert img is not None, "File could not be read"

    _, th_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) 
    return th_img 

def remove_content(img, kernel_size, iterations):
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (kernel_size, kernel_size))
    no_content = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel=kernel, iterations=iterations)
    return no_content



# TODO: Histogram equalization
