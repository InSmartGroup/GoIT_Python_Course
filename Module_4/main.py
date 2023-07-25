import sys
import os

# # lists
# print(dir(list))
"""
List methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
"""
# my_list = [1, 2, 'hello', 5, 'day']
# print(my_list)
#
# for i in my_list:
#     print(i)
#
# print(my_list[0], my_list[2], my_list[4])
# my_list[0] = 'HEY'
# print(my_list)
#
# print(my_list[1:3])
# print(my_list[::-1])
#
# numbers = [i for i in range(10)]
# print(numbers[0::2])
# print(numbers[1::2])
# print(numbers.clear())
#
# my_list = []
# print(my_list)
# my_list.append('yes')
# print(my_list)
# my_list.extend(['no', 'maybe', 'sure', 'of course', 'definitely'])
# print(my_list)
# sure = my_list.pop(3)
# print(f"My list: {my_list}", f"Popped item: {sure}")
# my_list.insert(0, 'NO NO NO')
# my_list.insert(len(my_list), 'YES YES YES')
# print(my_list)
# index = my_list.index("YES YES YES")
# print(f"Item 'YES YES YES' has index {index}")
#
# my_list = [1, 1, 1, 2, 2, 3]
# print(f"My list has {my_list.count(1)} items '1'")
#
# my_list = [5, 6, 3, 1, 2, 8, 6, 4, 3]
# print(sorted(my_list))
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list = ['a', 'b', 't', 'g', 'e', 'v']
# print(sorted(my_list))
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
#
# my_list = ['a', 'b', 'c', 'd', 'e']
# print(my_list)
# my_list.remove('a'), my_list.remove('d')
# print(my_list)
#
#
#
# dictionaries
# print(dir(dict))
"""
Dictionary methods: clear, copy, fromkeys, get, items, keys, values, pop, popitem, setdefault, update
"""
# my_dict = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 'some string', 'key5': ['some', 'list', 'here']}
# print(my_dict)
# print(my_dict['key2'])
# print(my_dict['key4'])
# print(my_dict['key5'])
# print(my_dict['key5'][1])
# print(my_dict['key5'][0:2])
# print(my_dict.get('key6'))
#
# popped_value_1 = my_dict.pop('key1')
# print(popped_value_1)
# popped_value_2 = my_dict.pop('key4')
# print(popped_value_2)
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#
# my_dict.update({'key6': 666})
# print(my_dict)
#
# for key in my_dict:
#     print(key)
#
# for value in my_dict.values():
#     print(value)
#
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")
#
# my_dict['new_stuff'] = 'new'
# print(my_dict)
#
# for i in range(1, 4):
#     my_dict[i] = f'new_{i}'
# print(my_dict)
#
#
#
# sets
# print(dir(set))
"""
Set methods: add, clear, copy, difference, difference_update, discard, intersection, intersection_update,
isdisjoint, issubset, issuperset, pop, remove, symmetric_difference, symmetric_difference_update,
union, update
"""
# my_set = set('hello')
# print(my_set)
# my_set = {'h', 'e', 'l', 'l', 'o'}
# print(my_set)
# my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(my_set)
#
# my_set.add('h')
# print(my_set)
# my_set.add(1)
# print(my_set)
#
# my_set.remove('o')
# print(my_set)
#
# my_set.add('xyz')
# print(my_set)
#
# my_set.remove('2')  # raises an error if no such item
# print(my_set)
#
# my_set.discard('2')  # doesn't raise an error if no such item
# my_set.discard('xyz')
# my_set.discard(1)
# print(my_set)
#
# set1 = {4, 5, 1, 2, 3}
# set2 = {1, 2, 4, 5, 6}
# set3 = set1 & set2  # joins sets only for common values
# print(set3)
# set3 = set1.intersection(set2)
# print(set3)
# set3 = set1 | set2  # joins sets
# print(set3)
# set3 = set1 ^ set2  # joins sets only for unique values
# print(set3)
#
#
#
# tuples
# print(dir(tuple))
"""
Tuple methods: count, index
"""
# my_tuple = tuple('hello')
# print(my_tuple)
# my_tuple = ('h', 'e', 'l', 'l', 'o')
# print(my_tuple)
# print(my_tuple.count('l'))
# print(my_tuple.index('h'))
#
# set1 = (1)  # Python won't recognise this as a tuple
# print(set1, type(set1))
# set1 = (1, )  # but now it will
# print(set1, type(set1))
#
#
#
# print(sys.platform)
# print(os.getcwd())
# exec(open('../Module_1/ex_7_average_sum.py').read())
