# 将格子转换为线条数量
m = 7
n = 1

# 存储格子线条用的二维数组
matrix = [[-1 for i in range(n)] for i in range(m)]

# 判断是否越界
def out_of_range(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return True
    return False

# 记录当前格子的需要的最小步数
def set_step(x, y, step):
    if out_of_range(x, y):
        return
    if step == 0:
        return
    if matrix[x][y] < 0:
        matrix[x][y] = step
    else:
        matrix[x][y] = min(matrix[x][y], step)

hasResult = False
# 运行
# x - m
# y - n
def run(x, y, step):
    global hasResult
    if out_of_range(x, y):
        return
    # 递归结束条件: 当前要走的格子之前已经走过并且所用步数比当前要少
    if 0 < matrix[x][y] < step:
        return
    # 递归结束条件：已经有马跑到了终点
    if hasResult:
        return
    set_step(x, y, step)
    # 当有马跑到终点时，记录状态
    if x == m-1 and n == n-1:
        hasResult = True
        return

    # 闯四海八荒
    run(x + 2, y + 1, step + 1)
    run(x - 2, y - 1, step + 1)

    run(x + 2, y - 1, step + 1)
    run(x - 2, y + 1, step + 1)

    run(x + 1, y + 2, step + 1)
    run(x - 1, y - 2, step + 1)

    run(x + 1, y - 2, step + 1)
    run(x - 1, y + 2, step + 1)


# 从原点进发
run(0, 0, 0)

# 输出最终的结果
print (matrix[m-1][n-1])