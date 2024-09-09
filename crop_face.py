import cv2 as cv
import dlib
import matplotlib.pyplot as plt

detector = dlib.get_frontal_face_detector()
print('111')
print("sasdf")
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
lt = []
pictures_path=['genki4k_dataloader_files/files/file{}.jpg'.format(str(i).zfill(4)) for i in range(1,4001)]
for i in range(0,50):

    img = cv.imread(pictures_path[i])
    [x,y,c] = img.shape
    rec = dlib.rectangle(0,0,x,y)
    print(img.shape)
    imgt = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    shape =  predictor(imgt, rec)
        
    for i in range(68):
        cv.circle(img, (shape.part(i).x, shape.part(i).y), 2, (0, 255, 0), -1, 1)
    plt.title('img')
    plt.imshow(img)
    plt.show()


# def dlib_frontal_crop():

#     detector = dlib.get_frontal_face_detector()
#     lt = []
#     pictures_path=['genki4k_dataloader_files/files/file{}.jpg'.format(str(i).zfill(4)) for i in range(1,4001)]
#     for i in range(0,4000):
#         img = cv.imread(pictures_path[i])
#         print(img.shape)
#         imgt = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#         faces =  detector(imgt, 0)
#         if (len(faces)==1):
#             for k, d in enumerate(faces):
#                     # 用红色矩形框出人脸   
                
#                 if(d.left()> 0 and d.right() > 0  and d.top()>0 and d.bottom()>0 and d.left()<d.right() and d.top()<d.bottom()):
#                     img = img[d.left():d.right(),d.top():d.bottom(),:]
#                     print(d.left())
#                     print(d.right())
#                     print(d.top())
#                     print(d.bottom())
                

#         print(img.shape)
#         cv.imwrite('crop_img/file{}.jpg'.format(str(i+1).zfill(4)),img)

# def dlib_shape_predictor_crop():
#     predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#     lt = []
#     pictures_path=['genki4k_dataloader_files/files/file{}.jpg'.format(str(i).zfill(4)) for i in range(1,4001)]
#     for i in range(0,1):

#         img = cv.imread(pictures_path[i])
#         print(img.shape)
#         imgt = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#         shape =  predictor(imgt, 1)
#         if(len(shape)!=0):
            
#             for i in range(68):
#                 cv.circle(img, (shape.part(i).x, shape.part(i).y), 2, (0, 255, 0), -1, 1)
#         cv.imshow('face shape',img)
#         cv.waitKey(0)

            
        #cv.imwrite('crop_img/file{}.jpg'.format(str(i+1).zfill(4)),img)


