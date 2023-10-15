numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
len_ = len(numbers)
total = sum(filter(lambda x: isinstance(x, (int, float)), numbers))
numbers[numbers.index(None)] = total/len_
print('Измененный список:', numbers)

