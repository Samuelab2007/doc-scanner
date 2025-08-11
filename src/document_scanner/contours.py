import cv2 as cv
import numpy as np
from exceptions import ContourNotFoundError

def get_page_contour(img):
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    page_contour = max(contours, key=cv.contourArea)
    return page_contour

"""
TODO: Change strategy, create fallback for the cases when 4 corners cannot be found
Either there are too many corners or not enough.

Possible approaches: 

Relax the epsilon factor
    If the contour approximation is too tight, you might get 5–6 points; too loose, maybe 3 points.

    Try decreasing/increasing epsilon_factor and retry.

Pick the largest 4-sided contour in the image
    Filter contours by cv.isContourConvex and len(approx) == 4.

    If none found, use the bounding rectangle of the largest contour.

Force a rectangle from convex hull
    Take the convex hull → minimum area rectangle with cv.minAreaRect() → get 4 points.

"""
def find_corners(contour):
    for factor in [0.02, 0.015, 0.01, 0.005]:
        epsilon = factor * cv.arcLength(contour, True)  # precision: smaller = more points
        corners = cv.approxPolyDP(contour, epsilon, True)  # approximate polygon
        if len(corners) == 4:
            # If it has 4 sides, then return the corner coordinates. We flatten it before
            return corners.reshape(4, 2).astype("float32")
    raise ContourNotFoundError("Couldnt find a contour with exactly 4 corners")

def reorder_points(pts):
    s = pts.sum(axis=1); diff = np.diff(pts, axis=1)
    tl = pts[np.argmin(s)]; br = pts[np.argmax(s)]
    tr = pts[np.argmin(diff)]; bl = pts[np.argmax(diff)]
    return np.array([tl, tr, br, bl], dtype="float32")

def find_destination_points(rect):
    (tl, tr, br, bl) = rect
    width_a = np.linalg.norm(br - bl)
    width_b = np.linalg.norm(tr - tl)
    max_w = int(max(width_a, width_b))
    height_a = np.linalg.norm(tr - br)
    height_b = np.linalg.norm(tl - bl)
    max_h = int(max(height_a, height_b))

    dst = np.array([[0,0],[max_w-1,0],[max_w-1,max_h-1],[0,max_h-1]], dtype="float32")
    return (dst, max_w, max_h)