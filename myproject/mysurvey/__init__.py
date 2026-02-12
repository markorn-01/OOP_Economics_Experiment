from symtable import Class

from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'mysurvey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Q1: Age group
    age_group = models.StringField(
        label='Q1: What is your age group?',
        choices=['18–24', '25–40', '41–56', '57–65', '65+'],
        widget=widgets.RadioSelect
    )

    # Q2: Gender
    gender = models.StringField(
        label='Q2: What is your gender?',
        choices=['Male', 'Female', 'Non-binary/Other', 'Prefer not to say'],
        widget=widgets.RadioSelect
    )

    # Q3: Income (categorical ranges are better than integer)
    income = models.StringField(
        label='Q3: What is your annual household income?',
        choices=['<$30,000', '$30,000–$75,000', '>$75,000', 'Prefer not to say'],
        widget=widgets.RadioSelect
    )

    # Q4: Education
    education = models.StringField(
        label='Q4: What is your highest level of education?',
        choices=['High school or less', 'Some college', "Bachelor’s degree", 'Postgraduate', 'Other'],
        widget=widgets.RadioSelect
    )

    # Q5: Location
    location = models.StringField(
        label='Q5: Where do you live?',
        choices=['Urban', 'Suburban', 'Rural']
    )

# PAGES
class Introduction(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age_group', 'gender', 'income', 'education', 'location']

class Results(Page):
    pass

class Test(Page):
    pass

page_sequence = [Introduction, Demographics, Test]
