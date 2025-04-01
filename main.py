import matplotlib.pyplot as plt
import numpy as np


cov = [[0.01, 0], [0, 0.01]]

mean = [np.random.random(), np.random.random()]
x1, y1 = np.random.multivariate_normal(mean, cov, 100).T
plt.scatter(x1, y1, color='black', marker='x')

mean = [np.random.random(), np.random.random()]
x2, y2 = np.random.multivariate_normal(mean, cov, 100).T
plt.scatter(x2, y2,  color='black', marker='x')

mean = [np.random.random(), np.random.random()]
x3, y3 = np.random.multivariate_normal(mean, cov, 100).T
plt.scatter(x3, y3,  color='black', marker='x')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
S_all = list(zip(np.concatenate([x1, x2, x3]), np.concatenate([y1, y2, y3])))
print(S_all)

m1 = (np.random.random(), np.random.random())
m2 = (np.random.random(), np.random.random())
m3 = (np.random.random(), np.random.random())

plt.plot(m1[0], m1[1], color='red', marker='o', markersize=25)
plt.plot(m2[0], m2[1], color='green', marker='*', markersize=25)
plt.plot(m3[0], m3[1], color='blue', marker='<', markersize=25)
print(m1)
print(m2)
print(m3)
S1 = []
S2 = []
S3 = []
S1_old = []
S2_old = []
S3_old = []
plt.show()

while True:
    for point in S_all:
        m1_edist = np.sqrt(np.power(m1[0] - point[0], 2) + np.power(m1[1] - point[1], 2))
        m2_edist = np.sqrt(np.power(m2[0] - point[0], 2) + np.power(m2[1] - point[1], 2))
        m3_edist = np.sqrt(np.power(m3[0] - point[0], 2) + np.power(m3[1] - point[1], 2))
        smallest_dist = None
        if m1_edist < m2_edist:
            if m1_edist < m3_edist:
                S1.append(point)
            else:
                S3.append(point)
        elif m2_edist < m3_edist:
            S2.append(point)
        else:
            S3.append(point)

    if S1 == S1_old and S2 == S2_old and S3 == S3_old:
        break
    if S1.__len__() != 0:
        x,y = zip(*S1)
        plt.scatter(x, y, color='red', marker='o')
        m1 = (np.mean(x), np.mean(y))
    if S2.__len__() != 0:
        x,y = zip(*S2)
        plt.scatter(x, y, color='green', marker='*')
        m2 = (np.mean(x), np.mean(y))
    if S3.__len__() != 0:
        x,y = zip(*S3)
        plt.scatter(x, y, color='blue', marker='<')
        m3 = (np.mean(x), np.mean(y))
    plt.plot(m1[0], m1[1], color='red', marker='o', markersize=25)
    plt.plot(m2[0], m2[1], color='green', marker='*', markersize=25)
    plt.plot(m3[0], m3[1], color='blue', marker='<', markersize=25)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.show()

    S1_old = S1.copy()
    S2_old = S2.copy()
    S3_old = S3.copy()
    S1.clear()
    S2.clear()
    S3.clear()
