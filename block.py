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
                        "text": "안녕하세요, 저는 MJUBOT 입니다.\n Your future Begins Here! MyongJi University \n 인문캠퍼스 : (03674) 서울특별시 서대문구 거북골로 34 \n 자연캠퍼스 : (17058) 경기도 용인시 처인구 명지로 116"
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAwKSDoiprrms_pHc1f9tAs_ReE2W-Kvp7aLWcs8MYQRXq8Ka-CfcBi_dIjWW89Tkx2Lc&usqp=CAU",
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