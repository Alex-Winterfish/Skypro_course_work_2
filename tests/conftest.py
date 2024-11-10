import pytest
from pytest import fixture


@pytest.fixture
def test_response():
    return [
        {
            "arguments": [],
            "clusters": [],
            "fixes": [],
            "found": 13,
            "items": [
                {
                    "id": "109847610",
                    "premium": False,
                    "name": "Младший программист C++ (Windows, UNIX)",
                    "department": None,
                    "has_test": False,
                    "response_letter_required": False,
                    "area": {
                        "id": "2",
                        "name": "Санкт-Петербург",
                        "url": "https://api.hh.ru/areas/2",
                    },
                    "salary": {
                        "from": 130000,
                        "to": None,
                        "currency": "RUR",
                        "gross": False,
                    },
                    "type": {"id": "open", "name": "Открытая"},
                    "address": None,
                    "response_url": None,
                    "sort_point_distance": None,
                    "published_at": "2024-11-01T12:17:13+0300",
                    "created_at": "2024-11-01T12:17:13+0300",
                    "archived": False,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109847610",
                    "show_logo_in_search": None,
                    "insider_interview": None,
                    "url": "https://api.hh.ru/vacancies/109847610?host=hh.ru",
                    "alternate_url": "https://hh.ru/vacancy/109847610",
                    "relations": [],
                    "employer": {
                        "id": "241820",
                        "name": "Диалог-транс",
                        "url": "https://api.hh.ru/employers/241820",
                        "alternate_url": "https://hh.ru/employer/241820",
                        "logo_urls": {
                            "original": "https://img.hhcdn.ru/employer-logo-original/880166.jpg",
                            "240": "https://img.hhcdn.ru/employer-logo/3961540.jpeg",
                            "90": "https://img.hhcdn.ru/employer-logo/3961539.jpeg",
                        },
                        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=241820",
                        "accredited_it_employer": False,
                        "trusted": True,
                    },
                    "snippet": {
                        "requirement": "Понимание принципов объектно-ориентированного программирования. Опыт работы на железнодорожном транспорте в части систем управления сигнализацией, централизацией и блокировкой (<highlighttext>СЦБ</highlighttext>), и...",
                        "responsibility": "Разработка программного и информационного обеспечений в рамках развития компании. Разработка, оформление и согласование технической документации на программное обеспечение. ",
                    },
                    "contacts": None,
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "working_days": [],
                    "working_time_intervals": [],
                    "working_time_modes": [],
                    "accept_temporary": False,
                    "professional_roles": [
                        {"id": "156", "name": "BI-аналитик, аналитик данных"}
                    ],
                    "accept_incomplete_resumes": False,
                    "experience": {"id": "noExperience", "name": "Нет опыта"},
                    "employment": {"id": "full", "name": "Полная занятость"},
                    "adv_response_url": None,
                    "is_adv_vacancy": False,
                    "adv_context": None,
                }
            ],
            "page": 0,
            "pages": 13,
            "per_page": 1,
            "suggests": [],
        }
    ]
