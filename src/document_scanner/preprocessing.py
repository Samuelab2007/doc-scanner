import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def binarize(img):
    assert img is not None, "File could not be read"

    _, th_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) 
    return th_img 

def remove_content(img, kernel_size, iterations):
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (kernel_size, kernel_size))
    no_content = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel=kernel, iterations=iterations)
    return no_content

def find_histogram(img):
    plt.hist(img.ravel(),256,[0,256])
    plt.savefig("new_diploma_histogram.png")

def equalize_hist(img):
    # CLAHE method for histogram equalization(locally)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    return cl1