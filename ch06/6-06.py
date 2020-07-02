favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

names = ['jen', 'alice', 'mark','sarah', 'edward', 'phil']

for name_1 in names:
    flag = 0
    for name_2 in favorite_languages.keys():
        if name_1 == name_2:
            flag = 1
            break
    
    if flag == 1:
        print(name_1 + ", Thank you for your participation.")
    else:
        print(name_1 + ", We sincerely invite you to participate.")