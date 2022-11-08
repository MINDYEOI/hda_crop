import cv2
import os
import time
# # input
# camNo = 17
# label = 'person023'
# bb = [331, 142, 188, 337] # x, y, w, h
# print(label[-3:])
# frameNo = 2615
# #---


def crop(camNo, frameNo, bb):

    sx = bb[0]              # start x
    dx = bb[0] + bb[2]      # destination x

    sy = bb[1]              # start y
    dy = bb[1] + bb[3]      # destination y

    # filedir = './seq2img/camera' + str(camNo) + '/I0' + str(frameNo)+'.jpg'
    filedir = './seq2img/camera%d/I%s.jpg' % (camNo, frameNo)

    source = cv2.imread(filedir, 1)

    # print(source.shape)

    target = source[sy: dy, sx: dx]

    # cv2.imshow("Original", source)
    # cv2.imshow("Crop", target)
    # cv2.waitKey(0)
    # cv2.destroyAllWindow()

    return target


def save(target, label, camNo, frameNo):
    dir = './output/%d/%s/' % (camNo, label)

    if not(os.path.isdir(dir)):
        os.makedirs(os.path.join(dir))
    
    fileName = "0%s_c%ds1_%05d_00.jpg" % (label[-3:], camNo, frameNo)

    destination = dir + fileName
    # print(destination)
    cv2.imwrite(destination, target)


def saveAll(target, label, camNo, frameNo):
    dir = './output/all/'

    if not(os.path.isdir(dir)):
        os.makedirs(os.path.join(dir))
    
    fileName = "0%s_c%ds1_%05d_00.jpg" % (label[-3:], camNo, frameNo)
    destination = dir + fileName
    # print(destination)
    cv2.imwrite(destination, target)
    now = time.localtime()
    print("%s %04d/%02d/%02d %02d:%02d:%02d" % (fileName, now.tm_year,
                                                now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

# #print(filedir)


# target = crop(17, 2615, [331, 142, 188, 337])

# save(target, 'person023', 17, 2615)

def saveClean(target, label, camNo, frameNo):
    dir = './output/clean/%d/%s/' % (camNo, label)

    if not(os.path.isdir(dir)):
        os.makedirs(os.path.join(dir))

    fileName = "0%s_c%ds1_00%d_00.jpg" % (label[-3:], camNo, frameNo)
    destination = dir + fileName
    # print(destination)
    cv2.imwrite(destination, target)


def saveAllClean(target, label, camNo, frameNo):
    dir = './output/clean/all/'

    if not(os.path.isdir(dir)):
        os.makedirs(os.path.join(dir))

    fileName = "0%s_c%ds1_00%d_00.jpg" % (label[-3:], camNo, frameNo)
    destination = dir + fileName
    # print(destination)
    cv2.imwrite(destination, target)
    now = time.localtime()
    print("%s %04d/%02d/%02d %02d:%02d:%02d" % (fileName, now.tm_year,
                                                now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
