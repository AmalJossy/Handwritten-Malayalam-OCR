import os
import sys
import cv2
import csv
import numpy as np
import pandas as pd
from keras.models import load_model
import matplotlib.pyplot as plt

def getLabels():
    print("Classifying")
    #model = load_model('/home/hashrin/project/saved model/combined.h5')
    #labels=['അ','ഖ','മ്മ','മ്ല','യ്യ','ല്ല','വ്വ','ശ്ശ','ശ്ല','ശ്ച','ഷ്ട','സ്ല','ഗ','സ്സ','സ്റ്റ','സ്ധ','സ്ഥ','ഹ്മ','ഹ്ന','ഹ്ല','ള്ള','റ്റ','ൻ','ഘ','ൽ','ർ','ൾ','ൺ','ന്ധ','ങ','ച','ഛ','ജ','ഝ','ഞ','ട','ആ','ം','ഡ','ഢ','ണ','ത','ഥ','ദ','ധ','ന','പ','ഇ','ഫ','ബ','ഭ','മ','യ','ര','ല','വ','ശ','ഷ','ഉ','സ','ഹ','ള','ഴ','റ','ാ','ി','ീ','ു','ൂ','ഋ','ൃ','െ','േ','ൗ','്','്യ','്ര','്വ','ക്ക','ക്ല','എ','ക്ഷ','ക്ത','ഗ്ഗ','ഗ്ല','ഗ്ന','ഗ്മ','ങ്ക','ങ്ങ','ച്ച','ച്ഛ','ഏ','ജ്ജ','ജ്ഞ','ഞ്ച','ഞ്ഞ','ട്ട','ഡ്ഡ','ണ്ട','ണ്ഡ','ണ്മ','ണ്ണ','ഒ','ത്ത','ത്ഥ','ത്ഭ','ത്സ','ത്മ','ദ്ദ','ദ്ധ','ന്റ','ന്ത','ന്ദ','ക','ന്ന','ന്മ','ന്ഥ','പ്പ','പ്ല','ബ്ബ','ബ്ല','ബ്ധ ','ബ്ദ','മ്പ']
    
    model=load_model('/home/hashrin/project/saved model/finalmodel.h5')
    labels=['അ','ഖ','മ്മ','മ്ല','യ്യ','ല്ല','വ്വ','ശ്ശ','ശ്ല','ശ്ച','ഷ്ട','സ്ല','ഗ','സ്സ','സ്റ്റ','സ്ധ','സ്ഥ','ഹ്മ','ഹ്ന','ഹ്ല','ള്ള','റ്റ','ൻ','ഘ','ൽ','ർ','ൾ','ൺ','ന്ധ','ങ','ച','ഛ','ജ','ഝ','ഞ','ട','ആ','ം','ഡ','ഢ','ണ','ത','ഥ','ദ','ധ','ന','പ','ഇ','ഫ','ബ','ഭ','മ','യ','ര','ല','വ','ശ','ഷ','ഉ','സ','ഹ','ള','ഴ','റ','ാ','ി','ീ','ു','ൂ','ഋ','ൃ','െ','േ','ൗ','്','്യ','്ര','്വ','ക്ക','ക്ല','എ','ക്ഷ','ക്ത','ഗ്ഗ','ഗ്ല','ഗ്ന','ഗ്മ','ങ്ക','ങ്ങ','ച്ച','ച്ഛ','ഏ','ജ്ജ','ജ്ഞ','ഞ്ച','ഞ്ഞ','ട്ട','ഡ്ഡ','ണ്ട','ണ്ഡ','ണ്മ','ണ്ണ','ഒ','ത്ത','ത്ഥ','ത്ഭ','ത്സ','ത്മ','ദ്ദ','ദ്ധ','ന്റ','ന്ത','ന്ദ','ക','ന്ന','ന്മ','ന്ഥ','പ്പ','പ്ല','ബ്ബ','ബ്ല','ബ്ദ','മ്പ']
    
    char_count_list=[]
    Sreq = 30
    path='/home/hashrin/project/final/working/word/'
    dir=sorted(os.listdir(path),key=lambda x: int(os.path.splitext(x)[0]))
    no_of_items=0
    for item in dir:
        d=sorted(os.listdir(path+item),key=lambda x: int(os.path.splitext(x)[0]))
        i=0
        for image_file in d:
            no_of_items+=1
            image_path=path+item+'/'+image_file
            image = cv2.imread(image_path, 0)
            resized = cv2.resize(image, None, fx=Sreq/image.shape[0], fy=Sreq/image.shape[1],interpolation=cv2.INTER_CUBIC)
            flattened = resized.flatten()
            #data_row = np.append(flattened, label)
            with open('output.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(flattened)
            i+=1
        char_count_list.append(i)
    # j=0
    # for item in char_count_list:
    #     print(item)
    #     j+=1
    #     if j==3:
    #         break

    i=0
    j=0
    wrd_list=[]
    #print(char_count_list)
    n=0
    while j>=0:
        dataset=pd.read_csv("/home/hashrin/project/final/output.csv",header=None,skiprows=i,nrows=char_count_list[j])
        dataset=dataset.values
        X_test=dataset
        X_test=np.subtract(255,X_test)
        X_test = X_test.reshape(X_test.shape[0], 30, 30, 1).astype('float32')
        X_test = X_test / 255
        X_test=X_test
        predictions=model.predict(X_test)
        indices=[list(prediction).index(max(prediction)) for prediction in predictions if max(prediction)>0.65]
        #indices=[list(prediction).index(max(prediction)) for prediction in predictions]
        predicted_labels=[labels[index] for index in indices]
        k=[]
        for l in predicted_labels:
            k.append(l)
        wrd_list.append(k)
        i=i+char_count_list[j]
        j+=1
        if j==len(char_count_list):
            break
    print("classified")
    return wrd_list
#getLabels()



# columns = 20
# rows = 20
# w=30
# h=30
# fig=plt.figure(figsize=(8, 8))
# for i in range(1, 41):
#     img=X_test[i-1].reshape((30,30))
#     fig.add_subplot(rows, columns, i)
#     #plt.title(predicted_labels[i-1])
#     plt.imshow(img,cmap='gray')
# plt.show()
# for l in predicted_labels:
#     print(l)

#     os.remove('output.csv')
    
    



    