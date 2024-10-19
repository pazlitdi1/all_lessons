numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average = sum(numbers1) / len(numbers1)
print(average)

numbers2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
average_2 = sum(numbers2) / len(numbers2)
print(average_2)


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


average_1 = find_average(numbers1)
print(average_1)


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count


print(count_vowels("Hello lazy developer"))
print(count_vowels("Python is a very powerful language ."))


def nothing():
    print('This function is called.')
nothing()


def format_date(day: int, month: str, year: int):
    return f"The date is {day} {month} {year}"

print(format_date(day=15, month='January', year=2020))
print(format_date(day=2, month='June', year=2008))


def custom_greeting(*, name: str, greeting: str = "Hello lazy developer") -> str:
    return f"{greeting} {name}"
print(custom_greeting(name="Denislam", greeting="Welcome"))
print(custom_greeting(name="Ibrahim", greeting="Good morning"))