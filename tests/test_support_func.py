# coding=UTF-8
import src.vacancy_processing
from src.support_func import user_operation, user_request, user_interaction, user_file_interaction
from unittest import mock
from unittest.mock import Mock, patch
import builtins

def test_user_operation(capsys):

    with mock.patch.object(builtins, 'input', lambda x: '1'):

        assert user_operation() == '1'
        captured = capsys.readouterr()
        assert captured.out == 'Добро пожаловать в программу обработки вакансий\n'


def test_user_request():
    with mock.patch.object(builtins,'input', lambda x: '1'):
        assert user_request() == ('1',1)


def test_user_interaction():
    with mock.patch.object(builtins, 'input', lambda x: '1'):
        assert user_interaction() == '1'
@patch('src.support_func.dummy_vacancy')
def test_file_interaction_1(mock_vacancy, test_file_vacancy):
    with mock.patch.object(builtins, 'input', lambda x: 'Вакансия'):
        user_file_interaction('1')
        mock_vacancy.return_value = test_file_vacancy.vacancy_get('Вакансия')
        assert mock_vacancy.assert_called_once_with(test_file_vacancy.vacancy_get('Вакансия'))

@patch('src.vacancy_processing.FileWriteJson.vacancy_salary')
def test_file_interaction_2(mock_vac_sal):
    mock_vac_sal.return_value={}
    with mock.patch.object(builtins, 'input', lambda x: '100'):

        user_file_interaction('2')

        assert mock_vac_sal.assert_called_once_with(100, 100)
