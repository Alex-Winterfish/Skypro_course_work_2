from src.vacancy_processing import VacancyProc, FileWriteJson


def user_operation():
    print("Добро пожаловать в программу обработки вакансий")
    user_input = input(
        "Какие операции выполнить?\n"
        "1 - обработка вакансий из файла\n"
        "2 - выгрузка вакансий с сайта\n"
    )
    return user_input


def user_request():
    search_str = input("Введите вакансию для поиска на HH.ru: ")
    vac_lim = input("Введите число вакансий для обработки: ")
    return search_str, int(vac_lim)


def user_interaction():

    user_input = input(
        "Какие операции с вакансиями выполнить? \n"
        "1 - поиск по названию\n"
        "2 - поиск по вилке зарплат\n"
        "3 - удаление\n"
    )

    return user_input


dummy_vac = VacancyProc(
        0,
        0,
        0,
        0,
    )
dummy_f_vac = FileWriteJson(dummy_vac)

def user_file_interaction(user_input: str):

    if user_input == "1":
        input_string = input("Что искать?: ")
        vacancy = dummy_f_vac.vacancy_get(input_string)
        return vacancy

    elif user_input == "2":
        min_sal = int(input("Введите нижний предел зарплаты "))
        max_sal = int(input("Введите верхний предел зарплаты "))
        dummy_f_vac.vacancy_salary(min_sal, max_sal)

    elif user_input == "3":
        search_string = input("Какую вакансию удалить? ")
        dummy_f_vac.vacancy_delite(search_string)
