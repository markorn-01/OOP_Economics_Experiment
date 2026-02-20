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
    
    # Optional
    # Q8.1:
    provider = models.StringField(
        label='Q8.1: Which BNPL provider do you use most frequently?',
        choices=['PayPal Pay in 4', 'Affirm', 'Klarna', 'After pay', 'Apple Pay Later', 'Other', 'None'],
        widget=widgets.RadioSelect
    )
    provider_other = models.LongStringField(blank=True, label='Please specify')

    # Q8.2:
    service_reason = models.LongStringField(
        label='Q8.2: Why do you use BNPL services? (Select all that apply)',
        blank=False,
    )

    # Q8.3:
    bnpl_impulse_products = models.LongStringField(
        label='Q8.3: What types of products do you typically buy impulsively using BNPL? (Select all that apply)',
        blank=True
    )
    
    # Q8.4:
    q8_4_expensive_bnpl = models.IntegerField(
        label='Q8.4: On a scale of 1–7 (1 = Strongly agree, 7 = Strongly disagree), rate the statement: '
              'The more expensive the good is, the more I tend to use BNPL options.',
        min=1,
        max=7,
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

    # Q13: Influence
    bnpl_influence = models.StringField(
        label="Q13: How does the availability of BNPL influence your decision to make a purchase now vs. later?",
        choices=[
            "Encourages immediate purchase",
            "No effect",
            "Delays purchase"
        ],
        widget=widgets.RadioSelect,)
    
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
      
class OptionalPayment(Page):
    form_model = 'player'
    form_fields = ['provider',
                   'provider_other',
                   'service_reason',
                   'bnpl_impulse_products',
                   'q8_4_expensive_bnpl']

    @staticmethod
    def is_displayed(player):
        return player.bnpl_frequency != 'Never'

    @staticmethod
    def error_message(player, values):
        if values.get('provider') == 'Other' and not values.get('provider_other'):
            return 'Please specify your "Other" BNPL provider.'
        if not values.get('service_reason'):
            return 'Please select at least one reason for Q8.2.'

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.provider != 'Other':
            player.provider_other = ''

class FunFact1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.bnpl_frequency != 'Never'

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
                   'q128',
                   'bnpl_influence']

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

class FunFact2(Page):
    pass

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

page_sequence = [Introduction, Demographics, Payment, OptionalPayment, FunFact1, Preference, FunFact2, Habit, Test]