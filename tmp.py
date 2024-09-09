import cv2
import dlib
import numpy as np
import os

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()

for i in range(1000):
    img_path = os.path.join("genki4k/files/", f"file{i+1:04d}.jpg")
    img = cv2.imread(img_path)
    print(i)
    cv2.imwrite(f"crop_img/file{i+1:04d}.jpg", img)
        # continue
    dets = detector(img, 1)
    if len(dets) != 0:
        d = dets[0]
        shape = predictor(img, d)
        lip = shape.parts()[1:68]
        x = [p.x for p in lip]
        y = [p.y for p in lip]
        min_x, max_x = min(x)-30, max(x)+30
        min_y, max_y = min(y)-50, max(y)+60
        
        if min_x < 0: min_x = 0
        if min_y < 0: min_y = 0
        if max_x > img.shape[1]: max_x = img.shape[1]
        if max_y > img.shape[0]: max_y = img.shape[0]

        lip_img = img[min_y:max_y, min_x:max_x]
        cv2.imwrite(f"./crop_pad_img/file{i+1:04d}.jpg", lip_img)
    else:
        cv2.imwrite(f"./crop_pad_img/file{i+1:04d}.jpg", img)



