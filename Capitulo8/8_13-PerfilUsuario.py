def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

persona = build_profile('Pablo', 'Calvente', lugar = 'España', edad = '31', nacionalidad = 'Española')
print(persona)