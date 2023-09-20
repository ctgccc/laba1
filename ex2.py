
text = input("Введите слово:")
pair_lower = 0
pair_upper = 0
vowel_count = 0
for i in range(1, len(text)):
    if text[i - 1].islower() and text[i].islower():
        pair_lower += 1
    if text[i - 1].isupper() and text[i].isupper():
        pair_upper += 1
for letter in text:
    if letter.lower() in ['а', 'е', 'у', 'о', 'э', 'ы', 'я', 'и', 'ю', 'А', 'Е', 'У', 'О', 'Э', 'Ы', 'Я', 'И', 'Ю']:
        vowel_count += 1
print("Количество пар (стоящих рядом) верхнего регистра: ", pair_upper)
print("Количество пар (стоящих рядом) нижнего регистра:", pair_lower)
print("Количество гласных букв: ", vowel_count)
