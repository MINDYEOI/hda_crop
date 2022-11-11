import annotation
import detection
import jebal
import time


camNos = [17, 18, 19, 40, 50, 53, 54, 56, 57, 58, 59, 60]
now = time.localtime()

for camNo in camNos:

    annoList = annotation.getAnnoList(camNo)
    detList = detection.getCleanDetectList(camNo)

    detSet = set(list(map(tuple, detList)))
    detList_ = list(map(list, detSet))

    for subAnnoList in annoList:
        label = subAnnoList[0]

        for subDetList in detList_:
            for idx in range(1, len(subAnnoList)):
                now = time.localtime()
                if subDetList[2:] == subAnnoList[idx]:
                    seqName = "%05d" % subDetList[1]
                    cropImg = jebal.crop(
                        subDetList[0], seqName, subDetList[2:])
                    jebal.saveClean(
                        cropImg, label, subDetList[0], subDetList[1])
                    jebal.saveAllClean(
                        cropImg, label, subDetList[0], subDetList[1])

                    break
