
def getDetectList(camNum):
    
    """
    Name : detection
    Function : Read the `/Detections/allD.txt` file and
    
    
    Input : camNum(int)      # camera No.

    Output: list_file(list)   # it consists of [ CameraNo, FrameNo, BoundingBoxCoordinates]
    
    
        
    """

    camNum = str(camNum)
    filedir = "./hda_detections_all/camera" + camNum + "/Detections/allD.txt"
    # #print(filedir)


    with open(filedir, 'r') as f:
        list_file = []
        for line in f:
            # #print(type(line))
            list_file.append(line.split(','))
            
            

    for i in range(0, len(list_file)):
        list_file[i].pop()
        # print(list_file[i])
        
        for j in range(0, 6):
            list_file[i][j] = int(float(list_file[i][j]))
            
        #print(list_file[i])
        
    return list_file

