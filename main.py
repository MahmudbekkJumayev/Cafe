from typing import Optional, Union
from datetime import date,datetime


users_list: list[dict[str,Union[str,date]]] = [
    {
        "username" : "python",
        "password" : "1234",
        "first_name" : "Botir", 
        "type" : "admin",
        "last_name" : "Tursunov",
        "birth_day" : date(2000, 1, 1),
    }
]

food_list: list[dict] = [
    {
        "name" : "Osh",
        "price" : 15000,
    },
    {
        "name" : "Manti",
        "price" : 12000,
    },
    {
        "name" : "Shashlik",
        "price" : 20000,
    },
    {
        "name" : "Somsa",
        "price" : 5000,
    },
    {
        "name" : "Lag'mon",
        "price" : 18000,
    },
] 

bought_food_history: list[dict] = [
    {
       "user" : {
        "first_name" : "Botir", 
        "last_name" : "Tursunov",
        "type" : "admin",
        "birth_day" : date(2000, 1, 1),
       },
         "food" : {
              "name" : "Osh",
              "price" : 15000,
              "date" : datetime.now()
         },

    },
    
]


def check_username(username: str) -> bool:
    for user in users_list:
        if user["username"] == username:
            return False
    return True

def get_menu(user: Optional[dict]) -> str:
    menu = '''
1. Taomlarni ko'rish
2. Taomlarni o'zgartirish
3. Taomlarni o'chirish
4.Logout
'''
    if user is None:
     menu ='''
1.Login
2.Register
'''
    else:
        if user["type"] == "admin":
            menu = '''
1. Taomlarni ko'rish
2. Taomlarni o'zgartirish
3. Taomlarni o'chirish
4. Taom qo'shish
5.Logout
'''
        else:
            menu = '''
1. Taomga buyurtma berish
2. Olingan taomlar ro'yxatini ko'rish
3.Logout
'''

    return menu

# Register user
def register_user():
    _username = input("Username: ")
    while not check_username(_username):
        _username = input("Bunday username allaqchon mavjud boshqa username kiriting: ")
    _first_name = input("First name: ")
    _last_name = input("Last name: ")
    _password = input("Password: ")
    _type = input("Type: ")
    while _type not in ["admin", "user"]:
        _type = input("Type (admin/user): ")
    _birth_day = input("Birth day (2005-08-19): ")
    _date = date.fromisoformat(_birth_day) 
    users_list.append({
        "username" : _username,
        "password" : _password,
        "first_name" : _first_name,
        "last_name" : _last_name,
        "type" : _type,
        "birth_day" : _date,
            })
    print("User muvaffaqiyatli ro'yxatdan o'tdi")

# Login user
def login_user():
    _username = input("Username: ")
    _password = input("Password: ")
    for user in users_list:
        if user["username"] == _username:
            if user["password"] == _password:
                current_user = user
                menu = get_menu(current_user)
                print(f"Successfully logged in as {current_user['first_name']}")
                while _k := input(get_menu(current_user)):
                    if current_user["type"] == "admin":
                        if _k == '1':
                            print("Taomlar ro'yxati: ")
                            for food in food_list:
                                print(f"{food['name']} - {food['price']}")
                        elif _k == '2':
                            _name = input("O'zgartiriladigan taom nomi: ")
                            _price = input("Yangi narxni kiriting: ")
                            for food in food_list:
                                if food["name"] == _name:
                                    food["price"] = _price
                                    print("Taom muvaffaqiyatli o'zgartirildi")
                                    break
                                else:
                                    print("Bunday taom topilmadi")
                        elif _k == '3':
                            _name = input("O'chiriladigan taom nomi: ")
                            for food in food_list:
                                if food["name"] == _name:
                                    del food
                                    print("Taom muvaffaqiyatli o'chirildi")
                                    break
                                else:
                                    print("Bunday taom topilmadi")
                        elif _k == '4':
                            _name = input("Yangi taom nomi: ")
                            _price = input("Narxni kiriting: ")
                            food_list.append({
                                "name" : _name,
                                "price" : _price,
                            })
                            print("Taom muvaffaqiyatli qo'shildi")
                        elif _k == '5': 
                            print(f"Xayr {current_user['first_name']}")
                            current_user = None
                            print("Successfully logged out")
                            break
                        else:
                            print("Menyuni to'gri tanlang")
                            break
                    else:
                        if _k == 1:
                            print("Taomlar ro'yxati: ")
                            for food in food_list:
                                print(f"{food['name']} - {food['price']}")
                            _name = input("Sotib olish uchun taom nomini kiriting: ")
                            for food in food_list:
                                if food["name"] == _name:
                                    print(f"Taom nomi {food['name']} va narxi {food['price']} Sotib olindi ")
                                    bought_food_history.append({
                                        "user" : current_user.copy(),
                                        "food" : food.copy(),
                                    })
                                    break
                                else:
                                    print("Bunday taom topilmadi")
                        elif _k == 2:
                            print("Olingan taomlar ro'yxati: ")
                            for food in bought_food_history:
                                if food["name"]["username"] = current_user["username"]:
                                    print(f"{food['food']['name']} - {food['food']['price']} - {food['food']['date']}")
                        elif _k == 3:
                            print(f"Xayr {current_user['first_name']}")
                            current_user = None
                            print("Successfully logged out")
                            break
            else:
                print("Password is incorrect")
                break
        else:
            print("Username is incorrect")



def start_project():
    current_user: Optional[dict] = None
    menu = get_menu(current_user)
    while k := input(menu):
        if k == '1':
           login_user()    
        elif k == '2':
            register_user()
        else:
         print("Menyuni to'gri tanlang")

if __name__ == "__main__":
    start_project()
