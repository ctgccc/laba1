seq = input("Введите целое число: ")
fr_dict = {}

for num in range(len(seq)):
    if seq[num] in fr_dict:
        fr_dict[seq[num]] += 1
    else:
        fr_dict[seq[num]] = 1

print(fr_dict)