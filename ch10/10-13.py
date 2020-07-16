import json

def get_stored_username():
    #   获取之前存储的名字
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:    #   json文件为空的时候进行读取会直接报错 这里要进行处理
        username = ''
        return username
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def verify_user(username):
    name = input("Please input your name to verify: ")
    if name == username:
        flag = True
    else:
        flag = False

    return flag

def greet_user():
    #   获取用户姓名
    username = get_stored_username()
    if username:  # 用户名为空 则直接要求输入新的用户名
        flag = verify_user(username)
        if flag:
            print("Welcome back, " + username + "!")
        else:
            print("Please enter the correct name!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
