from typing import Optional, Union
from datetime import date, datetime

admin_balance: float = 0 

users_list: list[dict[str, Union[str, date]]] = [
    {
        "username": "python",
        "password": "1234",
        "first_name": "Botir",
        "type": "admin",
        "last_name": "Tursunov",
        "birth_day": date(2000, 1, 1),
    }
]

food_list: list[dict] = [
    {"name": "Osh", "price": 15000},
    {"name": "Manti", "price": 12000},
    {"name": "Shashlik", "price": 20000},
    {"name": "Somsa", "price": 5000},
    {"name": "Lag'mon", "price": 18000},
]

bought_food_history: list[dict] = []

def get_menu(user: Optional[dict]) -> str:
    if user is None:
        return """
1. Login
2. Register
"""
    elif user["type"] == "admin":
        return """
1. Taomlarni ko'rish
2. Taomlarni o'zgartirish
3. Taomlarni o'chirish
4. Taom qo'shish
5. Balansni ko'rish
6. Logout
"""
    elif user["type"] == "moderator":
        return """
1. Taomlarni ko'rish
2. Taomlarni o'zgartirish
3. Logout
"""
    else:
        return """
1. Taomga buyurtma berish
2. Olingan taomlar ro'yxatini ko'rish
3. Logout
"""

def login_user():
    global admin_balance
    _username = input("Username: ")
    _password = input("Password: ")
    for user in users_list:
        if user["username"] == _username and user["password"] == _password:
            current_user = user
            print(f"Successfully logged in as {current_user['first_name']}")
            while (choice := input(get_menu(current_user))) != '6':
                if current_user["type"] == "admin":
                    if choice == '1':
                        print("Taomlar ro'yxati:")
                        for food in food_list:
                            print(f"{food['name']} - {food['price']}")
                    elif choice == '2':
                        _name = input("O'zgartiriladigan taom nomi: ")
                        _price = input("Yangi narxni kiriting: ")
                        for food in food_list:
                            if food["name"] == _name:
                                food["price"] = int(_price)
                                print("Taom muvaffaqiyatli o'zgartirildi")
                                break
                    elif choice == '3':
                        _name = input("O'chiriladigan taom nomi: ")
                        food_list[:] = [food for food in food_list if food["name"] != _name]
                        print("Taom muvaffaqiyatli o'chirildi")
                    elif choice == '4':
                        _name = input("Yangi taom nomi: ")
                        _price = int(input("Narxni kiriting: "))
                        food_list.append({"name": _name, "price": _price})
                        print("Taom muvaffaqiyatli qo'shildi")
                    elif choice == '5':
                        print(f"Admin balansi: {admin_balance} so'm")
                elif current_user["type"] == "moderator":
                    if choice == '1':
                        print("Taomlar ro'yxati:")
                        for food in food_list:
                            print(f"{food['name']} - {food['price']}")
                    elif choice == '2':
                        _name = input("O'zgartiriladigan taom nomi: ")
                        _price = input("Yangi narxni kiriting: ")
                        for food in food_list:
                            if food["name"] == _name:
                                food["price"] = int(_price)
                                print("Taom muvaffaqiyatli o'zgartirildi")
                                break
                else:
                    if choice == '1':
                        print("Taomlar ro'yxati:")
                        for food in food_list:
                            print(f"{food['name']} - {food['price']}")
                        _name = input("Sotib olish uchun taom nomini kiriting: ")
                        for food in food_list:
                            if food["name"] == _name:
                                now = datetime.now()
                                print(f"{food['name']} {food['price']} so'mga sotib olindi ({now})")
                                bought_food_history.append({
                                    "user": current_user.copy(),
                                    "food": food.copy(),
                                    "date": now
                                })
                                admin_balance += food['price'] * 0.1  
                                break
                    elif choice == '2':
                        print("Olingan taomlar ro'yxati:")
                        for record in bought_food_history:
                            if record["user"]["username"] == current_user["username"]:
                                print(f"{record['food']['name']} - {record['food']['price']} - {record['date']}")
            print(f"Xayr {current_user['first_name']}")
            break

def start_project():
    while (k := input(get_menu(None))) != '0':
        if k == '1':
            login_user()
        elif k == '2':
            print("Ro'yxatdan o'tish hali qo'shilmagan")
        else:
            print("Menyuni to'g'ri tanlang")

if __name__ == "__main__":
    start_project()
