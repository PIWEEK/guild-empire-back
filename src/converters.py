# coding: utf-8

# core
from games import game_runtime
from guilds import guild_runtime
from dummy import DUMMY_LAST_TURN


# == game ==
def convert_game(game: game_runtime.Game, guild: guild_runtime.Guild) -> object:
    result = {}

    result['places'] = _convert_places(game)
    result['guild'] = _convert_guild(guild)
    result['free_actions'] = _convert_actions(game.definition.free_actions)
    result['last_turn'] = DUMMY_LAST_TURN

    return result


# == Places and actions ==
def _convert_places(game: game_runtime.Game) -> object:
    places = []

    for place in game.places:
        current = {
            'name': place.definition.name,
            'slug': place.definition.slug,
            'actions': _convert_actions(place.definition.actions),
        }

        places.append(current)

    return places


def _convert_actions(actions) -> object:
    results = []

    for action in actions:
        current = {
            'slug': action.slug,
            'name': action.name,
            'action_points': action.action_points,
            'skills_needed': action.skills_needed,
            'skills_upgraded': action.skills_needed,
        }
        results.append(current)

    return results


# == Guild and members ==
def _convert_guild(guild: guild_runtime.Guild) -> object:
    result = {
        'assets': _convert_assets(guild),
        'members': _convert_members(guild)
    }

    return result


def _convert_assets(guild: guild_runtime.Guild) -> object:
    assets = []
    for asset in guild.assets:
        assets.append({
            'name': asset.name,
            'slug': asset.slug,
            'value': asset.value,
        })
    return assets


def _convert_members(guild: guild_runtime.Guild) -> object:
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
