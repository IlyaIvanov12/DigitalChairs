def count_letters(let):
    let = let.lower()
    letter = list(let)
    new_letter = []
    for index, i in enumerate(letter):
        if i.isalpha():
            new_letter.append(i)
    letter_dict = {}
    for index, i in enumerate(new_letter):
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    return letter_dict


def calculate_frequency(letters_dict):
    p = sum(letters_dict.values())
    for i in letters_dict:
        letters_dict[i] /= p
        letters_dict[i] = round(letters_dict[i], 2)
    return letters_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letter = count_letters(main_str)
dict = calculate_frequency(letter)
for key, value in dict.items():
    print(f"{key}: {value}")
# TODO Распечатайте в столбик букву и её частоту в тексте
