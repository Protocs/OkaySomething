import re

from yaml import YAMLObject

from okayenglish.scenariomachine.states import create_dynamic_next_state_function


class Choice(YAMLObject):
    yaml_tag = "!Choice"

    def __init__(self, match, next, hint=None, prepend_next_text=()):
        self.hint = hint
        self.match = match
        self.next = create_dynamic_next_state_function(next)
        self.prepend_next_text = prepend_next_text
        if isinstance(prepend_next_text, str):
            self.prepend_next_text = (prepend_next_text,)

    def fits_under(self, response):
        """
        Возвращает ``True``,
        если ``response`` подходит под этот вариант,
        иначе ``False``.
        """
        return re.match(self.match, response) is not None
