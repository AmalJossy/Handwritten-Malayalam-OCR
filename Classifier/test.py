from keras.models import load_model
model = load_model('/home/hashrin/project/saved model/mymodel.h5')
labels=['അ','ഖ','മ്മ','മ്ല','യ്യ','ല്ല','വ്വ','ശ്ശ','ശ്ല','ശ്ച','ഷ്ട','സ്ല','ഗ','സ്സ','സ്റ്റ','സ്ധ','സ്ഥ','ഹ്മ','ഹ്ന','ഹ്ല','ള്ള','റ്റ','ൻ','ഘ','ൽ','ർ','ൾ','ൺ','ന്ധ','ങ','ച','ഛ','ജ','ഝ','ഞ','ട','ആ','ഠ','ഡ','ഢ','ണ','ത','ഥ','ദ','ധ','ന','പ','ഇ','ഫ','ബ','ഭ','മ','യ','ര','ല','വ','ശ','ഷ','ഉ','സ','ഹ','ള','ഴ','റ','ാ','ി','ീ','ു','ൂ','ഋ','ൃ','െ','േ','ൗ','്','്യ','്ര','്വ','ക്ക','ക്ല','എ','ക്ഷ','ക്ത','ഗ്ഗ','ഗ്ല','ഗ്ന','ഗ്മ','ങ്ക','ങ്ങ','ച്ച','ച്ഛ','ഏ','ജ്ജ','ജ്ഞ','ഞ്ച','ഞ്ഞ','ട്ട','ഡ്ഡ','ണ്ട','ണ്ഡ','ണ്മ','ണ്ണ','ഒ','ത്ത','ത്ഥ','ത്ഭ','ത്സ','ത്മ','ദ്ദ','ദ്ധ','ന്റ','ന്ത','ന്ദ','ക','ന്ന','ന്മ','ന്ഥ','പ്പ','പ്ല','ബ്ബ','ബ്ല','ബ്ധ','ബ്ദ','മ്പ']                   
import numpy as np
import pandas as pd
for chunk in pd.read_csv("/home/hashrin/project/final/Classifier/output.csv",header=None,chunksize=7):
    dataset=chunk.values
    X_test=dataset
    X_test=np.subtract(255,X_test)
    X_test = X_test.reshape(X_test.shape[0], 30, 30, 1).astype('float32')
    X_test = X_test / 255
    sample_chars=X_test
    predictions=model.predict(sample_chars)
    indices=[list(prediction).index(max(prediction)) for prediction in predictions]
    predicted_labels=[labels[index] for index in indices]
    for l in predicted_labels:
        print(l)
    break

# X_test=dataset
# X_test=np.subtract(255,X_test)
# X_test = X_test.reshape(X_test.shape[0], 30, 30, 1).astype('float32')
# X_test = X_test / 255
# sample_chars=X_test

# predictions=model.predict(sample_chars)
# indices=[list(prediction).index(max(prediction)) for prediction in predictions]
# predicted_labels=[labels[index] for index in indices]

# columns = 20
# rows = 20
# w=30
# h=30
# # fig=plt.figure(figsize=(8, 8))
# # for i in range(1, sample_chars.shape[0] +1):
# #     img=sample_chars[i-1].reshape((30,30))
# #     fig.add_subplot(rows, columns, i)
# #     #plt.title(predicted_labels[i-1])
# #     plt.imshow(img,cmap='gray')
# # plt.show()
# for l in predicted_labels:
#     print(l," ")