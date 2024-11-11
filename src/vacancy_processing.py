import json

class VacancyProc:
    vacancy_name: str
    salary: float
    requirement: str
    vacancy_url: str
    schedule: str
    vacancy_list: list

    __slots__ = ('vacancy_name', 'requirement', 'vacancy_url', 'schedule', 'salary')

    def __init__(self,vacancy_name, requirement, vacancy_url, schedule, salary=None):
        self.vacancy_name = vacancy_name
        if salary is None:
            self.salary = 'Зарплата не указана'
        else:
            self.salary = salary
        self.requirement = requirement
        self.vacancy_url = vacancy_url
        self.schedule = schedule

    def __le__(self, other):
        if self.salary != 'Зарплата не указана' and other.salary != 'Зарплата не указана':
            return self.salary < other.salary
        else:
            print('Не указана зарплата')

    def __ge__(self, other):
        if self.salary != 'Зарплата не указана' and other.salary != 'Зарплата не указана':
            return self.salary >= other.salary
        else:
            print('Не указана зарплата')

    def __gt__(self,other):
        if self.salary != 'Зарплата не указана' and other.salary != 'Зарплата не указана':
            return self.salary > other.salary
        else:
            print('Не указана зарплата')



    @classmethod
    def new_vacancy(
        cls,
        new_vacancy,
    ):
        vacancy_name = new_vacancy[0]
        salary = new_vacancy[1]
        vacancy_url = new_vacancy[2]
        requirement = new_vacancy[3]
        schedule = new_vacancy[4]

        return cls(vacancy_name, requirement, vacancy_url, schedule, salary)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.vacancy_name}, {self.vacancy_url})'


class FileWriteJson:

    vacancy_id = 1

    def __init__(self, vacancy:VacancyProc, file_path=None):
        self.file_path = file_path
        self.name = vacancy.vacancy_name
        self.salary = vacancy.salary
        self.requirement = vacancy.requirement
        self.vacancy_url = vacancy.vacancy_url
        self.schedule = vacancy.schedule
        self.vacancy_dict = dict()

    @property
    def json_write(self):
        'Метод формирует словарь для добавления в файл'
        self.vacancy_dict['id вакансии'] = FileWriteJson.vacancy_id
        self.vacancy_dict['Название Вакансии'] = self.name
        self.vacancy_dict['Требования к вакансии'] = self.requirement
        self.vacancy_dict['Зарплата'] = self.salary
        self.vacancy_dict['Ссылка на вакансию НН.ru'] = self.vacancy_url
        with open(self.file_path, 'a') as f:
            json.dump(self.vacancy_dict, f, ensure_ascii=False, indent=-1, separators=(',', ':'))
        FileWriteJson.vacancy_id += 1

    @property
    def json_delite(self):

        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data




if __name__ == '__main__':

    vacancy1 = VacancyProc('монтер', 'kghkh', 'sdfd', 'sfsf')
    vacancy2 = VacancyProc('механик', 'kghkh', 'sdfd', 'sfsf', 30000)


    file_vacancy = FileWriteJson(vacancy1, '../data/vacancies.json').json_write

    #print(file_vacancy.json_delite)