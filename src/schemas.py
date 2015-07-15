# coding: utf-8

# Third party
from skame.exceptions import SchemaErrors
from skame.schemas import base as b
from skame.schemas.types import List
from skame.validator import validate


class RecursiveList(List):
    message = 'Turn must be a list of character actions'

    def __init__(self, item_schema, *args, **kwargs):
        super(RecursiveList, self).__init__(*args, **kwargs)
        self._item_schema = item_schema

    def validate(self, data):
        all_errors = []
        result = super(RecursiveList, self).validate(data)

        for item in data:
            data, errors = validate(self._item_schema, item)
            if errors:
                all_errors.append(errors)

        if all_errors:
            raise SchemaErrors(all_errors)

        return result


turn_character_actions_schema = b.schema({
    "place": b.Pipe(str, message="Place must be present"),
    "action": b.Pipe(str, message="Action must be present"),
    # Optional:
    # "target": b.Pipe(dict, message="Target must be present"),
})


turn_character_schema = b.schema({
    "slug": b.Pipe(str, message="Character slug must be present"),
    "actions": RecursiveList(turn_character_actions_schema),
})
