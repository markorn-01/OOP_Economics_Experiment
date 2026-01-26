from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'myapp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Get information of each player
    name = models.StringField(label='Your Name: ')
    age = models.IntegerField(label='Your Age: ', min=0, max=100)
    gender = models.StringField(label='Your Gender: ', choices=['Male', 'Female', 'Other', 'Prefer not to tell'])
    coin = models.BooleanField()
    prediction = models.BooleanField(label='Your Prediction: ',
                                     choices=[(True, 'Heads'),
                                              (False, 'Tails')],
                                     widget=widgets.RadioSelect)


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'gender']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        player.coin = random.choice([True, False])

class Coin(Page):
    form_model = 'player'
    form_fields = ['prediction']
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.prediction == player.coin:
            player.payoff += 1

class Results(Page):
    pass


page_sequence = [Demographics, Coin, Results]
