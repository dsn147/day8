users={}
'''
    "account"：{
        "username":"username",
        "password":"asdfasdf"
    }
'''
bank_name = "中国工商银行昌平支行"

# 银行开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 1.看银行是否已满  满了返回3
    if len(users) > 100:
        return 3

    # 2.用户名是否存在，若存在返回2
    if account in users.keys():
        return 2
    # 3.正常开户，将用户信息存在数据库
    users[account]  = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1
# 用户操作逻辑
def addUser():
    username = input("请输入用户名:")
    password = input("请输入取款密码:")
    country= input("请输入国家:")
    province = input("请输入省份：")
    street =  input("请输入街道：")
    door = input("请输入门牌号：")
    ascll = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a",
             "s", "d", "f", "g", "h", "j", "k", "z", "x", "c", "v", "b", "n", "m"]

    # 随机产生8个数的账号
    i = 0
    name = ""
    how = len(ascll)
    import random

    while True:
        r = random.randint(0, how - 1)
        if i < 8:
            list = (ascll[r])
            name = name + list
            i = i + 1
        else:
            break
    account = name #账号
    # 架构数据传输给银行
    status = bank_addUser(account,username,password,country,province,street,door)

    if status == 1:
        print("开户成功！以下是您的个人信息：")
        info = '''
            -------------------个人信息------------------
            用户名:%s,
            密码：%s,
            账号:%s,
            地址：
                国家:%s,
                省份:%s,
                街道：%s,
                门牌号:%s
            余额：%s,
            开户行:%s
        '''
        print(info % (username,password,account,country,province,street,door,users[account]["money"],bank_name))
        print(account,type(account))
        print(password,type(password))

    elif status == 2:
        print("该用户已存在，别瞎弄！")
    elif status == 3:
        print("对不起，数据库已满！请携带证件到其他银行办理！")
#存钱
def save_money():
    account = str(input("请输入您的账号:"))
    if account in users.keys():
        money = int(input("请输入金额"))
        users[account]["money"] =  users[account]["money"] + money
        print("您当前金额为：",users[account]["money"])

    else:
        print("你的账号输入错误")
#取钱
def get_money():
    while True:
        account = str(input("请输入您的账号:"))
        if account in users.keys():
            password = input("请输入您的密码：")
            if password in users[account]["password"]:
                print("您的余额为：", users[account]["money"])
                gm = int(input("请输入取出金额："))
                while users[account]["money"] < gm:
                    gm = int(input("您输入金额超过您的余额,请重新输入："))
                if users[account]["money"]>=gm:
                    print("成功取出")
                    users[account]["money"] = users[account]["money"] - gm
                    print("余额为：", users[account]["money"])
                    break
            else:
                print("密码输入错误，请重新输入")
        else:
            print("账号输入错误，请重新输入")


#银行转账逻辑
def bank_transfer(roll_out,password,shift_to,transfer_amount):
    if roll_out and shift_to not in users.keys():
        return 1

    if password not in users[roll_out]["password"]:
        return 2

    if transfer_amount > users[roll_out]["money"]:
        return 3
    users[roll_out]["money"] = users[roll_out]["money"] - transfer_amount
    users[shift_to]["money"] = users[shift_to]["money"] + transfer_amount
    return 0
#用户转账操作
def transfer_account():
    roll_out = input("请输入转出账号：")
    password = str(input("请输入密码："))
    shift_to = input("请输入转入账号：")
    transfer_amount = input("请输入转账金额：")
    transfer_amount = int(transfer_amount)
    condition = bank_transfer(roll_out,password,shift_to,transfer_amount)

    if condition == 0:
        print("转账成功，以下是您本次的转账信息：")
        info = '''
            -------------------转账信息--------------------
            转入的用户名：%s
            转入的账号：%s
            转入的金额：%s
            '''
        print(info % (users[shift_to]["username"],shift_to,transfer_amount))

    elif condition == 1:
        print("账号输入错误")
    elif condition == 2:
        print("密码输入错误")
    elif condition == 3:
        print("没有账号余额")

#查询
def bank_query():
    while chose == '5':
        AA = input("请输入账号：")
        if AA in users.keys():
            p =input("请输入账户密码：")
            if p == users[AA]["password"]:
               print("用户名：",users[AA]["username"])
               print("密码：", users[AA]["password"])
               print("账号：", AA)
               print("地址：")
               print("   国家：", users[AA]["country"])
               print("   省份：", users[AA]["province"])
               print("   街道：", users[AA]["street"])
               print("   门牌号：", users[AA]["door"])
               print("余额：", users[AA]["money"])
               print("开户行：", users[AA]["bank_name"])
               break
            else:
                print("您的密码输入错误，请重新输入")
        else:
            print("该用户不存在，请重新输入！")

def welcome():
    print("--------------------------------------")
    print("-           中国工商银行账户管理系统    -")
    print("--------------------------------------")
    print("-    1.开户                           -")
    print("-    2.存钱                           -")
    print("-    3.取钱                           -")
    print("-    4.转账                           -")
    print("-    5.查询                           -")
    print("-    6.Bye！                          -")
    print("- -------------------------------------")

while True:
    welcome() # 打印页面
    chose = input("请输入您的业务编号:")
    if chose == '1':
        addUser()
    elif chose == '2':
        save_money()
    elif chose == '3':
        get_money()
    elif chose == '4':
        transfer_account()
        #transfer_accounts()
    elif chose == '5':
        bank_query()
    elif chose == '6':
        print("欢迎下次再来使用中国工商银行账户管理系统，再见！")
        break
    else:
        print("输入非法，请重新输入！")