# coding: utf-8

# third party
from anillo.http import Ok, NotImplemented

# core
from games.game_services import get_guild_from_game
from storage.methods import load_game

# guild empire back
from dummy import DUMMY_GET
from converters import convert_game


def get_turn(request):
    game = request.get_params.get('game', None)
    guild_slug = request.get_params.get('guild', None)

    # Dummy data for development
    if not game:
        return Ok(DUMMY_GET)

    game_object = load_game(game)

    guild = get_guild_from_game(game_object, guild_slug)
    converted_game = convert_game(game_object, guild)

    return Ok(converted_game)


def post_turn(request):
    return NotImplemented()
