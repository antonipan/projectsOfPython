import view

def buttom_click():
    groups_list, quantity1 = view.quantity_groups()
    subjects_list, quantity2 = view.subjects()
    view.groups_print(groups_list, quantity1)
    view.groups_print(subjects_list, quantity2)
