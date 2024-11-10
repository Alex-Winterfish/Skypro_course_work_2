from src.classes_api import HeadHunterAPI, VacancyAPI
from unittest.mock import patch, Mock


@patch("src.classes_api.HeadHunterAPI._api_request")
def test_init_hh_class(mock_api_request, test_response):
    mock_api_request.return_value = test_response
    vacancy1 = HeadHunterAPI("vacancy")

    assert vacancy1._get_vacancies == ""


def test_request():
    vacancy = HeadHunterAPI("Python")
    assert vacancy.vacancies_request == ""
