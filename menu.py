from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks


@match_regex(r"!menu")
async def website(opsdroid, config, message):
    await message.respond(
        Blocks(
            [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "*식당을 선택해주세요:*"},
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "명진당",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/485/subview.do",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "학생 회관",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/486/subview.do",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "생활관 식당",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/487/subview.do",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "교직원 식당",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/488/subview.do",
                        },
                    ],
                },
            ]
        )
    )
