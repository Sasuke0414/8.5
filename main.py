# user = {
#     'name': "abdulloh",
#     'pass': "0414",
#     'is_admin': True
# }

# print(f'{user["name"]} -> {user["pass"]} -> {user["is_admin"]}')


# dbuser = {
#     "id": "abdulloh",
#     "pass": "1234"
# }

# id = input("ID kiriting: ")
# password = input("Password kiriting: ")

# user = {
#     'id': id,
#     'pass': password
# } 


# if user["id"] == dbuser["id"] and user["pass"] == dbuser["pass"]:
#     print("Tizimga Kirdingiz !")
# else:
#     print("Nmadr Xato")
# --------------------------------------------------------------------------------------
films = {
    "Forrest Gumb": 8.8,
    "Yulduzli urushlar": 8.7,
    "Uzuklar Hukmdori": 8.3
}

for film in films:
    if films[film] > 8.5:
        print(f"{film} -> Yuqori Reytingli")
    if films[film] < 8.5:
        print(f"{film} -> Pas Reytingli")