from remarkable_individual import get_person_name

pob = input("What's your place of birth? ")
dob = input("What's your date of birth? ")
pronoun = input("What's the pronoun of the person? ")
challenge = input("What challenge did they face? ")
talent = input("What particular skills or talent do they have?")

early_life_background = f"{get_person_name()} was born in {pob} on {dob}.\
 Growing up, {pronoun} faced numerous challenges, including {challenge}. Despite these difficulties, {pronoun} \
 demonstrated an early talent for {talent}, which became a cornerstone of {pronoun} identity."

print(early_life_background)