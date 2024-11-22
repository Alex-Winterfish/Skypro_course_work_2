from src.classes_api import HeadHunterAPI, VacancyAPI
from unittest.mock import patch


@patch("src.classes_api.HeadHunterAPI._api_request")
def test_init_hh_class_vacancy_list(mock_api_request, test_response):
    """Функция проверяет работу метода vacancy_list класса HeadHunterAPI"""
    mock_api_request.return_value = test_response
    vacancy1 = HeadHunterAPI("менеджер")

    assert vacancy1.vacancy_list == [
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
        [
            "Менеджер по продажам услуг",
            300000,
            "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "Необходимо иметь отличную успеваемость в школе, желателен опыт работы в "
            "продажах. Коммуникабельность. Обучаемость. Мобильность. Желательно, хороший "
            "уровень английского.",
            "Полный день",
        ],
        [
            "Оператор call-центра",
            "null",
            "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "Знание русского языка и компьютера. Умение общаться с людьми.",
            "Гибкий график",
        ],
    ]


@patch("src.classes_api.HeadHunterAPI._api_request")
def test_init_hh_class_get_vacancy(mock_api_request, test_response):
    """Функция проверяет работу метода get_vacancy класса HeadHunterAPI"""
    mock_api_request.return_value = test_response
    vacancy2 = HeadHunterAPI("менеджер")

    assert vacancy2._get_vacancies == [
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
        {
            "accept_incomplete_resumes": "false",
            "accept_temporary": "false",
            "address": "null",
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/109221333",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109221333",
            "archived": "false",
            "area": {
                "id": "160",
                "name": "Алматы",
                "url": "https://api.hh.ru/areas/160",
            },
            "contacts": "null",
            "created_at": "2024-10-24T13:17:13+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/2144643",
                "id": "2144643",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/5727065.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5727064.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1026574.png",
                },
                "name": "Центр профессиональной подготовки Nurikon",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/2144643",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2144643",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "109221333",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Менеджер по продажам услуг",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "70",
                    "name": "Менеджер по продажам, менеджер по работе с " "клиентами",
                }
            ],
            "published_at": "2024-10-24T13:17:13+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "KZT",
                "from": 300000,
                "gross": "true",
                "to": "null",
            },
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Необходимо иметь отличную успеваемость в школе, "
                "желателен опыт работы в продажах. "
                "Коммуникабельность. Обучаемость. Мобильность. "
                "Желательно, хороший уровень английского.",
                "responsibility": "Общение по телефону с компаниями сфере "
                "недропользования(нефть, уран, горнорудное "
                "дело) по базе клиентов , созданной компанией "
                "в течение 16 лет. ",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/109221333?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": "true",
            "accept_temporary": "true",
            "address": {
                "building": "махалля Чулпон",
                "city": "Ташкент",
                "description": "null",
                "id": "13982896",
                "lat": 41.305373,
                "lng": 69.302293,
                "metro": "null",
                "metro_stations": [],
                "raw": "Ташкент, Яшнободский район, махалля Чулпон",
                "street": "Яшнободский район",
            },
            "adv_context": "null",
            "adv_response_url": "null",
            "alternate_url": "https://hh.ru/vacancy/108388097",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108388097",
            "archived": "false",
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759",
            },
            "contacts": "null",
            "created_at": "2024-11-05T09:05:05+0300",
            "department": "null",
            "employer": {
                "accredited_it_employer": "false",
                "alternate_url": "https://hh.ru/employer/10011655",
                "id": "10011655",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/6334615.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/6334614.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1178547.jpg",
                },
                "name": "CALLTRAFFIC",
                "trusted": "true",
                "url": "https://api.hh.ru/employers/10011655",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10011655",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "has_test": "false",
            "id": "108388097",
            "insider_interview": "null",
            "is_adv_vacancy": "false",
            "name": "Оператор call-центра",
            "premium": "false",
            "professional_roles": [
                {
                    "id": "83",
                    "name": "Оператор call-центра, специалист " "контактного центра",
                }
            ],
            "published_at": "2024-11-05T09:05:05+0300",
            "relations": [],
            "response_letter_required": "false",
            "response_url": "null",
            "salary": {
                "currency": "UZS",
                "from": "null",
                "gross": "false",
                "to": 5500000,
            },
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "show_logo_in_search": "null",
            "snippet": {
                "requirement": "Знание русского языка и компьютера. Умение "
                "общаться с людьми.",
                "responsibility": "Отвечать на входящие звонки от клиентов. "
                "Помогать клиентам с их вопросами. Быть "
                "вежливым и дружелюбным.",
            },
            "sort_point_distance": "null",
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/108388097?host=hh.ru",
            "working_days": [],
            "working_time_intervals": [
                {
                    "id": "from_four_to_six_hours_in_a_day",
                    "name": "Можно сменами по\xa04-6\xa0часов в\xa0" "день",
                }
            ],
            "working_time_modes": [
                {"id": "start_after_sixteen", "name": "С\xa0началом дня после 16:00"}
            ],
        },
    ]


def test_abcstract_class():
    "Функция проверяет работу абстрактного класса VacancyAPI"

    class DummyClass(VacancyAPI):

        def __init__(self, vacancy):
            super().__init__(vacancy)
            self.vacancy = vacancy

        def _api_request(self):
            super()._api_request()
            vacancies = (self.vacancy + " ") * 2
            return vacancies

        def _get_vacancies(self):
            super()._get_vacancies()
            test_vacancies = (self.vacancy + " ") * 4
            return test_vacancies

    dummy_vacancy = DummyClass("Вакансия")
    assert dummy_vacancy.vacancy == "Вакансия"
    assert dummy_vacancy._api_request() == "Вакансия Вакансия "
    assert dummy_vacancy._get_vacancies() == "Вакансия Вакансия Вакансия Вакансия "
