# import tensorflow as tf
# if tf.test.gpu_device_name():
#     print('gpu : {}'.format(tf.test.gpu_device_name()))
# else:
#     print("install gpu")

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())