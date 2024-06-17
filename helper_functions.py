import calendar
from datetime import datetime

# Get User name
def get_person_name():
    """Collect person name"""
    person_name = input("What's the name of that remarkable person in your life? ")
    name = person_name
    return name.title()

# Get Their birthdate

def get_person_birthdate():
    """Collect person date of birth and give a return it well formatted"""
    birthdate_str = input("Enter the birthdate of the person (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        day_of_week = birthdate.strftime("%A")
        day_of_month = birthdate.day
        # Include suffix of each day
        if 4 <= day_of_month <= 20 or 24 <= day_of_month <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd", "th"][day_of_month % 10 - 1]
        month = birthdate.strftime("%B")
        year = birthdate.year
        birthdate_formatted = f"{day_of_week}, the {day_of_month}{suffix} of {month} {year}."
        return birthdate_formatted
    
    except ValueError:
        # Handle the error if the input format is incorrect
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


def get_place_of_birth():
    """Collect person place of birth well formatted."""
    country = input("What is the person country of birth? ")
    town = input("What is the person's birth town? ")

    pob = f"{town.title()}, {country.title()}"
    return pob

subject_pronoun = ["he", "she", "they", "ze", "fae", "xe", "ve"]
object_pronoun = ["him", "her", "them", "zir", "xem", "faer", "ver"]
possess_pronoun = ["his", "hers", "their", "zirs", "xyrs", "faers", "vers"]

def get_subjective_pronoun():
    """Collect the subjective pronoun of the person"""
    pronoun = input("What is the person's subjective pronoun in: he, she, they, ze, fae, xe,  and ve? ")
    if pronoun in subject_pronoun:
        return pronoun
    else:
        print("Invalid pronoun. Please select one of the following: he, she, they ze, fae, xe, and ve.")
        return None
    
def get_objective_pronoun():
    """Collect the objective pronoun of the person"""
    pronoun = input("What is the person's objective pronoun in: him, her, them, zir, xem, faer, and ver? ")
    if pronoun in object_pronoun:
        return pronoun
    else:
        print("Invalid pronoun. Please select one of the following: him, her, them, zir, xem, faer, and ver")
        return None

def get_possessive_pronoun():
    """Collect the possessive pronoun of the person"""
    pronoun = input("What is the person's possessive pronoun in: his, hers, their, zirs, xyrs, faers, vers? ")
    if pronoun in possess_pronoun:
        return pronoun.lower()
    else:
        print("Invalid pronoun. Please select one of the following: his, hers, their, zirs, xyrs, faers, vers")
        return None

def get_challenge():
    """Return the challenge/challenges the person faced in a well formatted"""
    challenge = input("What challenge did they face? ")
    return challenge


def get_talent():
    """Return the talent/talents the person have"""
    talent = input("What particular skills or talent do they have? ")
    return talent.lower()

def get_achievement():
    """Return the achievements the person have."""
    achievement = input("Describe a major achievement.")
    return achievement.lower()

def get_why_impressive():
    """Return why the achievement was impressive"""
    impressive = input("Explain why the achievement was impressive or challenging. ")
    return impressive.lower()

def get_contribution_area():
    """Return the community the person made a contribution to."""
    community = input("What community has the person made a contribution to? ")
    contribution = f" {community.title()} community"
    return contribution

def describe_contribution():
    """Describe the contribution the perosn made to their community."""
    contribution = input("Give an example of the contribution the person made to their community? ")
    return contribution.lower()

def get_quality():
    """Return one quality of the person."""
    qualities = []
    while True:      
        prompt = "give more than one quality such as kindness, determination, intelligence, etc. "
        prompt += "\n Enter 'quit' anytime when you are done. "
        quality = input(prompt)
        if quality.lower() == "quit":
                break
        else:
            try:             
                if len(quality) > 1:
                    qualities.append(quality.lower())
                else:
                    print("Please enter more than one qualities")
            except Exception as e:
                print(f"You need to input more than one qualities")
    return qualities

