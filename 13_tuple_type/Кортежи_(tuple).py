user_roles = ("admin", "editor", "viewer")
for i in user_roles:
    print(i)


user_roles = ("admin", "editor", "viewer")
print("admin" in user_roles)
print("writer" in user_roles)


user_roles = ("admin", "editor", "viewer")
print(user_roles[1])


user_roles = ("admin", "editor", "viewer")

role_1, role_2, role_3 = user_roles

print(role_1)
print(role_2)
print(role_3)