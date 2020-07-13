import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, edgecolors='none', cmap=plt.cm.Blues, s=20)
plt.axis([0, 5100, 0, 5100**3])
plt.show()