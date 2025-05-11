import json

class Admin_User:
    def admin():
        with open ("db.json", "r") as file:
            db = json.load(file)
        for user in db:
            if user["id"] == "admin":
                continue
            else:
                print("\n"+"User ID: ", user["id"])
                for key, value in user.items():
                    if key == "id" or key == "Password" or key == "Total_Balance":
                        continue
                    print(key+" : "+str(value))