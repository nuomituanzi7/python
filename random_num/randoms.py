import random

num = random.randint(0, 100)
print(num)
count = 0
var = 1
# while var == 1:  # 表达式永远为 true
#     str = int(input("输入一个数字  :"))
#     if str>num:
#         print("大了")
#     elif str<num:
#         print("小了")
#     else:
#         print("恭喜猜中，本轮幸运数字：",str)
#         break

for str in range(5):
    count= count+1
    str = int(input("输入一个数字  :"))
    if str > num:
        print("大了")
    elif str < num:
        print("小了")
    else:
        print("恭喜猜中，本轮幸运数字：", str,"一共输入",count,"次成功")
        break
else:print("机会用完")
