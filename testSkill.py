from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

class nice(Skill):
    @match_regex(r'nice')
    async def hello(self, message):
        await message.respond('nice')