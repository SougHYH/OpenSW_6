from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

class MapLinkSkill(Skill):
    @match_regex(r'!map')
    async def provide_map_link(self, message):
        map_url = 'https://www.mju.ac.kr/campusMap/mjukr/view.do?findType=B'
        await message.respond(f'캠퍼스 맵: {map_url}')