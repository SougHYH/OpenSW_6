from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks


class BlocksSkill(Skill):

    @match_regex(r"who are you\?")
    async def who_are_you(self, event):
        await event.respond(Blocks([
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "안녕하세요, 저는 MJUBOT 입니다."
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": "https://i.namu.wiki/i/_Wk24M8xsAnZkawadTDB5XPa7OXGkC3YOzlSlhqMzWBuuKodwViFBzv9lPFQEGzV8Ekv5B5-hzkkVYS6n3P7kw.svg",
                        "alt_text": "opsdroid logo"
                    }
                },
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