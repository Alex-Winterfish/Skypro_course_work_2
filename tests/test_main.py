import main
from unittest import mock
from unittest.mock import patch
import builtins

@patch('main.user_file_interaction')
@patch('main.user_interaction')
@patch('main.user_operation')
def test_main(mock_user_operation,mock_user_interaction, mock_interaction, capsys):
    mock_user_operation.return_value = '1'
    mock_user_interaction.return_value = '2'
    mock_interaction.return_value = '3'
    main.main()
    captured = capsys.readouterr()
    assert (
        captured.out == '')