import matplotlib.pyplot as plt
import numpy as np

points = np.array([[1,1], [1,2],[1,3],[1,4],[1,5],[2,1], [2,2],[2,3],[2,4],[2,5]])

print(points)
print(points.shape)
plt.plot(points[:,0],points[:,0], "ro")  # r : res , o:circle
plt.show()

n = np.array([2.5,2])
plt.plot(n[0], n[1] ,"bo")  # b : blue , o:circle
plt.show()