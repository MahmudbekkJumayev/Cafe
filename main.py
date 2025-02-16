from typing import Optional, Union
from datetime import date, datetime

users_list: list[dict[str, Union[str, date, int]]] = [
    {
        "username": "python",
        "password": "1234",
        "first_name": "Botir",
        "last_name": "Tursunov",
        "type": "admin",
        "birth_day": date(2000, 1, 1),
        "balance": 0,
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

def check_username(username: str) -> bool:
    return all(user["username"] != username for user in users_list)

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
1. Taom narxini o'zgartirish
2. Logout
"""
    else:
        return """
1. Taomga buyurtma berish
2. Olingan taomlar ro'yxatini ko'rish
3. Logout
"""

def register_user():
    _username = input("Username: ")
    while not check_username(_username):
        _username = input("Bunday username mavjud, boshqa tanlang: ")
    _first_name = input("First name: ")
    _last_name = input("Last name: ")
    _password = input("Password: ")
    _type = input("Type (admin/user/moderator): ")
    while _type not in ["admin", "user", "moderator"]:
        _type = input("Type (admin/user/moderator): ")
    _birth_day = date.fromisoformat(input("Birth day (YYYY-MM-DD): "))
    users_list.append({
        "username": _username,
        "password": _password,
        "first_name": _first_name,
        "last_name": _last_name,
        "type": _type,
        "birth_day": _birth_day,
        "balance": 0 if _type == "admin" else None
    })
    print("User muvaffaqiyatli ro'yxatdan o'tdi")

def login_user():
    _username = input("Username: ")
    _password = input("Password: ")
    for user in users_list:
        if user["username"] == _username and user["password"] == _password:
            current_user = user
            print(f"Successfully logged in as {current_user['first_name']}")
            while True:
                choice = input(get_menu(current_user))
                if current_user["type"] == "admin":
                    if choice == '1':
                        print("Taomlar ro'yxati:")
                        for food in food_list:
                            print(f"{food['name']} - {food['price']}")
                    elif choice == '2':
                        _name = input("Narxi o'zgartiriladigan taom: ")
                        for food in food_list:
                            if food["name"] == _name:
                                food["price"] = int(input("Yangi narx: "))
                                print("Narx yangilandi")
                                break
                    elif choice == '3':
                        _name = input("O'chiriladigan taom: ")
                        food_list[:] = [food for food in food_list if food["name"] != _name]
                        print("Taom o'chirildi")
                    elif choice == '4':
                        food_list.append({"name": input("Yangi taom nomi: "), "price": int(input("Narx: "))})
                        print("Yangi taom qo'shildi")
                    elif choice == '5':
                        print(f"Admin balans: {current_user['balance']}")
                    elif choice == '6':
                        print(f"Xayr {current_user['first_name']}")
                        return
                elif current_user["type"] == "moderator":
                    if choice == '1':
                        _name = input("Narxi o'zgartiriladigan taom: ")
                        for food in food_list:
                            if food["name"] == _name:
                                food["price"] = int(input("Yangi narx: "))
                                print("Narx yangilandi")
                                break
                    elif choice == '2':
                        return
                else:
                    if choice == '1':
                        print("Taomlar ro'yxati:")
                        for food in food_list:
                            print(f"{food['name']} - {food['price']}")
                        _name = input("Sotib olish uchun taom: ")
                        for food in food_list:
                            if food["name"] == _name:
                                print(f"{food['name']} sotib olindi")
                                bought_food_history.append({
                                    "user": current_user["username"],
                                    "food": food["name"],
                                    "price": food["price"],
                                    "date": datetime.now()
                                })
                                for admin in users_list:
                                    if admin["type"] == "admin":
                                        admin["balance"] += food["price"] * 0.1
                                break
                    elif choice == '2':
                        print("Olingan taomlar:")
                        for record in bought_food_history:
                            if record["user"] == current_user["username"]:
                                print(f"{record['food']} - {record['price']} - {record['date']}")
                    elif choice == '3':
                        return

def start_project():
    while True:
        choice = input(get_menu(None))
        if choice == '1':
            login_user()
        elif choice == '2':
            register_user()

if __name__ == "__main__":
    start_project()
