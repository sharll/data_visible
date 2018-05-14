import matplotlib.pyplot as plt
x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values,edgecolors='none', s=40)
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of number", fontsize=14)
plt.axis([0, 1100, 0, 1100000])#设置 xy轴的取值范围，注意传值的形式
plt.savefig('colormap.png', bbox_inches='tight')
plt.show()
