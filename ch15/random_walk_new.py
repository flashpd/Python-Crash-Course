from random import choice

class RandomWalk():
    
    def __init__(self, num_points = 5000):
        self.num_points = num_points

        # 所有的随机漫步都始于(0, 0) x和y都是列表 所以调用的时候都是取最后一个数字
        self.x_values = [0]
        self.y_values = [0]
        self.x_step = 0
        self.y_step = 0
    
    def get_step(self):

        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        self.x_step = x_direction * x_distance
        
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        self.y_step = y_direction * y_distance

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            
            self.get_step()
            self.get_step()

            # 拒绝原地踏步
            if self.x_step == 0 and self.y_step == 0:
                continue
            
            # 计算下一点的x和y
            next_x = self.x_values[-1] + self.x_step
            next_y = self.y_values[-1] + self.y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
