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

    # Q12: Month preference
    q121 = make_time_choice()
    q122 = make_time_choice()
    q123 = make_time_choice()
    q124 = make_time_choice()
    q125 = make_time_choice()

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

class Preference(Page):
    form_model = 'player'
    form_fields = ['purchase_pref',
                   'scale_pref',
                   'q111',
                   'q112',
                   'q113',
                   'q114',
                   'q115',
                   'q121',
                   'q122',
                   'q123',
                   'q124',
                   'q125',
                   'bnpl_influence']

    rows11 = [
        ('q111', 1000, 1002),
        ('q112', 1000, 1004),
        ('q113', 1000, 1009),
        ('q114', 1000, 1015),
        ('q115', 1000, 1022),
    ]

    rows12 = [
        ('q121', 1000, 1007),
        ('q122', 1000, 1014),
        ('q123', 1000, 1021),
        ('q124', 1000, 1035),
        ('q125', 1000, 1053),
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(q11_rows=Preference.rows11,
                    q12_rows=Preference.rows12)

class Habit(Page):
    form_model = 'player'
    form_fields = [
        'q14_1','q14_2','q14_3','q14_4','q14_5',
        'q14_6','q14_7','q14_8','q14_9','q14_10',
        'bnpl_necessities',
    ]

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

    @staticmethod
    def vars_for_template(player: Player):
        return dict(q14_rows=Habit.q14_rows)

class Insights(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):

        # Init a dictionary to collect facts
        dict = {}

        # FACT 1: Calculate the percentage based on selected age group and frequency of using BNPL
        # Create a base for age group and frequency 2D-array
        age_freq_base = {
            "18–24": {"Yes": 20, "No": 2},
            "25–40": {"Yes": 15, "No": 5},
            "41–56": {"Yes": 10, "No": 20},
            "57–65": {"Yes": 2, "No": 30},
            "65+": {"Yes": 1, "No": 20}
        }

        # Collect the value of age_group from the player
        selected_age = player.age_group

        # For q8 if player chose 'Never' then it would be classified as 'No', otherwise 'Yes'
        frequency = 'No' if player.bnpl_frequency == 'Never' else 'Yes'

        # Add this player to the number of people from the same age group and frequency
        age_freq_base[selected_age][frequency] += 1

        # Sum up and calculate percentage
        total_age = sum(age_freq_base[selected_age].values())
        percentage = round(age_freq_base[selected_age][frequency] / total_age * 100, 2)

        # Add percentage to dict
        dict["percentage"] = percentage

        # FACT 2.1: Show the most popular factor in q7
        # Create base for factors
        factor_base = {
            "Convenience": 8,
            "Security": 8,
            "Trust in provider": 8,
            "Cost": 8,
            "Speed": 8
        }

        # Get the first ranked factor of player
        player_first_factor = player.factor_ranking.split(' | ')[0]

        # Add the first ranked factor of player to the base
        factor_base[player_first_factor] += 1

        # Get the most first-ranked factor
        max_value = max(factor_base.values())

        top_factors = [
            key for key, value in factor_base.items()
            if value == max_value
        ]

        if len(top_factors) == 1:
            first_factors = top_factors[0]
        elif len(top_factors) == 2:
            first_factors = " and ".join(top_factors)
        else:
            first_factors = ", ".join(top_factors[:-1]) + " and " + top_factors[-1]

        # Add the most popular factor to dict
        dict["first_factors"] = first_factors
        dict["num_factors"] = len(top_factors)

        # FACT 2.2: Show the most popular provider in q8.1
        # Create base for providers
        provider_base = {
            "PayPal Pay in 4": 8,
            "Affirm": 8,
            "Klarna": 8,
            "After pay": 8,
            "Apple Pay Later": 8
        }
        if frequency == 'Yes':

            # Get the chosen provider of player
            player_most_provider = player.provider

            # If player did not choose "Other" nor "None", add the chosen provider of player to the base
            if player_most_provider not in ["Other", "None"]:
                provider_base[player_most_provider] += 1

        # Get the most chosen provider
        max_value = max(provider_base.values())

        top_providers = [
            key for key, value in provider_base.items()
            if value == max_value
        ]

        if len(top_providers) == 1:
            most_providers = top_providers[0]
        elif len(top_providers) == 2:
            most_providers = " and ".join(top_providers)
        else:
            most_providers = ", ".join(top_providers[:-1]) + " and " + top_providers[-1]

        # Add the most popular provider to dict
        dict["most_providers"] = most_providers
        dict["num_providers"] = len(top_providers)

        # FACT 3:
        # Calculate the turning numbers for q11 and q12
        # Create a list of questions
        question_11_list = [player.q111, player.q112, player.q113, player.q114, player.q115]
        idx_11 = len(question_11_list)-1

        # Create a base turning amount
        past_turn_amount = [1000, 1004, 1000, 1009, 1022]
        len_turn_amount = len(past_turn_amount)
        sum_turn_amount = sum(past_turn_amount)


        # Find the turning point if it is valid
        for q in range(1, len(question_11_list)):
            if question_11_list[q] != question_11_list[q-1]:
                if question_11_list[q-1] == 1:
                    idx_11 = q
                else:
                    idx_11 = -1
                break

        # Check if the question was answered rationally
        if idx_11 != -1:
            for q in range(idx_11, len(question_11_list)-1):
                if question_11_list[q] != question_11_list[q+1]:
                    idx_11 = -1
                    break

            # If after turning point it is still a valid answer, then collect it.
            if idx_11 != -1:
                rows11 = Preference.rows11
                _, left_amt, right_amt = rows11[idx_11]

                choice_val = question_11_list[idx_11]  # 1 or 2
                chosen_amt = left_amt if choice_val == 1 else right_amt
                sum_turn_amount += chosen_amt
                len_turn_amount += 1

        dict["turn_amount_q11_ave"] = round(sum_turn_amount / len_turn_amount, 2)


        # Q12
        question_12_list = [player.q121, player.q122, player.q123, player.q124, player.q125]
        idx_12 = len(question_12_list) - 1

        # Create a base turning amount
        past_turn_amount_12 = [1007, 1021, 1000, 1053, 1014]
        len_turn_amount_12 = len(past_turn_amount_12)
        sum_turn_amount_12 = sum(past_turn_amount_12)

        # Find the turning point if it is valid
        for q in range(1, len(question_12_list)):
            if question_12_list[q] != question_12_list[q - 1]:
                if question_12_list[q - 1] == 1:
                    idx_12 = q
                else:
                    idx_12 = -1
                break

        # Check if the question was answered rationally
        if idx_12 != -1:
            for q in range(idx_12, len(question_12_list) - 1):
                if question_12_list[q] != question_12_list[q + 1]:
                    idx_12 = -1
                    break

            # If after turning point it is still a valid answer, then collect it.
            if idx_12 != -1:
                rows12 = Preference.rows12
                _, left_amt, right_amt = rows12[idx_12]

                choice_val = question_12_list[idx_12]  # 1 or 2
                chosen_amt = left_amt if choice_val == 1 else right_amt
                sum_turn_amount_12 += chosen_amt
                len_turn_amount_12 += 1
        dict["turn_amount_q12_ave"] = round(sum_turn_amount_12 / len_turn_amount_12, 2)

        # FACT 4: Indications from unplanned shopping score
        question_14_list = [player.q14_1, player.q14_2,
                            player.q14_3, player.q14_4,
                            player.q14_5, player.q14_6,
                            player.q14_7, player.q14_8,
                            player.q14_9, player.q14_10]
        q14_ave = round(sum(question_14_list) / len(question_14_list),2)
        dict['q14_ave'] = q14_ave
        if q14_ave <= 2.4:
            q14_text = (
                "➜ Your unplanned shopping is usually deliberate rather than automatic.<br> "
                "➜ You tend to think before buying, so impulses are less likely to drive your choices."
            )
        elif q14_ave <= 3.4:
            q14_text = (
                "➜ You sometimes buy impulsively, especially in certain situations.<br> "
                "➜ Impulses may influence you occasionally, but the behavior is not consistently automatic."
            )
        else:
            q14_text = (
                "➜ Unplanned shopping may be a strong habit for you.<br> "
                "➜ It can happen automatically with little deliberation, suggesting a more routine pattern."
            )

        dict["q14_text"] = q14_text
        return dict

class Results(Page):
    pass

class Test(Page):
    pass

page_sequence = [Introduction, Demographics, Payment, OptionalPayment, Preference, Habit, Insights, Test]