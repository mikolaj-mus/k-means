import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig, ax = plt.subplots()

cov = [[0.01, 0], [0, 0.01]]

mean = [np.random.random(), np.random.random()]
x1, y1 = np.random.multivariate_normal(mean, cov, 100).T

mean = [np.random.random(), np.random.random()]
x2, y2 = np.random.multivariate_normal(mean, cov, 100).T

mean = [np.random.random(), np.random.random()]
x3, y3 = np.random.multivariate_normal(mean, cov, 100).T

S_all = list(zip(np.concatenate([x1, x2, x3]), np.concatenate([y1, y2, y3])))

m1 = (np.random.random(), np.random.random())
m2 = (np.random.random(), np.random.random())
m3 = (np.random.random(), np.random.random())

ax.scatter(x1, y1, color='black', marker='x')
ax.scatter(x2, y2, color='black', marker='x')
ax.scatter(x3, y3, color='black', marker='x')

centroid1, = ax.plot(m1[0], m1[1], 'ro', markersize=20)
centroid2, = ax.plot(m2[0], m2[1], 'g*', markersize=20)
centroid3, = ax.plot(m3[0], m3[1], 'b<', markersize=20)

ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)

ax.text(0, 1.15, "Iteration: 0", fontsize=20, color='black', ha='center')

plt.pause(1)

# K-means iteration
S1_old = S2_old = S3_old = []
iteration = 0

while True:
    iteration += 1
    S1, S2, S3 = [], [], []

    for point in S_all:
        d1 = np.linalg.norm(np.array(point) - np.array(m1))
        d2 = np.linalg.norm(np.array(point) - np.array(m2))
        d3 = np.linalg.norm(np.array(point) - np.array(m3))

        if d1 < d2 and d1 < d3:
            S1.append(point)
        elif d2 < d3:
            S2.append(point)
        else:
            S3.append(point)

    if S1 == S1_old and S2 == S2_old and S3 == S3_old:
        plt.pause(2)
        plt.close(fig)
        break

    ax.clear()
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)

    if S1:
        x, y = zip(*S1)
        ax.scatter(x, y, color='red', marker='o')
        m1 = (np.mean(x), np.mean(y))

    if S2:
        x, y = zip(*S2)
        ax.scatter(x, y, color='green', marker='*')
        m2 = (np.mean(x), np.mean(y))

    if S3:
        x, y = zip(*S3)
        ax.scatter(x, y, color='blue', marker='<')
        m3 = (np.mean(x), np.mean(y))

    ax.plot(m1[0], m1[1], 'ro', markersize=20)
    ax.plot(m2[0], m2[1], 'g*', markersize=20)
    ax.plot(m3[0], m3[1], 'b<', markersize=20)

    ax.text(0.08, 1.15, f"Iteration: {iteration}", fontsize=20, color='black', ha='center')

    plt.pause(1)

    S1_old, S2_old, S3_old = S1[:], S2[:], S3[:]

plt.ioff()
plt.show()
