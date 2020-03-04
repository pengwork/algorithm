import numpy as np
import matplotlib.pyplot as plt

x_mat = np.mat([[1, 1, 1],[1, 0, 1]]).T
y_mat = np.mat([1, 0.5, 1]).T

def wc_cal(x_mat, y_mat, alpha, maxIter):
    X = x_mat
    beta = np.mat([[0.1], [0.1]])
    beta0 = beta.copy()
    for i in range(maxIter):
        f = X*beta
        dbeta = X.T*(1/(1+np.exp(-f))-y_mat)
        beta -= alpha*dbeta
    return beta0, beta

beta0,beta = wc_cal(x_mat, y_mat, 0.00003, 20000)
print("beta0:\n",beta0,"\nbeta:\n",beta)

plotx = np.arange(0, 1, 0.0001)
b0 = beta[0, 0]
b1 = beta[1, 0]
plotf = b0 + b1*plotx
plt.plot(plotx, plotf, label = 'f-model')

x = [1,0,1]
y = [1, 0.5, 0.8]
plt.scatter (x, y, s=50, c='r', label="dataset")
plt.grid(True)
plt.xlabel='x'
plt.ylabel='y'
plt.legend()
plt.show()
