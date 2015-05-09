# -*- coding: utf-8 -*-
import cv2

src = cv2.imread('../../image/twittan/twittan.jpg')
dst = src.copy()

roi_x = 100
roi_y = 100
roi_w = 150
roi_h = 200

dst[roi_y:roi_y+roi_w, roi_x:roi_x+roi_w] = cv2.blur(src[roi_y:roi_y+roi_w, roi_x:roi_x+roi_w], (5, 5), (-1, -1))
cv2.imwrite('twi_blur_cv.jpg', dst)



