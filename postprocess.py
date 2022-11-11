import random
import os
import argparse
import cv2
import shutil

def splitdata(dir, aim):

    target_dir = './dataset/'
    train_dir = target_dir + 'bounding_box_train/'
    test_dir = target_dir + 'bounding_box_test/'
    query_dir = target_dir + 'query/'

    if not(os.path.isdir(target_dir)):
        os.makedirs(os.path.join(target_dir))


    all_data = os.listdir(dir)
    random.shuffle(all_data)
    #print(all_data)

    data_num = len(all_data)


    if(aim == 1):

        if not(os.path.isdir(train_dir)):
            os.makedirs(os.path.join(train_dir))

        if not(os.path.isdir(test_dir)):
            os.makedirs(os.path.join(test_dir))

        if not(os.path.isdir(query_dir)):
            os.makedirs(os.path.join(query_dir)) 

        train_num = int(data_num * 0.5)
        test_num = int(data_num * 0.9)

        for train_img in all_data[:train_num]:
            source =cv2.imread(dir+train_img)
            cv2.imwrite(train_dir+train_img,source)
            print('Saved %s in %s' % (train_img, train_dir), end='\r')
        print("\n")
        for test_img in all_data[train_num:test_num]:
            source =cv2.imread(dir+test_img)
            cv2.imwrite(test_dir+test_img,source)
            print('Saved %s in %s' % (test_img, test_dir), end='\r')
        print("\n")
        for query_img in all_data[test_num:]:
            source=cv2.imread(dir+query_img)
            cv2.imwrite(query_dir+query_img, source)
            print('Saved %s in %s' % (query_img, query_dir), end='\r')
        print("\n")

    else:

        if not(os.path.isdir(train_dir)):
            os.makedirs(os.path.join(train_dir))

        if not(os.path.isdir(test_dir)):
            os.makedirs(os.path.join(test_dir))

        if not(os.path.isdir(query_dir)):
            os.makedirs(os.path.join(query_dir)) 
            
        test_num = int(data_num * 0.7)  
        for test_img in all_data[:test_num]:
            source =cv2.imread(dir+test_img)
            cv2.imwrite(test_dir+test_img,source)
            print('Saved %s in %s' % (test_img, test_dir), end='\r')
        print("\n")
        for query_img in all_data[test_num:]:
            source=cv2.imread(dir+query_img)
            cv2.imwrite(query_dir+query_img, source)
            print('Saved %s in %s' % (query_img, query_dir), end='\r')
        print("\n")




    

def parse_args():
  parser = argparse.ArgumentParser(description="Divide the dataset")
  parser.add_argument("--input", "-i", required=True,
    help="Path to input data")
  parser.add_argument("--aim", "-a", required=True,
    help="Purpose the data (To train : 1, To test : 2")
  
  return parser.parse_args()




if __name__ == "__main__":
    args = parse_args()
    if (args.input[-1:] != "/"):
        args.input = args.input + '/'
        print(args.input)
    splitdata(args.input, args.aim)