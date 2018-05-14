import matplotlib.pyplot as plt
input_num = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_num,squares, linewidth=5)
plt.title("square numbers", fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value", fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()