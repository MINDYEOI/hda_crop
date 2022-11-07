


def getAnnoList(camNum):
    #camNum = 17

    camNum = str(camNum)
    filedir = "./hda_annotations/cam" + camNum + ".txt"


    with open(filedir, "r") as f:
        datafile = f.readlines()
    

    posIndex = 0 # datafile 안에 있는 pos 정보 index
    
    # type(datafile)
    
    anot_info = []

    # print(datafile[0])

    for line in datafile:
        posIndex += 1
        if 'lbl' in line:
            if line[4:8] == '\'per':
                label = line[5:14]
                # print(label)
                # print(datafile[posIndex])
                positions = datafile[posIndex][6:-2]
                positions = positions.split('; ')
                positions.pop()
                
                for i in range(0, len(positions)):
                    positions[i] = positions[i].split()
                    
                    for j in range(0, len(positions[i])):
                        #print(type(positions[i][j]))
                        positions[i][j] = int(float(positions[i][j]))
                        
                positions.insert(0,label)
                anot_info.append(positions)
                #print(positions)
                
    return anot_info # 테스트 해바야햄
                
                
                
def list2txt(inputList):
        
    with open('./annotation_result.txt', 'w', encoding='UTF-8') as f:
        for i in range(0, len(inputList)):
            # f.write(inputList[i]+'\n')
            # print(inputList[i])
            for j in range(0, len(inputList[i])):
                f.write(inputList[i][j]+', ')
        