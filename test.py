import numpy as np
X = np.array([[111, 1], [222, 2], [333, 3]])
for j in range(X.shape[1]):
        x = X[:,j]
        print(j, x)
# print(X.shape)