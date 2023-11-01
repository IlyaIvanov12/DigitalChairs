def find_index(list_, find_it):
    if find_it in list_:
        index = list_.index(find_it)
        return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_item_list = ['банан', 'груша', 'персик']
for find_item in find_item_list:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
