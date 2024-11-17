from src.support_func import user_operation, user_request, user_interaction, user_file_interaction
from unittest import mock
from unittest.mock import patch
import builtins

def test_user_operation():
    with mock.patch.object(builtins, 'input', lambda x: '1'):
        assert user_operation() == '1'

def test_user_request():
    with mock.patch.object(builtins,'input', lambda x: '1'):
        assert user_request() == ('1',1)

def test_user_interaction():
    with mock.patch.object(builtins, 'input', lambda x: '1'):
        assert user_interaction() == '1'
def test_file_interaction():
    pass

