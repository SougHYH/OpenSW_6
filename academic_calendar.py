from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks


@match_regex(r"!calender")
async def website(opsdroid, config, message):
    await message.respond(
        Blocks(
            [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "학사 일정 확인하기"},
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "전체 학사일정",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/262/subview.do",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "학사 공지",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/257/subview.do",
                        },
                    ],
                },
            ]
        )
    )
