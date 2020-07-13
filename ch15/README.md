# 第十五章知识点小结

- 模块`matplotlib`用于制作各种图表，Windows10上安装该模块在命令提示符中输入指令

  ```
  python -m pip install matplotlib
  ```

  然后进入python环境，导入该模块，不报错则说明安装成功

- `import matplotlib.pyplot as plt`导入pyplot模块并指定别名为plt，这个模块包含很多用于生成图表的函数

- 函数`plot()`用于生成折线图，第一个参数可以是列表代表着点，第二个参数linewidth决定了线条的粗细（可缺省）

- 函数`show()`用于显示图，函数`savefig()`用于保存照片，第一个参数指定保存的文件名

- 函数`title()`设置标题，第二个参数fontsize设置大小（可缺省）

- 函数`xlabel()`和`ylabel()`用于设置坐标轴的字样和大小

- 函数`tick_params()`设置刻度的样式，多个参数，参数可以设置为`anis='both'`影响x轴和y轴（both可以替换为x或者y），参数labelsize用于设置字号大小

- 函数`scatter()`用于绘制散点图，参数cmap是一系列颜色，从起始颜色渐变到结束颜色

- 函数`axis()`传入一个列表，里面要求四个值，x和y的最小最大值

