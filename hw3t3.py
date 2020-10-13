import matplotlib.pyplot as plt
import numpy as np
a = np.zeros((15, 28))
a[2:-2, 1] = 1; a[2, 2:6] = 1
a[2:7, 6] = 1; a[7:-2, 7] = 1
a[7, 2:7] = 1; a[-3, 2:7] = 1
a[2:-2, 10] = 1; a[2:-2, 14] = 1
a[2:-2, 18] = 1; a[-3, 10:19] = 1
a[2, 21:26] = 1; a[2:13, 26] = 1
a[12, 21:26] = 1; a[7, 21:26] = 1
u, s, w = np.linalg.svd(a)
rank = np.linalg.matrix_rank(a)
for i in range(15):
    print(u[i, :])
v = w.T
