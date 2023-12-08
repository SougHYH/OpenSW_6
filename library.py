from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks


@match_regex(r"!library")
async def website(opsdroid, config, message):
    await message.respond(
        Blocks(
            [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "[자연캠퍼스 도서관]\n 자료열람 및 대출시간\n ☞ 학기 중: 월~금 08:40~18:30 \n ☞ 방학 중: 월~금 09:00~16:50 \n ☞ 일반열람실: 06:00~24:00(시험기간 24시간 개방)"},
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "도서 검색",
                                "emoji": True,
                            },
                            "url": "https://lib.mju.ac.kr/search/i-discovery",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "도서관 홈페이지",
                                "emoji": True,
                            },
                            "url": "https://lib.mju.ac.kr",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "도사관 열람실 이용안내",
                                "emoji": True,
                            },
                            "url": "https://lib.mju.ac.kr/guide/facility/smuf?tabIndex=20",
                        },
                    ],
                },
            ]
        )
    )