# coding: utf-8

# third party
from anillo.http import Ok, NotImplemented

# core
from storage.methods import load_game

# guild empire back
from dummy import DUMMY_GET
from serializers import serialize_game


def get_turn(request):
    game = request.get_params.get('game', None)

    if not game:
        return Ok(DUMMY_GET)

    game_object = load_game(game)

    serialized_game = serialize_game(game_object)

    return Ok(serialized_game)


def post_turn(request):
    return NotImplemented()
