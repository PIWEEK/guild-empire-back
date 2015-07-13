# coding: utf-8

# python
from random import randint, choice


#
# Action
#
DUMMY_ACTION = {
    'name': 'name',
    'slug': 'slug',
    'action_points': 1,
    'stuff': 'Not implemented.'
}


def get_actions():
    return [DUMMY_ACTION for x in range(0, randint(1, 10))]


#
# Place
#
DUMMY_PLACE = {
    'name': 'Name',
    'slug': 'slug',
    'actions': get_actions(),
}


def get_places():
    return [DUMMY_PLACE for x in range(0, randint(1, 5))]


#
# Members
#
DUMMY_CONDITION = {
    'name': 'Name',
    'slug': 'slug',
    'type': choice(
        ["positive", "negative", "permanent-positive",
         "permanent-negative", "status"]
    )
}

DUMMY_SKILL = {
    'name': 'Name',
    'slug': 'slug',
    'value': randint(1, 20),
    'modifier': randint(1, 6),
}

DUMMY_MEMBER = {
    'name': 'Name',
    'slug': 'slug',
    'archetype': 'thief',
    'conditions': [DUMMY_CONDITION for x in range(0, randint(0, 3))],
    'skills': [DUMMY_SKILL for x in range(0, randint(0, 6))]
}


def get_members():
    return [DUMMY_MEMBER for x in range(0, 10)]

#
# Guild
#
DUMMY_GUILD_INFO = {
    'gold': randint(10, 1234567),
    'influence': randint(10, 2345),
    'infamy': randint(10, 12345),
    'members': get_members(),
}

#
# Last turn
#
DUMMY_LAST_TURN_ITEM = {
    'character': 'slug',
    'guild_assets': {
        'gold': randint(-1000, 1000),
        'influence': randint(-1000, 1000),
        'infamy': randint(-1000, 1000)
    },
    'skills': [
        {
            'slug': 'slug',
            'variation': randint(-5, 5)
        } for x in range(0, randint(0, 3))
    ],
    'conditions_gained': [],
    'conditions_lost': [],
    'events': ['Lorem ipsum dolor sit amet']
}
DUMMY_LAST_TURN = [DUMMY_LAST_TURN_ITEM for x in range(0, 10)]

#
# Get method
#
DUMMY_GET = {
    'last_turn': DUMMY_LAST_TURN,
    'places':  get_places(),
    'free_actions': get_actions(),
    'guild': DUMMY_GUILD_INFO,
}
