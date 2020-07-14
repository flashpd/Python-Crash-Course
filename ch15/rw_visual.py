import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 可以赋初值 更改需要描述的点
    # rw = RandomWalk(5)
    rw = RandomWalk()   
    rw.fill_walk()

    # 设置分辨率和屏幕空间
    plt.figure(dpi = 128, figsize=(10, 6))

    # 将每个点都保存在列表里 然后当作参数 可以实现颜色的变换
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s = 15)
    
    # 突出起始点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break