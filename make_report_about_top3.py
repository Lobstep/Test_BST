from operator import itemgetter
import openpyxl

students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}
students_avg_scores_list = []


def make_report_about_top3(students_avg_scores):
    students_scores_sort = dict(sorted(students_avg_scores.items(), key=itemgetter(1), reverse=True)[:3])
    for name_score in students_scores_sort.items():
        students_avg_scores_list.append(name_score)

    book = openpyxl.Workbook()
    sheet = book.active
    sheet.title = 'Топ 3 студента'
    row = 1
    sheet['A' + str(row)] = 'Студенты'
    sheet['B' + str(row)] = 'Средний балл'
    for item, value in students_avg_scores_list:
        row += 1
        sheet['A' + str(row)] = item
        sheet['B' + str(row)] = value
    book.save('students_top3.xlsx')


make_report_about_top3(students_avg_scores)
