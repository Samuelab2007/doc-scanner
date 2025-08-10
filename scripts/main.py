import cv2 as cv
from document_scanner import contours, preprocessing, transform

img = cv.imread('examples/images/diploma.jpg', cv.IMREAD_GRAYSCALE)

# Binarize
binary_img = preprocessing.binarize(img)    

# Morphological operations
empty = binary_img #preprocessing.remove_content(binary_img, 5, 15)

cv.imshow("EMpty image", empty)
cv.waitKey(0)
cv.destroyAllWindows()

# Contours
contour_img = img.copy()
page_contour = contours.get_page_contour(empty)

# Corners

# Find corners and find homography matrix

corners = contours.find_corners(page_contour)

output_img = img.copy()  # make a copy of the original image

# Perform homography warp

rect = contours.reorder_points(corners)
dst, max_w, max_h = contours.find_destination_points(rect)


img = cv.imread('examples/images/diploma.jpg')

warped = transform.warp_perspective(img, rect, dst, max_w, max_h)

# Obtain only the now corrected page


# OCR



cv.imshow("Corrected image", warped)
cv.waitKey(0)
cv.destroyAllWindows()