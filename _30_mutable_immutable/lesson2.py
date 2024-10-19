# def append_in_list(*, element: int, lst: list = []) ->list:
#     lst.append(element)
#     return lst
#
#
# my_list = append_in_list(element=1)
# print(my_list)
# another_list = append_in_list(element=2)
# print(another_list)


# def append_in_list(*, element: int, lst: list = None) -> list:
#    if lst is None:
#       lst = []
#    lst.append(element)
#    return lst
#
#
# mylist = append_in_list(element=1)
# print(mylist)
# another_list = append_in_list(element=2)
# print(another_list)


my_list = [3, 1, 2]
another_list = sorted(my_list)
print(my_list)
print(another_list)