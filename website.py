from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks

@match_regex(r'!web')
async def website(opsdroid, config, message):
    await message.respond(Blocks([
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Visit website",
                            "emoji": True
                        },
                        "url": "https://www.mju.ac.kr/sites/mjukr/intro/intro.html"
                    }
                ]
            }
        ]
    ))