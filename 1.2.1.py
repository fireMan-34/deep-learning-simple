from tensorflow.keras.datasets import mnist
import numpy

# 加載數據
(x_train, y_train),(x_test, y_test) = mnist.load_data()

 
print("x_train type", type(x_train))
print("y_train type", type(y_train))
print("x_test type", type(x_test))
print("y_test type", type(y_test))

x_train:numpy.ndarray = x_train
y_train:numpy.ndarray = y_train
x_test:numpy.ndarray = x_test
y_test:numpy.ndarray = y_test

# 顯示數據形狀

print("x_train", x_train.shape)
print("y_train", y_train.shape)
print("x_test", x_test.shape)
print("y_test",y_test.shape)


# 顯示數據集
import matplotlib.pyplot as plt
import os

# 創建畫布
fig, ax = plt.subplots(
  nrows=2,
  ncols=5,
  sharex=True,
  sharey=True,
)

# 平鋪畫布
ax = ax.flatten()

for ii in range(10):
    # 獲取數據集中0-9數字 https://www.w3schools.com/python/numpy/numpy_array_reshape.asp
    img = x_train[y_train == ii][0].reshape(28, 28)
    # 绘制数字
    ax[ii].imshow(img, cmap='Greys', interpolation='nearest')

# 隐藏横纵坐标
ax[0].set_xticks([])
ax[0].set_yticks([])
# 画布紧凑输出
plt.tight_layout()

# 保存图片
figure_path = './figures'
if os.path.exists(figure_path) is False:
    os.makedirs(figure_path)
plt.savefig(os.path.join(figure_path, 'mnist.png'))

# 显示图片
plt.show()