# coding: utf-8

# third party
from anillo.http import Ok, BadRequest, Created
from skame.exceptions import SchemaError, SchemaErrors

# core
from games.game_services import get_guild_from_game, new_game, submit_turn
from storage.methods import load_game, save_game

# guild empire back
from converters import convert_game, turn_to_runtime
from dummy import DUMMY_GET
from schemas import RecursiveList, turn_character_schema


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
    [
        {
            "slug": "character slug",
            "actions": [{
                "place": "place_slug",
                "action": "action_slug",
                "target": {
                    "guild": "guild_slug",
                    "character": "character_slug"
                }
            }]
        }
    ]
    ```
    """

    game_uuid = request.get_params.get('game', None)
    guild_slug = request.get_params.get('guild', None)

    # Validate the post schema
    try:
        schema = RecursiveList(turn_character_schema)
        schema.validate(request.body)

    except SchemaError as error:
        return BadRequest({
            "errors": error.error
        })
    except SchemaErrors as error:
        return BadRequest({
            "errors": error.errors
        })

    # Load game and guild runtime
    game = load_game(game_uuid)
    guild = get_guild_from_game(game, guild_slug)

    # Convert turn to runtime objects
    turn = turn_to_runtime(request.body, game, guild)

    # Submit turn to core
    updated_game = submit_turn(game, turn)

    # Convert new game data
    converted_updated_game = convert_game(updated_game, guild)

    return Created(converted_updated_game)
