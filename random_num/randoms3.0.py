import random

num = random.randint(0, 100)
print(num)
count = 0
var = 5000
while var > 0:
    count=count+1
    str = int(input("输入一个数字  :"))
    if str > num:
        var = var - 500
        print("大了,剩余金币数:", var)
    elif str < num:
        var = var - 500
        print("小了,剩余金币数:", var)
    else:
        var = var + 3000
        print("恭喜猜中!!!，本轮幸运数字:", str,"剩余金币数:", var)
        print("是否继续下一轮游戏?")
        a = int(input("1为继续游戏0为结束游戏:"))
        if a == 1:
            num = random.randint(0, 100)
            print(num)
        else:
            print("游戏结束,剩余金币数:", var)
            break
