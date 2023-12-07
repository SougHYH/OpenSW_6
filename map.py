from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks

@match_regex(r'!map')
async def website(opsdroid, config, message):
    await message.respond(Blocks([
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "campus map",
                            "emoji": True
                        },
                        "url": "https://www.mju.ac.kr/campusMap/mjukr/view.do?findType=B"
                    }
                ]
            }
        ]
    ))