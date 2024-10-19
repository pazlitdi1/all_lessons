import json

# book = {
#     'title': '1984',
#     'author': 'Pazlitdinov Mansur',
#     'isbn': '978-3765328921',
#     'uuid': 'a0eebc99-8c0h-7ef8-bb2d-3bb7mm234a01',
# }
#
# json_string = json.dumps(book)
#
# print(type(json_string))
# print(json_string)
# json_string = {"title": "1984", "author": "Pazlitdinov Mansur", "isbn": "978-3765328921", "uuid": "a0eebc99-8c0h-7ef8-bb2d-3bb7mm234a01"}


# json_string1 = '{"title": "1984", "author": "Pazlitdinov Mansur", "isbn": "978-3765328921", "uuid": "a0eebc99-8c0h-7ef8-bb2d-3bb7mm234a01"}'
#
# book = json.loads(json_string1)
# print(book)


book = {
    'title': '1984',
    'author': 'Pazlitdinov Mansur',
    'isbn': '978-3765328921',
    'uuid': 'a0eebc99-8c0h-7ef8-bb2d-3bb7mm234a01',
    'count': 30,
    'genres': ['dystopia']
}

json_string = json.dumps(book)
print(json_string)