
class VacancyProc:
    vacancy_name: str
    salary: float
    requirement: str
    vacancy_url: str
    schedule: str

    def __init__(self,vacancy_name, salary, requirement, vacancy_url, schedule):
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.requirement = requirement
        self.vacancy_url = vacancy_url
        self.schedule = schedule

