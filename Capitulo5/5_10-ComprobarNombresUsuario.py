current_users = ["KalRam", "kjilo", "liot", "redtro", "cast24"]
new_users = ["kalram", "tucato", "liot", "redRibon"]
current_users2 = []

for current in current_users:
    current_users2.append(current.upper())

for user in new_users:
    if user.upper() in current_users2:
        print("El usuario "+ user+" no esta disponible")
    else:
        print("El usuario "+user+" esta disponible")