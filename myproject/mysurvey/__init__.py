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

# Q11: Intertemporal choice rows
def make_time_choice():
    return models.IntegerField(choices=[[1, ""], [2, ""]], blank=False)

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

    # Section 3:
    # Q9: Purchase preference
    purchase_pref = models.StringField(
        label='Q9: When making purchases, do you prefer to:',
        choices=[ ('pay_now', 'Pay now to avoid future debt'),
                    ('spread_payment', 'Spread payments over time')]
    )

    # Q10: slider 1–7
    scale_pref = models.IntegerField(
        label='Q10: On a scale of 1–7, '
              'how would you rate your preference for spending now vs. saving for the future?',
        min=1,
        max=7,
    )

    # Q11: Week preference
    q111 = make_time_choice()
    q112 = make_time_choice()
    q113 = make_time_choice()
    q114 = make_time_choice()
    q115 = make_time_choice()
    q116 = make_time_choice()
    q117 = make_time_choice()
    q118 = make_time_choice()

    # Q12: Month preference
    q121 = make_time_choice()
    q122 = make_time_choice()
    q123 = make_time_choice()
    q124 = make_time_choice()
    q125 = make_time_choice()
    q126 = make_time_choice()
    q127 = make_time_choice()
    q128 = make_time_choice()

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

class Preference(Page):
    form_model = 'player'
    form_fields = ['purchase_pref',
                   'scale_pref',
                   'q111',
                   'q112',
                   'q113',
                   'q114',
                   'q115',
                   'q116',
                   'q117',
                   'q118',
                   'q121',
                   'q122',
                   'q123',
                   'q124',
                   'q125',
                   'q126',
                   'q127',
                   'q128']
                   # 'bnpl_influence']

    @staticmethod
    def vars_for_template(player: Player):
        rows11 = [
            ('q111', 1000, 1002),
            ('q112', 1000, 1004),
            ('q113', 1000, 1006),
            ('q114', 1000, 1010),
            ('q115', 1000, 1015),
            ('q116', 1000, 1022),
            ('q117', 1000, 1030),
            ('q118', 1000, 1040),
        ]

        rows12 = [
            ('q121', 1000, 1007),
            ('q122', 1000, 1014),
            ('q123', 1000, 1021),
            ('q124', 1000, 1035),
            ('q125', 1000, 1053),
            ('q126', 1000, 1079),
            ('q127', 1000, 1109),
            ('q128', 1000, 1147),
        ]

        return dict(q11_rows=rows11, q12_rows=rows12)


class Results(Page):
    pass

class Test(Page):
    pass

page_sequence = [Introduction, Demographics, Payment, Preference, Test]
