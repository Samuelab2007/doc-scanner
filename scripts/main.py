import cv2 as cv
from document_scanner import contours, preprocessing, transform, ocr

img = cv.imread('examples/images/libro.jpg', cv.IMREAD_COLOR_BGR)
# Use the cvtColor() function to grayscale the image
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray_image)
cv.waitKey(0)
cv.destroyAllWindows()
# Histogram equalization
gray_image = preprocessing.equalize_hist(gray_image)

cv.imshow("equalized", gray_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Binarize
binary_img = preprocessing.binarize(gray_image)    

# Morphological operations
empty = binary_img #preprocessing.remove_content(binary_img, 5, 15)

cv.imshow("EMpty image", empty)
cv.waitKey(0)
cv.destroyAllWindows()

# Contours
contour_img = gray_image.copy()
page_contour = contours.get_page_contour(empty)

# Corners

# Find corners and find homography matrix

corners = contours.find_corners(page_contour)

output_img = img.copy()  # make a copy of the original image

# Perform homography warp

rect = contours.reorder_points(corners)
dst, max_w, max_h = contours.find_destination_points(rect)


# Perform perspective transform on original image
warped = transform.warp_perspective(img, rect, dst, max_w, max_h)

# OCR
ocr.perform_ocr(warped, "./example.pdf")


cv.imwrite("result.jpg", warped)

cv.imshow("Corrected image", warped)
cv.waitKey(0)
cv.destroyAllWindows()