def get_person_name():
    """Collect person name"""
    person_name = input("What's the name of that remarkable person in your life? ")
    name = person_name
    return name.title()

name_of_person = get_person_name()

remarkable_individual = f"There are people in our lives who leave a lasting impact on us,\
 shaping our perspectives and influencing our paths. One such individual is {name_of_person}\
. {name_of_person} is a remarkable person whose qualities \
and actions have had a profound influence on my life."

print(remarkable_individual)