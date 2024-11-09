from abc import ABC, abstractmethod


class VacancyAPI(ABC):

    @abstractmethod
    def __init__(self, vacancy, api_key):
        self.__api_key = api_key
        self.__vacancy = vacancy

    @abstractmethod
    def __api_request(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass


class HeadHunterAPI(VacancyAPI):

    url = 'https://api.hh.ru/vacancies/?'

    def __init__(self, vacancy, api_key):
        super().__init__(vacancy, api_key)


    def api_request(self):
        super().api_request()

        pass

    def get_vacancy(self):
        super().get_vacancy()
        pass
