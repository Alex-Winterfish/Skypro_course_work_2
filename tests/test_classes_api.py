from src.classes_api import HeadHunterAPI


def test_init_hh_class():
    vacancy1 = HeadHunterAPI('vacancy', 'api')

    assert vacancy1