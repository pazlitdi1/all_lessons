variable = "I'm local variable out of scope"
def my_function():
    variable = "I'm local variable inside function"
    print(variable)


my_function()
print(variable)


COMFORTABLE_TEMPERATURE = 25

def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTABLE_TEMPERATURE - temperature
print(get_diff_from_comfortable_temperature(temperature=20))


globar_var = "I'm a global varible"

def mans_function():
    global global_var
    global_var = "I defined inside inside the scope of mans_function"

print(globar_var)
mans_function()
print(globar_var)

DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_leveled_up(current_experience=150, gained_experience=60))  # True
print(is_leveled_up(current_experience=10, gained_experience=60))  # False
