import tensorflow as tf
from PIL import Image
import numpy as np

from train import CNN

'''
python 3.7
tensorflow 2.0.0b0
pillow(PIL) 4.3.0
'''


class Predict(object):
    def __init__(self):
        latest = tf.train.latest_checkpoint('./ckpt')
        self.cnn = CNN()
        # 恢复网络权重
        # self.cnn.model.load_weights(latest)
        self.cnn.model.load_weights("newWeight.hdf5")

    def predict(self, image_path):
        # 以黑白方式读取图片
        img = Image.open(image_path).convert('L')
        img = img.convert('1')  # 二值化
        img = img.resize((28, 28))  # resize到28*28
        flatten_img = np.reshape(img, (28, 28, 1))
        x = np.array([1 - flatten_img])

        # API refer: https://keras.io/models/model/
        y = self.cnn.model.predict(x)

        # 因为x只传入了一张图片，取y[0]即可
        # np.argmax()取得最大值的下标，即代表的数字
        print(image_path)
        print(y[0])
        print('        -> Predict digit', np.argmax(y[0]))


if __name__ == "__main__":
    app = Predict()
    i = 0
    while i < 11:
        numer_img = str(i)
        file_name_list = './test_images/' + numer_img + '.png'
        app.predict(file_name_list)
        i += 1
