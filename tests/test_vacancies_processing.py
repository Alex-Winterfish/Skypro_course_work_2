from src.vacancy_processing import FileWrite, FileWriteJson, VacancyProc
from unittest import mock
from unittest.mock import patch

def test_vacancy_init():
    """Функция проверяет инициализацию экземпляра класса"""
    vacancy = VacancyProc("dummy", "shallow", "url/", "shift", 100)
    assert vacancy.vacancy_name == "dummy"
    assert vacancy.requirement == "shallow"
    assert vacancy.vacancy_url == "url/"
    assert vacancy.schedule == "shift"
    assert vacancy.salary == 100


def test_new_vacancy(test_dummy_vac):
    """Функция проверяет создание класса через конструктор new_vacancy"""
    vacancy = VacancyProc("dummy", "shallow", "url/", "shift", 100)
    vacancy1 = vacancy.new_vacancy(test_dummy_vac)
    assert vacancy1.vacancy_name == "dummy#2"
    assert vacancy1.requirement == "shallow"
    assert vacancy1.vacancy_url == "url/new"
    assert vacancy1.schedule == "shift"
    assert vacancy1.salary == 1000


def test_validation():
    """Функция проверяет метод валидации"""
    vacancy1 = VacancyProc(
        "dummy",
        None,
        "url/",
        "shift",
    )
    assert vacancy1.salary == 0
    assert vacancy1.requirement == ""


def test_compare(test_dummy_vac1, test_dummy_vac2):
    """Функция проверяет возможность сравнения экземпляров класа по зарплате"""
    vacancy1 = VacancyProc.new_vacancy(test_dummy_vac1)
    vacancy2 = VacancyProc.new_vacancy(test_dummy_vac2)
    assert (vacancy1 < vacancy2) == True


def test_file_write_json_init(test_vacancy_1):
    """Функция проверяет инициализацию экземпляра класса FileWriteJson"""
    vacancy = FileWriteJson(test_vacancy_1)
    assert vacancy.name == "dummy#1"
    assert vacancy.requirement == "shallow"
    assert vacancy.vacancy_url == "url/new"
    assert vacancy.schedule == "shift"
    assert vacancy.salary == 10


def test_file_write_json_w(test_vacancy_1):
    """Функция проверяет запись в файл"""

    vacancy = FileWriteJson(test_vacancy_1)
    with mock.patch("builtins.open", mock.mock_open()) as open_mock:
        vacancy.vacancy_write
        assert open_mock.call_count == 2
        assert open_mock().write.call_args_list == [
            mock.call("[\n "),
            mock.call("{"),
            mock.call("\n  "),
            mock.call('"Название Вакансии"'),
            mock.call(": "),
            mock.call('"dummy#1"'),
            mock.call(",\n  "),
            mock.call('"Требования к вакансии"'),
            mock.call(": "),
            mock.call('"shallow"'),
            mock.call(",\n  "),
            mock.call('"Зарплата"'),
            mock.call(": "),
            mock.call("10"),
            mock.call(",\n  "),
            mock.call('"Ссылка на вакансию НН.ru"'),
            mock.call(": "),
            mock.call('"url/new"'),
            mock.call("\n "),
            mock.call("}"),
            mock.call("\n"),
            mock.call("]"),
        ]

def test_file_write_json_del(test_vacancy_1):
    '''Функция проверяет удаление вакансии из файла'''
    vacancy = FileWriteJson(test_vacancy_1)
    with mock.patch("builtins.open", mock.mock_open()) as open_mock:
        vacancy.vacancy_delite('вакансия')
        assert open_mock.call_count == 1

def test_file_write_json_get_vac(test_vacancy_1):
    '''Функция проверяет'''
    vacancy = FileWriteJson(test_vacancy_1)
    with mock.patch("builtins.open", mock.mock_open()) as open_mock:
        vacancy.vacancy_get('вакансия')
        assert open_mock.call_count == 1

def test_file_write_json_get_sal(test_vacancy_1):
    '''Функция проверяет'''
    vacancy = FileWriteJson(test_vacancy_1)
    with mock.patch("builtins.open", mock.mock_open()) as open_mock:
        vacancy.vacancy_salary(0,100)
        assert open_mock.call_count == 1

