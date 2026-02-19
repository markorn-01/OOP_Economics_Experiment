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

    #Section 4:
    #Q14: BNPL vs. implulse shopping
    def make_likert_1_5(label):
        return models.IntegerField(label=label, min=1, max=5)

    q14_1 = make_likert_1_5('Q14. Unplanned shopping is something … I do frequently.')
    q14_2 = make_likert_1_5('Q14. Unplanned shopping is something … I do automatically.')
    q14_3 = make_likert_1_5('Q14. Unplanned shopping is something … I do without having to consciously remember.')
    q14_4 = make_likert_1_5('Q14. Unplanned shopping is something … that makes me feel weird if I do not do it.')
    q14_5 = make_likert_1_5('Q14. Unplanned shopping is something … I do without thinking.')
    q14_6 = make_likert_1_5('Q14. Unplanned shopping is something … would require effort not to do it.')
    q14_7 = make_likert_1_5('Q14. Unplanned shopping is something … that belongs to my (daily, weekly, monthly) routine.')
    q14_8 = make_likert_1_5('Q14. Unplanned shopping is something … I start doing before I realize I’m doing it.')
    q14_9 = make_likert_1_5('Q14. Unplanned shopping is something … I would find hard not to do.')
    q14_10 = make_likert_1_5('Q14. Unplanned shopping is something … I have no need to think about doing.')

    # Q15: single choice
    bnpl_necessities = models.StringField(
        label='Q15: How would the availability of digital payment methods, especially Buy Now Pay Later for shopping necessities (e.g: PayPal and PayPal Pay in 4 in supermarkets) influence your decision to purchase?',
        choices=['Encourages more purchase', 'No effect', 'Less purchase'],
        widget=widgets.RadioSelect,
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
                   # 'provider',
                   # 'service_reason',
                   # 'is_abandoned',
                   # 'missed_bnpl',
                   # 'product_type',
                   # 'statement_rate']

class Habit(Page):
    form_model = 'player'
    form_fields = [
        'q14_1','q14_2','q14_3','q14_4','q14_5',
        'q14_6','q14_7','q14_8','q14_9','q14_10',
        'bnpl_necessities',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        q14_rows = [
            ('q14_1',  '… I do frequently.'),
            ('q14_2',  '… I do automatically.'),
            ('q14_3',  '… I do without having to consciously remember.'),
            ('q14_4',  '… that makes me feel weird if I do not do it.'),
            ('q14_5',  '… I do without thinking.'),
            ('q14_6',  '… would require effort not to do it.'),
            ('q14_7',  '… that belongs to my (daily, weekly, monthly) routine.'),
            ('q14_8',  '… I start doing before I realize I’m doing it.'),
            ('q14_9',  '… I would find hard not to do.'),
            ('q14_10', '… I have no need to think about doing.'),
        ]
        return dict(q14_rows=q14_rows)

class Results(Page):
    pass

class Test(Page):
    pass

page_sequence = [Introduction, Demographics, Payment, Habit, Test]
