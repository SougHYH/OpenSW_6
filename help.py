from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

command_list = ['MJU_BOT 에는 다음과 같은 명령을 사용 할 수 있습니다.\n',
                '!help  -- 명령어 도움말',
                '!intro -- 명지대 소개 및 연락처',
                '!web   -- 명지대 공식 웹사이트'
                '!map   -- 명지대 자연캠퍼스 지도'
                '!menu  -- 명지대 학식 메뉴']

@match_regex(r'!help')
async def help(opsdroid, config, message):
    command = ('\n'.join(command_list))
    await message.respond(command)