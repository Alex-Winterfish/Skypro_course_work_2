import json
import re
from abc import ABC, abstractmethod
from pathlib import PurePath


class VacancyProc:
    vacancy_name: str
    salary: float
    requirement: str
    vacancy_url: str
    schedule: str

    __slots__ = ("vacancy_name", "requirement", "vacancy_url", "schedule", "salary")

    def __init__(self, vacancy_name, requirement, vacancy_url, schedule, salary=None):
        self.vacancy_name = vacancy_name
        self.__validation(salary, requirement)
        self.vacancy_url = vacancy_url
        self.schedule = schedule

    def __validation(self, salary, requirement):
        if salary is None:
            self.salary = 0
        else:
            self.salary = salary
        if requirement is None:
            self.requirement = ""
        else:
            self.requirement = requirement

    def __gt__(self, other):

        return self.salary > other.salary

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
        return f"{self.__class__.__name__} ({self.vacancy_name}, {self.vacancy_url})"


class FileWrite(ABC):

    @abstractmethod
    def __init__(self, vacancy: VacancyProc):
        self.name = vacancy.vacancy_name
        self.salary = vacancy.salary
        self.requirement = vacancy.requirement
        self.vacancy_url = vacancy.vacancy_url
        self.schedule = vacancy.schedule
        self.vacancy_dict = dict()

    @abstractmethod
    def vacancy_write(self):
        pass

    @abstractmethod
    def vacancy_delite(self, search_string):
        pass

    @abstractmethod
    def vacancy_get(self, search_string):
        pass


class FileWriteJson(FileWrite):
    vacancy_id = 1

    def __init__(self, vacancy: VacancyProc, file_path=PurePath("data/vacancies.json")):
        self.__file_path = file_path
        super().__init__(vacancy)

    @property
    def vacancy_write(self):
        """Метод формирует словарь для добавления в файл"""
        super().vacancy_write()
        self.vacancy_dict["Название Вакансии"] = self.name
        self.vacancy_dict["Требования к вакансии"] = self.requirement
        self.vacancy_dict["Зарплата"] = self.salary
        self.vacancy_dict["Ссылка на вакансию НН.ru"] = self.vacancy_url

        stop = 0
        with open(self.__file_path, "r") as file:
            try:
                data = json.load(file)
                for vacancy in data:
                    if vacancy.get("Ссылка на вакансию НН.ru") == self.vacancy_url:
                        stop = 1
                        print("Vacancy already exist")
                    else:
                        continue

            except json.decoder.JSONDecodeError:
                data = list()

        if stop == 0:
            with open(self.__file_path, "w+") as file:
                data.append(self.vacancy_dict)
                json.dump(data, file, ensure_ascii=False, indent=1)

        FileWriteJson.vacancy_id += 1

    def vacancy_delite(self, search_string: str):
        super().vacancy_delite(search_string)

        try:
            with open(self.__file_path, "r+") as f:
                data = json.load(f)
            for vacancy in data:
                count = 0
                for key, value in vacancy.items():

                    if key not in ["Зарплата"]:
                        search_pattern = re.search(
                            f"{search_string}", value, flags=re.I
                        )
                        if search_pattern is not None:
                            count += 1
                if count > 0:
                    data.remove(vacancy)
                else:
                    continue

            with open(self.__file_path, "w") as f:
                json.dump(data, f, ensure_ascii=False, indent=-1, separators=(",", ":"))
        except Exception as e:
            print(f"Ошибка {e} в модуле json_delite")

    def vacancy_get(self, search_string: str):
        super().vacancy_get(search_string)
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
            count = 0
            for vacancy in data:
                for key, value in vacancy.items():
                    if key not in ["Зарплата"]:
                        search_pattern = re.search(
                            f"{search_string}", value, flags=re.I
                        )
                        if search_pattern is not None:
                            count += 1
                            print(vacancy)
                        else:
                            continue
            if count == 0:
                print("Вакансия не найдена")

        except Exception as e:
            print(f"Ошибка {e} в модуле vacancy_get")

    def vacancy_salary(self, min_sal: int, max_sal: int):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)

            i = 0
            for vacancy in data:
                if int(vacancy.get("Зарплата")) > max_sal:
                    i += 1
                else:
                    continue
            j = 0
            for vacancy in data:
                if int(vacancy.get("Зарплата")) >= min_sal:
                    j += 1
                else:
                    continue
            for vac in data[i:j]:
                print(vac)

        except Exception as e:
            print(f"Ошибка {e} в модуле vacancy_salary")


if __name__ == "__main__":

    vacancy1 = VacancyProc("монтер", "kghkh", "sdfd", "sfsf")
    vacancy2 = VacancyProc("механик", "kghkh", "sdfd", "sfsf", 30000)
    vacancy3 = VacancyProc.new_vacancy(
        [
            "Младший программист C++ (Windows, UNIX)",
            130000,
            "https://api.hh.ru/vacancies/109847610?host=hh.ru",
            "Понимание принципов объектно-ориентированного программирования. Опыт работы на железнодорожном транспорте в части систем управления сигнализацией, централизацией и блокировкой (<highlighttext>СЦБ</highlighttext>), и...",
            "Электромеханик СЦБ",
            "полный день",
        ]
    )
    print(vacancy2.salary)

    vacancy4 = VacancyProc("уборщик", "cleaning", "sdfdsf", "sdfd")

    # file_vacancy = FileWriteJson(vacancy2, '../data/vacancies.json').json_write
    # file_vacancy1 = FileWriteJson(vacancy1)
    # file_vacancy2 = FileWriteJson(vacancy2)
    # file_vacancy3 = FileWriteJson(vacancy3)
    # file_vacancy4 = FileWriteJson(vacancy4)

    # print(file_vacancy)
    # file_vacancy1.vacancy_write
    # file_vacancy2.vacancy_write
    # file_vacancy4.vacancy_write
    # print(file_vacancy3.vacancy_salary(0, 120_000))
    # print(file_vacancy4.vacancy_delite('уборщик'))
