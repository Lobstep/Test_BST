know_english = ['Vasya', 'Jimmy', 'Max', 'Peter', 'Eric', 'Zoi', 'Felix']
sportsmen = ['Don', 'Peter', 'Eric', 'Jimmy', 'Mark']
more_than_20_years = ['Peter', 'Julie', 'Jimmy', 'Mark', 'Max']
name_list = []


def find_athlets():
    for name in *know_english, *sportsmen, *more_than_20_years:
        if name in know_english and name in sportsmen and name in more_than_20_years:
            name_list.append(name)
    print('Студенты которые проходят по всем трём категориям:', *sorted(set(name_list)))


find_athlets()