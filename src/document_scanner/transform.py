import cv2 as cv

def warp_perspective(img, rect, dst, max_w, max_h):
    M = cv.getPerspectiveTransform(rect, dst)
    return cv.warpPerspective(img, M, (max_w, max_h))
