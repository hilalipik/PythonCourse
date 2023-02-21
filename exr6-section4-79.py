some_list = ['a', 'b', 'c', 'd', 'b','m','n','n']

doup = []

for letter in some_list:
    if some_list.count(letter) > 1 and letter not in doup:
        doup.append(letter)
print (doup)