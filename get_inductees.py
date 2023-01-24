names = ['Vasya', 'Alice', 'Petya', 'Jenny', 'Fedya', 'Viola', 'Mark', 'Chris', 'Margo', 'Roman', 'Viktor']
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001, 2009, 2013]
genders = ['Male', 'Female', 'Male', 'Female', 'Male', None, None, None, None, 'Male', 'Male']
now_year = 2021
men_military = []
year_specification = []
over_30 = []
under_18 = []
gender_clarification = []
woman = []
none = []


def get_inductees(names: list, birthday_years: list, genders: list):
    for name, year, gender in zip(names, birthday_years, genders):
        if year == None and gender == 'Male':
            year_specification.append(name)
        if year != None and (now_year - year) > 18 and gender == None:
            gender_clarification.append(name)
        if gender == 'Male' and year != None and (now_year - year) < 30 and (2021 - year) > 18:
            men_military.append(name)
        if gender == 'Female':
            woman.append(name)
        if year != None and gender == 'Male' and (now_year - year) > 30:
            over_30.append(name)
        if year == None and gender == None:
            none.append(name)
        if year != None and gender == 'Male' and (now_year - year) < 18:
            under_18.append(name + f' (через {18-(now_year-year)} лет может быть готов к военной службе)')

    print('Парни которые годны к военной службе:', *men_military)
    print('Парни у которых нужно уточнить год рождения:', *year_specification)
    print('Парни которым больше 30 лет:', *over_30)
    print('Парни которым меньше 18:', *under_18)
    print('Люди у которых нужно уточнить пол:', *gender_clarification)
    print('Девушки:', *woman)
    print('Люди у которых не известен пол и год рождения:', *none)


get_inductees(names, birthday_years, genders)
