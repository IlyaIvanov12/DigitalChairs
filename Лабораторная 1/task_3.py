# TODO Найдите количество книг, которое можно разместить на дискете
full = 1.44
Number_of_page = 100
Number_of_strings = 50
Number_of_symbols_in_string = 25
Symbol_weight = 4
Book_weight = Symbol_weight * Number_of_symbols_in_string * Number_of_strings * Number_of_page / 1024 ** 2
Books = round(full // Book_weight)
print("Количество книг, помещающихся на дискету:", Books)
