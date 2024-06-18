from helper_functions import *

person_name = get_person_name()
pob = get_place_of_birth()
birthdate = get_person_birthdate()
sp = get_subjective_pronoun()
pp = get_possessive_pronoun()
challenge = get_challenge()
talent = get_talent()
achievement = get_achievement()
wi = get_why_impressive()
community = get_contribution_area()
contribution = describe_contribution()
quality = get_quality()

remarkable = f"There are people in our lives who leave a lasting impact on us, shaping our perspectives and influencing our paths.\
 One such individual is {person_name}. {person_name} is a remarkable person whose qualities and\
 actions have had a profound influence on my life."

early_life = f"\t{person_name} was born in {pob} on {birthdate}.\
 Growing up, {sp} faced numerous challenges, including {challenge}. Despite these difficulties,\
 {sp} demonstrated an early talent for {talent}, which became a cornerstone of {pp} identity."

achievements = f"\tAs {person_name} grew older, {sp} achieved many significant milestones.\
     One of the most notable accomplishments was {achievement}. This accomplishment was particularly impressive because {wi}.\n \
     \tIn addition to personal achievements,{person_name} has made substantial contributions to {community}.\
    For example, {contribution}. This effort has had a significant impact on , benefiting many people in the process."

qualities = f"\tWhat truly sets {person_name} apart are {pp} personal qualities. {sp} is known for {quality[0]}\
 Another remarkable characteristic of {person_name} is {quality[1]}."

print(f"A remarkable individual\n\
      {remarkable}\nEarly Life and Background \n{early_life} \
      \nAchievements and Contributions \n{achievements}\
      ")