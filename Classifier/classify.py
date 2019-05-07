import os
import sys
Sreq = 30
path='/home/hashrin/project/final/working/word/'
dir=sorted(os.listdir(path),key=lambda x: int(os.path.splitext(x)[0]))
for item in dir:
    d=sorted(os.listdir(path+item),key=lambda x: int(os.path.splitext(x)[0]))
    for image_file in d:
        image_path=path+item+'/'+image_file
        image = cv2.imread(image_path, 0)
        resized = cv2.resize(image, None, fx=Sreq/image.shape[0], fy=Sreq/image.shape[1],interpolation=cv2.INTER_CUBIC)
        flattened = resized.flatten()
        data_row = np.append(flattened, label)
        with open('output.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data_row)
    
    os.remove('output.csv')


def getLabels():
    # read files of working/word/<word folder>/<char images

    # classify
    # append to 2D list
    return [[1,2],[1,2,3]]