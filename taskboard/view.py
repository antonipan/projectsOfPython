def quantity_groups ():
    name = ''
    groups_list = []
    while 'ex' != name:
        name = input('Введите название группы: ')
        if name == 'ex': break
        groups_list.append(name)
    quantity = len(groups_list)
    return groups_list, quantity

def subjects ():
    name = ''
    subjects_list = []
    while 'ex' != name:
        name = input('Введите название предмета: ')
        if name == 'ex': break
        subjects_list.append(name)
    quantity = len(subjects_list)
    return subjects_list, quantity


def groups_print(qroups_list, quantity):
    print(qroups_list)
    print(quantity)

