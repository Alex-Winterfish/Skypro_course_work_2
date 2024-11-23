# coding=UTF-8
from src.support_func import (
    user_operation,
    user_request,
    user_interaction,
    user_file_interaction,
)
from unittest import mock
from unittest.mock import patch
import builtins


def test_user_operation(capsys):

    with mock.patch.object(builtins, "input", lambda x: "1"):

        assert user_operation() == "1"
        captured = capsys.readouterr()
        assert captured.out == "Добро пожаловать в программу обработки вакансий\n"


def test_user_request():
    with mock.patch.object(builtins, "input", lambda x: "1"):
        assert user_request() == ("1", 1)


def test_user_interaction():
    with mock.patch.object(builtins, "input", lambda x: "1"):
        assert user_interaction() == "1"


@patch("src.support_func.dummy_f_vac")
def test_file_interaction_1(mock_vacancy, test_file_vacancy):
    with mock.patch.object(builtins, "input", lambda x: "Вакансия"):
        user_file_interaction("1")
        mock_vacancy.vacancy_get.return_value = {
            "Название Вакансии": "Электромеханик СЦБ"
        }
        assert user_file_interaction("1") == {"Название Вакансии": "Электромеханик СЦБ"}
        assert mock_vacancy.assert_called_once


@patch("src.support_func.dummy_f_vac")
def test_file_interaction_2(mock_vac_sal):
    mock_vac_sal.return_value = {""}
    with mock.patch.object(builtins, "input", lambda x: "100"):

        user_file_interaction("2")

        assert mock_vac_sal.assert_called_once


@patch("src.support_func.dummy_f_vac")
def test_file_interaction_3(mock_vac_del):
    mock_vac_del.return_value = {""}
    with mock.patch.object(builtins, "input", lambda x: "Вакансия"):

        user_file_interaction("3")

        assert mock_vac_del.assert_called_once
