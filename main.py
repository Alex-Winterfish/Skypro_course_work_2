from src.classes_api import HeadHunterAPI
from src.vacancy_processing import VacancyProc, FileWriteJson

def user_request():
    search_str = input('Введите вакансию: ')
    vac_lim = input('Введите число вакансий для обработки: ')
    return search_str, int(vac_lim)

def main():

    vacancy_search, vacancy_lim = user_request()

    user_vacancy = HeadHunterAPI(vacancy_search)

    user_vacancy_list = user_vacancy.vacancy_list[0:vacancy_lim]

    for i in range(len(user_vacancy_list)):
        FileWriteJson(VacancyProc.new_vacancy(user_vacancy_list[i])).vacancy_write

def vacancy_processing():

    user_input = input('Какие операции с вакансиями выполнить? \n' 
                       '1 - поиск по названию\n'
                       '2 - поиск по вилке зарплат\n'
                       '3 - удаление')

    if user_input == 1:
        input_string = input('Что искать?: ')
        vacancy = FileWriteJson.vacancy_get(input_string)
        return vacancy
    elif user_input == 2:



if __name__ == '__main__':

    main()