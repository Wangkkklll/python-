import random


# 分数
score = 0
# 游戏提示
print("WASD为移动方式;'+'代表你的当前位置,'*'代表目标位置;tui退出游戏！")
print("游戏开始！！！")
userX = 0
userY = 0
targetX = random.randint(0, 9)
targetY = random.randint(0, 9)
while True:
    for one in range(0, 10):
        ts = ""
        s=""

        for two in range(0, 10):
            if userX == targetX and userY == targetY:
                targetX = random.randint(0, 9)
                targetY = random.randint(0, 9)
                score += 1
                print("当前分数:%d" % (score))
            if userX == one and userY == two:
                ts = "+"
            elif targetX == one and targetY == two:
                ts = "*"
            else:
                ts = "-"
            s+=ts  #除了目标和自身，其他地方均为-
        print(s)
    move = input("请移动或退出：").upper()
    if move == "TUI":
        break
    elif move == "S" and userX < 9:
        userX += 1
    elif move == "W" and userX > 0:
        userX -= 1
    elif move == "D" and userY < 9:
        userY += 1
    elif move == "A" and userY > 0:
        userY -= 1
print("游戏结束，最终得分：{}".format(score))



