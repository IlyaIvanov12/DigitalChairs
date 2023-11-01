def find_common(first, second):
    first_ = set(first.split('|'))
    second_ = set(second.split('|'))
    common = sorted(list(first_.intersection(second_)))
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
