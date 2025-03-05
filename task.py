def merge_lists_to_dict(keys, values):
    result_dict = dict(zip(key, val))
    return result_dict


key = ['a', 'b', 'c']
val = [1, 2, 3]


merg = merge_lists_to_dict(key, val)


print(merg)
# Вызов функции с использованием аргументов с ключевыми словами
result = merge_lists_to_dict(list1=[1, 2, 3], list2=[4, 5, 6])

# Второй вызов функции с одним позиционным аргументом и одним аргументом с ключевым словом
result2 = merge_lists_to_dict([1, 2, 3], list2=[4, 5, 6])
