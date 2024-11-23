from src.classes_api import HeadHunterAPI
from src.vacancy_processing import VacancyProc, FileWriteJson
from src.support_func import user_request, user_operation, user_interaction,user_file_interaction




def main():

    while True:

        operation_choice = user_operation()
        if operation_choice in ['1','2']:
            break

    if operation_choice == '1':


        while True:

            user_input = user_interaction()
            if user_input in ['1', '2', '3']:
                break

        user_file_interaction(user_input)

    else:

        vacancy_search, vacancy_lim = user_request()

        user_vacancy = HeadHunterAPI(vacancy_search)

        user_vacancy_lim = user_vacancy.vacancy_list[0:vacancy_lim]

        user_vacancy_list = [VacancyProc.new_vacancy(user_vacancy_lim[i]) for i in range(len(user_vacancy_lim))]

        user_vacancy_list = sorted(user_vacancy_list, reverse=True)

        for i in range(len(user_vacancy_list)):
            FileWriteJson(user_vacancy_list[i]).vacancy_write


        while True:

            user_input = user_interaction()
            if user_input in ['1','2','3']:
                break

        user_file_interaction(user_input)




if __name__ == '__main__':

    main()