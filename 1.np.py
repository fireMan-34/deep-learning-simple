# https://numpy.github.net.cn/doc/stable/user/absolute_beginners.html
import numpy as np

'''
# 閲讀 numpy 文檔風格代碼
# 帶 >>> 輸入
>>> a = np.arange(6)
# 不帶則是輸出
(1,6)
'''

a = np.array([1, 2, 3, 4, 5, 6])

b = np.array([
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],]
)

print("a =>",a[0])
print("b =>",b[0])