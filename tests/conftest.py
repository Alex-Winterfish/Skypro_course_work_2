import pytest
from src.vacancy_processing import FileWriteJson, VacancyProc


@pytest.fixture
def test_response():
    return {
        "items": [
            {
                "id": "109221333",
                "premium": "false",
                "name": "Менеджер по продажам услуг",
                "department": "null",
                "has_test": "false",
                "response_letter_required": "false",
                "area": {
                    "id": "160",
                    "name": "Алматы",
                    "url": "https://api.hh.ru/areas/160",
                },
                "salary": {
                    "from": 300000,
                    "to": "null",
                    "currency": "KZT",
                    "gross": "true",
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": "null",
                "response_url": "null",
                "sort_point_distance": "null",
                "published_at": "2024-10-24T13:17:13+0300",
                "created_at": "2024-10-24T13:17:13+0300",
                "archived": "false",
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
                "show_logo_in_search": "null",
                "insider_interview": "null",
                "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/109221333",
                "relations": [],
                "employer": {
                    "id": "2144643",
                    "name": "Центр профессиональной подготовки Nurikon",
                    "url": "https://api.hh.ru/employers/2144643",
                    "alternate_url": "https://hh.ru/employer/2144643",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                        "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                        "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
                    "accredited_it_employer": "false",
                    "trusted": "true",
                },
                "snippet": {
                    "requirement": "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший уровень английского.",
                    "responsibility": "Общение по телефону с компаниями сфере недропользования(нефть, уран, горнорудное дело) по базе клиентов , созданной компанией в течение 16 лет. ",
                },
                "contacts": "null",
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": "false",
                "professional_roles": [
                    {
                        "id": "70",
                        "name": "Менеджер по продажам, менеджер по работе с клиентами",
                    }
                ],
                "accept_incomplete_resumes": "false",
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": "null",
                "is_adv_vacancy": "false",
                "adv_context": "null",
            },
            {
                "id": "108388097",
                "premium": "false",
                "name": "Оператор call-центра",
                "department": "null",
                "has_test": "false",
                "response_letter_required": "false",
                "area": {
                    "id": "2759",
                    "name": "Ташкент",
                    "url": "https://api.hh.ru/areas/2759",
                },
                "salary": {
                    "from": "null",
                    "to": 5500000,
                    "currency": "UZS",
                    "gross": "false",
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "Ташкент",
                    "street": "Яшнободский район",
                    "building": "махалля Чулпон",
                    "lat": 41.305373,
                    "lng": 69.302293,
                    "description": "null",
                    "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                    "metro": "null",
                    "metro_stations": [],
                    "id": "13982896",
                },
                "response_url": "null",
                "sort_point_distance": "null",
                "published_at": "2024-11-05T09:05:05+0300",
                "created_at": "2024-11-05T09:05:05+0300",
                "archived": "false",
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
                "show_logo_in_search": "null",
                "insider_interview": "null",
                "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/108388097",
                "relations": [],
                "employer": {
                    "id": "10011655",
                    "name": "CALLTRAFFIC",
                    "url": "https://api.hh.ru/employers/10011655",
                    "alternate_url": "https://hh.ru/employer/10011655",
                    "logo_urls": {
                        "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                        "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                        "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
                    "accredited_it_employer": "false",
                    "trusted": "true",
                },
                "snippet": {
                    "requirement": "Знание русского языка и компьютера. Умение общаться с людьми.",
                    "responsibility": "Отвечать на входящие звонки от клиентов. Помогать клиентам с их вопросами. Быть вежливым и дружелюбным.",
                },
                "contacts": "null",
                "schedule": {"id": "flexible", "name": "Гибкий график"},
                "working_days": [],
                "working_time_intervals": [
                    {
                        "id": "from_four_to_six_hours_in_a_day",
                        "name": "Можно сменами по 4-6 часов в день",
                    }
                ],
                "working_time_modes": [
                    {"id": "start_after_sixteen", "name": "С началом дня после 16:00"}
                ],
                "accept_temporary": "true",
                "professional_roles": [
                    {
                        "id": "83",
                        "name": "Оператор call-центра, специалист контактного центра",
                    }
                ],
                "accept_incomplete_resumes": "true",
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": "null",
                "is_adv_vacancy": "false",
                "adv_context": "null",
            },
        ]
    }


@pytest.fixture
def test_dummy_vac1():
    return ["dummy#1", 10, "url/new", "shallow", "shift"]


@pytest.fixture
def test_dummy_vac2():
    return ["dummy#2", 1000, "url/new", "shallow", "shift"]


@pytest.fixture
def test_vacancy_1(test_dummy_vac1):
    vacancy = VacancyProc.new_vacancy(test_dummy_vac1)
    return vacancy


@pytest.fixture
def test_vacancy_2(test_dummy_vac2):
    vacancy = VacancyProc.new_vacancy(test_dummy_vac2)
    return vacancy
