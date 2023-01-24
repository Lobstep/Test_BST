from operator import itemgetter


def find_top_20():
    candidates = [
        {'name': 'Vasya', 'scores': {'math': 58, 'russian_language': 62, 'computer_science': 48}, 'extra_scores': 0},
        {'name': 'Fedya', 'scores': {'math': 33, 'russian_language': 85, 'computer_science': 42}, 'extra_scores': 2},
        {'name': 'Petya', 'scores': {'math': 92, 'russian_language': 33, 'computer_science': 34}, 'extra_scores': 1},
        {'name': 'Sandra', 'scores': {'math': 59, 'russian_language': 39, 'computer_science': 45}, 'extra_scores': 0},
        {'name': 'Sophia', 'scores': {'math': 67, 'russian_language': 47, 'computer_science': 34}, 'extra_scores': 2},
        {'name': 'Alice', 'scores': {'math': 56, 'russian_language': 31, 'computer_science': 44}, 'extra_scores': 1},
        {'name': 'Ethan', 'scores': {'math': 67, 'russian_language': 57, 'computer_science': 54}, 'extra_scores': 2},
        {'name': 'Ann', 'scores': {'math': 34, 'russian_language': 38, 'computer_science': 47}, 'extra_scores': 0},
        {'name': 'Natalie', 'scores': {'math': 45, 'russian_language': 89, 'computer_science': 29}, 'extra_scores': 2},
        {'name': 'Margaret', 'scores': {'math': 48, 'russian_language': 33, 'computer_science': 39}, 'extra_scores': 1},
        {'name': 'Elizabeth', 'scores': {'math': 87, 'russian_language': 37, 'computer_science': 46}, 'extra_scores': 2},
        {'name': 'Veronica', 'scores': {'math': 78, 'russian_language': 52, 'computer_science': 47}, 'extra_scores': 0},
        {'name': 'Julia', 'scores': {'math': 20, 'russian_language': 75, 'computer_science': 50}, 'extra_scores': 2},
        {'name': 'Dora', 'scores': {'math': 90, 'russian_language': 34, 'computer_science': 34}, 'extra_scores': 1},
        {'name': 'Peter', 'scores': {'math': 69, 'russian_language': 38, 'computer_science': 56}, 'extra_scores': 2},
        {'name': 'Paul', 'scores': {'math': 56, 'russian_language': 42, 'computer_science': 55}, 'extra_scores': 0},
        {'name': 'Nicholas', 'scores': {'math': 50, 'russian_language': 58, 'computer_science': 46}, 'extra_scores': 2},
        {'name': 'Michael', 'scores': {'math': 63, 'russian_language': 41, 'computer_science': 51}, 'extra_scores': 1},
        {'name': 'Matthew', 'scores': {'math': 39, 'russian_language': 67, 'computer_science': 33}, 'extra_scores': 2},
        {'name': 'Leo', 'scores': {'math': 88, 'russian_language': 72, 'computer_science': 32}, 'extra_scores': 0},
        {'name': 'Joseph', 'scores': {'math': 83, 'russian_language': 58, 'computer_science': 31}, 'extra_scores': 2},
        {'name': 'Dennis', 'scores': {'math': 52, 'russian_language': 89, 'computer_science': 41}, 'extra_scores': 1},
        {'name': 'Roman', 'scores': {'math': 29, 'russian_language': 55, 'computer_science': 39}, 'extra_scores': 2},
        {'name': 'Daniel', 'scores': {'math': 78, 'russian_language': 33, 'computer_science': 45}, 'extra_scores': 0},
        {'name': 'Gregory', 'scores': {'math': 53, 'russian_language': 44, 'computer_science': 47}, 'extra_scores': 2},
        {'name': 'Harry', 'scores': {'math': 72, 'russian_language': 77, 'computer_science': 32}, 'extra_scores': 1},
        {'name': 'Valentine', 'scores': {'math': 67, 'russian_language': 48, 'computer_science': 44}, 'extra_scores': 2},
        {'name': 'Boris', 'scores': {'math': 89, 'russian_language': 61, 'computer_science': 41}, 'extra_scores': 0},
        {'name': 'Alex', 'scores': {'math': 55, 'russian_language': 85, 'computer_science': 34}, 'extra_scores': 2},
        {'name': 'Anthony', 'scores': {'math': 45, 'russian_language': 73, 'computer_science': 46}, 'extra_scores': 1},
        {'name': 'Andrew', 'scores': {'math': 43, 'russian_language': 40, 'computer_science': 28}, 'extra_scores': 2},
        {'name': 'Isabella', 'scores': {'math': 48, 'russian_language': 88, 'computer_science': 29}, 'extra_scores': 0},
        {'name': 'Sophia', 'scores': {'math': 93, 'russian_language': 69, 'computer_science': 30}, 'extra_scores': 0},
        {'name': 'Ava', 'scores': {'math': 87, 'russian_language': 39, 'computer_science': 39}, 'extra_scores': 1},
        {'name': 'Emma', 'scores': {'math': 51, 'russian_language': 48, 'computer_science': 40}, 'extra_scores': 2},
    ]

    student = []
    ranging_student = []
    scores_stud = []
    scores_math = []
    scores_comp = []
    result_scor_stud = {}

    for index, i in enumerate(candidates, 1):
        name = i['name']
        math = i['scores']['math']
        russian_language = i['scores']['russian_language']
        computer_science = i['scores']['computer_science']
        extra_scores = i['extra_scores']
        scores_all = math + russian_language + computer_science + extra_scores
        student.append(name)
        scores_stud.append(scores_all)
        scores_math.append(math)
        scores_comp.append(computer_science)
        for x in range(0, len(student)):
            result_scor_stud[student[x]] = scores_stud[x], scores_math[x], scores_comp[x]

    result_dic = dict(sorted(result_scor_stud.items(), key=itemgetter(1), reverse=True))
    res_lis = list(result_dic.items())
    last_place = str(res_lis[19][1][0])
    top_20 = []
    for index, res in enumerate(res_lis, 1):
        stud_num = f'{index}: {res[0]} - количество балл(a/ов): {res[1][0]}'
        stud_last = f'{index}: {res[0]} - количество балл(a/ов): {res[1][0]}. Математика: {res[1][1]} балл(a/ов), Информатика: {res[1][2]} балл(a/ов)'
        top_20.append(''.join(stud_num))
        ranging_student.append(''.join((stud_last)))
    print(*top_20[:20], sep='\n')
    print('\nСписок студентов, чьё количество баллов одинаковое и претендуют на 20 место в список:\n')
    count_last = 0
    for number in ranging_student:
        count_last += 1
        if last_place in number and count_last > 20:
            print(number)


find_top_20()


























