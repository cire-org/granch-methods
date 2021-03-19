import matplotlib.pyplot as plt

plt.style.use('ggplot')

X = [0.5, 1, 1.866, 2.366, 2.866, 3.732, 4.598, 5.464, 5.964, 6.464]
Y = [-0.866, 0, -0.5, -1.366, -2.232, -2.732, -3.232, -2.732, -3.598, -4.464]

plt.scatter(X,Y)
plt.plot(X, Y)
plt.show()
