current_users = ['aaA', 'bbb', 'ccc', 'ddd', 'eee']
new_users = ['qqq', 'aAa', 'www', 'BBB', 'ppp']


for new_user in new_users:
    flag = 0
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            flag = 1
            break

    if flag == 1:
        print(new_user + " has already been used.")
    else:
        print(new_user + " has not been used.")