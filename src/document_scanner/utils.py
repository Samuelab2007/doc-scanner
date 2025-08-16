import cv2 as cv
from document_scanner import contours, preprocessing, transform

def read_img(pathname):
    img = cv.imread(pathname, cv.IMREAD_COLOR_BGR)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}")
    return img 

def copy_img(img):
    return img.copy()

def save_img(path, img):
    return cv.imwrite(path, img)

def convert_grayscale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def show_img(title, img):
    cv.imshow(f"{title}", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
