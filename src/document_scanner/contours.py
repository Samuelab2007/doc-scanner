import cv2 as cv
import numpy as np

def get_page_contour(img):
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    page_contour = max(contours, key=cv.contourArea)
    return page_contour

def find_corners(contour):
    epsilon = 0.02 * cv.arcLength(contour, True)  # precision: smaller = more points
    corners = cv.approxPolyDP(contour, epsilon, True)  # approximate polygon
    return corners

def reorder_points(pts):
    pts = np.array(pts, dtype="float32").reshape(4,2)
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