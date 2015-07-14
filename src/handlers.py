# coding: utf-8

# third party
from anillo.http import Ok, NotImplemented

# core
from games.game_services import get_guild_from_game, new_game
from storage.methods import load_game, save_game

# guild empire back
from dummy import DUMMY_GET
from converters import convert_game


def create_game(request):
    game_type = 'default'
    game = new_game(game_type)
    save_game(game)
    return Ok({
        'game': game.uuid,
        'guilds': [g.slug for g in game.guilds],
    })


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
    """
    Expected data:
    ```
    [{
        "slug": "character slug",
        "actions": [{
            "place": "place_slug",
            "action": "action_slug",
            "target": {
                "guild": "guild_slug",
                "character": "character_slug"
            }
        }]
    }]
    ```
    """
    game = request.get_params.get('game', None)
    guild_slug = request.get_params.get('guild', None)

    return Ok({"you_sent": request.body})
