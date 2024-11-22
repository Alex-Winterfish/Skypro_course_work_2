import main
from unittest.mock import patch


@patch("main.user_file_interaction")
@patch("main.user_interaction")
@patch("main.user_operation")
def test_main_1(mock_user_operation, mock_user_interaction, mock_interaction, capsys):
    """Функция проверяет взаимодействие с пользователем при работе с файлом"""
    mock_user_operation.return_value = "1"
    mock_user_interaction.return_value = "2"
    mock_interaction.return_value = "3"
    main.main()
    captured = capsys.readouterr()
    assert captured.out == ""


@patch("main.user_file_interaction")
@patch("main.user_interaction")
@patch("main.FileWriteJson")
@patch("main.HeadHunterAPI")
@patch("main.user_request")
@patch("main.user_operation")
def test_main_2(
    mock_user_operation,
    mock_user_request,
    mock_hh_ru,
    mock_file_write,
    mock_user_interaction,
    mock_interaction,
    mock_class_hh,
    mock_class_file_write,
    capsys,
):
    """Функция проверяет взаимодействие с пользователем при получении вакансий с НН.ру"""
    mock_user_operation.return_value = "2"
    mock_user_request.return_value = ("Вакансия", 100)
    mock_hh_ru.return_value = mock_class_hh("Вакансия")
    mock_file_write.return_value = mock_class_file_write
    mock_user_interaction.return_value = "1"
    mock_interaction.return_value = "1"
    main.main()
    captured = capsys.readouterr()
    assert captured.out == ""
