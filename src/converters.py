# coding: utf-8

# core
from games import game_runtime
from guilds import guild_runtime

# back
from dummy import DUMMY_LAST_TURN


# == game ==
def convert_game(game: game_runtime.Game, guild: guild_runtime.Guild) -> object:
    return {
        'pending': guild.slug in game.turns,
        'places': _convert_places(game),
        'guild': _convert_guild(guild),
        'free_actions': _convert_actions(game.definition.free_actions),
        'last_turn': DUMMY_LAST_TURN,
    }


# == Places and actions ==
def _convert_places(game: game_runtime.Game) -> object:
    places = [{
        'name': place.definition.name,
        'slug': place.definition.slug,
        'actions': _convert_actions(place.definition.actions),
    } for slug, place in game.places.items()]

    return places


def _convert_actions(actions) -> object:
    results = [{
        'slug': action.slug,
        'name': action.name,
        'action_points': action.action_points,
        'skills_needed': action.skills_needed,
        'skills_upgraded': action.skills_needed,
    } for action in actions]

    return results


# == Guild and members ==
def _convert_guild(guild: guild_runtime.Guild) -> object:
    return {
        'name': guild.name,
        'slug': guild.slug,
        'color': guild.color,
        'assets': _convert_assets(guild),
        'members': _convert_members(guild)
    }


def _convert_assets(guild: guild_runtime.Guild) -> object:
    assets = [{
        'name': asset.name,
        'slug': asset.slug,
        'value': asset.value,
    } for slug, asset in guild.assets.items()]

    return assets


def _convert_members(guild: guild_runtime.Guild) -> object:
    members = [{
        'name': member.name,
        'slug': member.slug,
        'archetype': member.archetype,
        'avatar_slug': member.avatar_slug,
        'skills': [{
            'name': skill.name,
            'slug': skill.slug,
            'value': skill.value,
            'modifier': skill.modifier,
        } for skill_slug, skill in member.skills.items()],
        'conditions': [{
            'name': condition.name,
            'slug': condition.slug,
            'type': condition.type,
            'description': condition.description,
        } for skill_condition, condition in member.conditions.items()],
    } for slug, member in guild.members.items()]

    return members


# == Turn ==
def turn_to_runtime(turns: list, game: game_runtime.Game, guild: guild_runtime.Guild) -> game_runtime.Turn:
    characters = {character['slug']: _convert_turn_characters(character) for character in turns}

    return game_runtime.Turn(
        guild=guild,
        characters=characters,
    )


def _convert_turn_characters(character_dict: dict) -> game_runtime.TurnCharacter:
    actions = [_convert_turn_character_action(action) for action in character_dict['actions']]

    return game_runtime.TurnCharacter(
        character=character_dict['slug'],
        actions=actions,
    )


def _convert_turn_character_action(action: list) -> game_runtime.TurnCharacterAction:
    return game_runtime.TurnCharacterAction(
        place=action['place'],
        action=action['action'],
        target=None
    )
