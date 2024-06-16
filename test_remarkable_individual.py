from remarkable_individual import get_person_name

def test_get_person_name():
    """Does the program returns Olamide Adu when prompted"""
    name = get_person_name()
    assert name == "Olamide Adu"