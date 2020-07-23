## 入门级Tensorflow-mnist手写数字识别

- 我的学习历程，以下为我入门时看的博主相关博客
- 代码中写的Tensorflow版本2.0，我目前安装的是1.3版本对目前代码貌似没影响
- 另外在学习过程中尝试换了个Alexnet网络， cpu训练很慢， 建议减小训练图像数量
- 代码predict部分，我加入了二值化，不然用原作者代码跑的时候会不准，我觉得是因为训练集是黑白图像，所以predict也用二值化会好一些

## mnist

- [TensorFlow 2.0 (五) - mnist手写数字识别(CNN卷积神经网络)](https://geektutu.com/post/tensorflow2-mnist-cnn.html)
    - [Github - v4_cnn](https://github.com/geektutu/tensorflow-tutorial-samples/tree/master/mnist/v4_cnn)
    - 介绍了如何搭建CNN网络，准确率达到0.99
    - 使用TensorFlow 2.0

- [TensorFlow入门(四) - mnist手写数字识别(制作h5py训练集)](https://geektutu.com/post/tensorflow-make-npy-hdf5-data-set.html)
    - [Github - make_data_set](https://github.com/geektutu/tensorflow-tutorial-samples/tree/master/make_data_set)
    - 介绍了如何使用 numpy 制作 npy 格式的数据集
    - 介绍了如何使用 h5py 制作 HDF5 格式的数据集

- [TensorFlow入门(三) - mnist手写数字识别(可视化训练)](https://geektutu.com/post/tensorflow-mnist-tensorboard-training.html)
    - [Github - mnist/v3](https://github.com/geektutu/tensorflow-tutorial-samples/tree/master/mnist/v3)
    - 介绍了tensorboard的简单用法，包括标量图、直方图以及网络结构图

- [TensorFlow入门(二) - mnist手写数字识别(模型保存加载)](https://geektutu.com/post/tensorflow-mnist-save-ckpt.html)
    - [Github - mnist/v2](https://github.com/geektutu/tensorflow-tutorial-samples/tree/master/mnist/v2)
    - 介绍了 TensorFlow 中如何保存训练好的模型
    - 介绍了如何从某一个模型为起点继续训练
    - 介绍了模型如何加载使用，传入真实的图片如何识别

- [TensorFlow入门(一) - mnist手写数字识别(网络搭建)](https://geektutu.com/post/tensorflow-mnist-simplest.html)
    - [Github - mnist/v1](https://github.com/geektutu/tensorflow-tutorial-samples/tree/master/mnist/v1)
    - 这篇博客介绍了使用 TensorFlow 搭建最简单的神经网络。
    - 包括输入输出、独热编码与损失函数，以及正确率的验证。

