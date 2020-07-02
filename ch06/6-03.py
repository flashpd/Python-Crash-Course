favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}


for name in favorite_languages.keys():
    print(favorite_languages[name])

for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)