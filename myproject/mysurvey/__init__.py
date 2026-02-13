from symtable import Class

from charset_normalizer import models
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
    # Section 1:
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

    # Section 2:
    # Q6: Payment methods
    payment_methods = models.LongStringField(
        label='Q6: Which digital payment methods have you used in the past 12 months? (Select all that apply)',
        blank=True)

    # Q7: Factors
    factor_ranking = models.LongStringField(
        label='Q7: What factors influence your choice of payment method at checkout? (Drag options to rank 1–5)',
        blank=False
    )

    # Q8: Frequency
    bnpl_frequency = models.StringField(
        label='Q8: How often do you use BNPL services (e.g., PayPal Pay in 4, Affirm, Klarna)?',
        choices=['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        widget=widgets.RadioSelectHorizontal
    )

    # Optional
    # Q8.1:
    provider = models.StringField(
        label='Q8.1: Which BNPL provider do you use most frequently?',
        choices=['PayPal Pay in 4', 'Affirm', 'Klarna', 'After pay', 'Apple Pay Later', 'Other', 'None'],
        widget=widgets.RadioSelect
    )

# PAGES
class Introduction(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age_group', 'gender', 'income', 'education', 'location']

class Payment(Page):
    form_model = 'player'
    form_fields = ['payment_methods',
                   'factor_ranking',
                   'bnpl_frequency']

class OptionalPayment(Page):
    form_model = 'player'
    form_fields = ['provider']
                   # 'service_reason',
                   # 'is_abandoned',
                   # 'missed_bnpl',
                   # 'product_type',
                   # 'statement_rate']

    @staticmethod
    def is_displayed(player):
        return player.bnpl_frequency != 'Never'


class Results(Page):
    pass

class Test(Page):
    pass

page_sequence = [Introduction, Demographics, Payment, OptionalPayment, Test]
