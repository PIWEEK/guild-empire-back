# coding: utf-8

# core
from games import game_runtime
from guilds import guild_runtime
from actions import action_defs


# == game ==
def serialize_game(game: game_runtime.Game) -> object:
    result = {}

    result['places'] = _serialize_game_places(game)
    result['guild'] = _serialize_guild(game)

    return result


# == Places and actions ==
def _serialize_action(action: action_defs.Action) -> object:
    result = {
        'slug': action.slug,
        'name': action.name,
        'action_points': action.action_points,
        'skills_needed': action.skills_needed,
        'skills_upgraded': action.skills_needed,
    }

    return result


def _serialize_game_places(game: game_runtime.Game) -> object:
    places = []

    for place in game.places:
        current = {
            'name': place.definition.name,
            'slug': place.definition.slug,
            'actions': [],
        }
        for action in place.definition.actions:
            current['actions'].append(_serialize_action(action))

        places.append(current)

    return places


# == Guild and members ==
def _serialize_assets(guild: guild_runtime.Guild) -> object:
    assets = []
    for asset in guild.assets:
        assets.append({
            'name': asset.name,
            'slug': asset.slug,
            'value': asset.value,
        })
    return assets


def _serialize_members(guild: guild_runtime.Guild) -> object:
    members = []
    for member in guild.members:
        current = {
            'name': member.name,
            'slug': member.slug,
            'archetype': member.archetype,
            'skills': [],
            'conditions': [],
        }

        for skill in member.skills:
            current['skills'].append({
                'name': skill.name,
                'slug': skill.slug,
                'value': skill.value,
                'modifier': skill.modifier,
            })

        for condition in member.conditions:
            current['conditions'].append({
                'name': condition.name,
                'slug': condition.slug,
                'type': condition.type,
                'description': condition.description,
            })

        members.append(current)
    return members


def _serialize_guild(game: game_runtime.Game) -> object:
    guild = game.guilds[0]  # TODO using first assuming player logged
    result = {
        'assets': _serialize_assets(guild),
        'members': _serialize_members(guild)
    }

    return result
