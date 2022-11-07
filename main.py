import annotation
import detection
import jebal
import time


camNos = [17, 18, 19, 40, 50, 53, 54, 56, 57, 58, 59, 60]
now = time.localtime()

for camNo in camNos:
    
    annoList = annotation.getAnnoList(camNo)
    detList = detection.getDetectList(camNo)
    
    for subAnnoList in annoList:
        label = subAnnoList[0]
        
        for idx in range(1, len(subAnnoList)):
            for subDetList in detList:
                now = time.localtime()
                print("finding.. %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
                if subDetList[2:] == subAnnoList[idx]:
                    seqName = "%05d" % subDetList[1]
                    cropImg = jebal.crop(subDetList[0], seqName, subDetList[2:])
                    jebal.save(cropImg, label, subDetList[0], subDetList[1])
                    jebal.saveAll(cropImg, label, subDetList[0], subDetList[1])

                    
                    