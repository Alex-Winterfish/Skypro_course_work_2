import main
from unittest import mock
from unittest.mock import patch
import builtins

@patch('src.support_func.user_file_interaction')
@patch('src.support_func.user_interaction')
@patch('src.support_func.user_operation')
def test_main(mock_user_operation,mock_user_interaction, mock_interaction):
    mock_user_operation.return_value = '1'
    mock_user_interaction.return_value = '2'
    mock_interaction.return_value = '2'
    main()
    pass