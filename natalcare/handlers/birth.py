from __future__ import unicode_literals

from timelines.handlers.new import NewHandler


class BirthHandler(NewHandler):
    prefix = ''
    keyword = 'birth|bir'

    def parse_message(self, text):
        "Tokenize message text."
        result = {'keyword': 'birth'}  # FIXME: This must match timeline name
        tokens = text.strip().split()
        result['name'] = tokens.pop(0)
        if tokens:
            # Remaining tokens should be a date string
            result['date'] = ' '.join(tokens)
        return result
