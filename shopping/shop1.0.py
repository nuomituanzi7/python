money=1000
goods={'卫衣': 200, '外套': 323, '帽子': 50, '牛仔裤': 123, '衬衫': 150, '老爹鞋': 93, '运动服': 350}
ShoppingCart=0
var=1

while var == 1:
    a=input("请选择商品:")

    if str>num:
        var=var-500
        print("大了,剩余金币数",var)
    elif str<num:
        var = var - 500
        print("小了,剩余金币数", var)
    else:
        var = var + 3000
        print("恭喜猜中，本轮幸运数字：",str)
        num = random.randint(0, 100)
        print(num)