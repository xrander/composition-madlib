from helper_functions import *


def test_get_person_name():
    """Does the program returns Olamide Adu when prompted?"""
    name = get_person_name()
    assert name == "Olamide Adu"

def test_get_person_birthdate():
    """
    Does birthdate return in the format, Sunday, the 24th of November 1996?
    """
    birthdate = get_person_birthdate()
    assert birthdate == "Sunday, the 24th of November 1996."

def test_get_place_of_birth():
    """Is place of birth formatted like 'Lagos, Nigeria'"""
    pob = get_place_of_birth()
    assert pob == "Lagos, Nigeria"

def test_get_subjective_pronoun():
    """
    Does the subjective pronoun return any of he, she, they, ze, fae, xe,  and ve when prompted?
    """
    sub_pronoun = ["he", "she", "they", "ze", "fae", "xe", "ve"]
    pronoun = get_subjective_pronoun()
    assert pronoun in sub_pronoun

def test_get_objective_pronoun():
    """
    Does the objective pronoun return any of him, her, them, zir, xem, faer, and ver when prompted? 
    """
    obj_pronoun = ["him", "her", "them", "zir", "xem", "faer", "ver"]
    pronoun = get_objective_pronoun()
    assert pronoun in obj_pronoun

def test_get_possessive_pronoun():
    """
    Does the objective pronoun return any of his, hers, their, zirs, xyrs, faers, and vers when prompted? 
    """
    pos_pronoun = ["his", "hers", "their", "zirs", "xyrs", "faers", "vers"]
    pronoun = get_possessive_pronoun()
    assert pronoun in pos_pronoun

def test_get_challenge():
    """Does the challenge return to ADHD?"""
    chal = get_challenge()
    assert chal == "ADHD"

def test_get_talent():
    """Does the talent return to speed reading"""
    tal = get_talent()
    assert tal == "speed reading"

def test_get_achievements():
    """Does achievement return first-class honours"""
    achievement = get_achievement()
    assert achievement == "first-class honours"

def test_why_impressive():
    """Does why impressive returns 'he's from a poor background'"""
    impressive = get_why_impressive()
    assert impressive == "he's from a poor background"

def test_get_contribution_area():
    """Is the contribution area Akure South"""
    contrib_area = get_contribution_area()
    assert contrib_area == "Akure South community"

def test_describe_contribution():
    """Is the contribution made providing quality education?"""
    contrib = describe_contribution()
    assert contrib == "providing quality education"

def test_get_quality():
    """ Check that recipient have qualities such as kindness or determination"""
    qualities = get_quality()
    assert qualities == ["kindness, determination"]