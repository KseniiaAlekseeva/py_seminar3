slovar = {1: 3, 2: 5}
print(list(slovar.values()))
list_of_dicts = [{"V": "S001"},
                 {"V": "S002"},
                 {"VI": "S001"},
                 {"VI": "S005"},
                 {"VII": "S005"},
                 {"V": "S009"},
                 {"VIII": "S007"}]

uniq_els = set()

for el in list_of_dicts:
    for key in el:
        element = el[key]
        # element = list(el.values())[0]
        uniq_els.add(element)
print(uniq_els)

uniq_el1 = set(list(i.values())[0] for i in list_of_dicts)
print(uniq_el1)
