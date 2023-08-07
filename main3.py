goods = {}


def add(name, value):
    goods[name] = value
    # if name in goods:
    #     print('true')
        #goods[name] = value

def ad(name, value):
    if name in goods:
        print('true')
        goods[name] = goods[name] + value
    else:
        goods[name] = value

add('ryyrt', 345)
ad('ryyrt', 55)
ad('3535', 700)
print(goods)
