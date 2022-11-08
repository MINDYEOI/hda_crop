import annotation
import detection
import jebal
import time


camNo = 18

annoList = annotation.getAnnoList(camNo)
detList = detection.getDetectList(camNo)

detSet = set(list(map(tuple, detList)))
detList_ = list(map(list, detSet))

if (detList == detList_):
    print('fail')


for subAnnoList in annoList:
    label = subAnnoList[0]

    for subDetList in detList:
        for idx in range(1, len(subAnnoList)):
            now = time.localtime()
            if subDetList[2:] == subAnnoList[idx]:
                seqName = "%05d" % subDetList[1]
                cropImg = jebal.crop(subDetList[0], seqName, subDetList[2:])
                jebal.save(cropImg, label, subDetList[0], subDetList[1])
                jebal.saveAll(cropImg, label, subDetList[0], subDetList[1])
