import cv2 as cv
from document_scanner import contours, preprocessing, transform, utils

def process_basic(image_path:str, debug:bool = False):
    """
    Full pipeline to process a document image:
    - Grayscale + equalize histogram
    - Binarize + morphological operations
    - Find contours & corners
    - Warp perspective to obtain corrected page
    Returns the corrected (warped) document image.
    """

    # Load image
    img = utils.read_img(image_path)

    # Step 1: Grayscale
    gray_image = utils.convert_grayscale(img)
    if debug: utils.show_img("Grayscale", gray_image)

    # Step 2: Histogram equalization
    gray_image = preprocessing.equalize_hist(gray_image)
    if debug: utils.show_img("Equalized", gray_image)

    # Step 3: Binarize
    binary_img = preprocessing.binarize(gray_image)
    if debug: utils.show_img("Binarized", binary_img)

    # Step 4: Morphological ops (optional — currently a no-op)
    empty = binary_img  # or: preprocessing.remove_content(binary_img, 5, 15)

    # Step 5: Contours & corners
    page_contour = contours.get_page_contour(empty)
    corners = contours.find_corners(page_contour)

    # Step 6: Perspective transform
    rect = contours.reorder_points(corners)
    dst, max_w, max_h = contours.find_destination_points(rect)
    warped = transform.warp_perspective(img, rect, dst, max_w, max_h)

    if debug: utils.show_img("Corrected image", warped)

    return warped