from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.connector.slack.events import Blocks


@match_regex(r"!bus")
async def bus(opsdroid, config, message):
    await message.respond(
        Blocks(
            [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "셔틀버스 정보 확인하기"},
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "자연켐퍼스 셔틀버스 안내",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/506/subview.do",
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "셔틀 운행 공지",
                                "emoji": True,
                            },
                            "url": "https://www.mju.ac.kr/mjukr/255/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbWp1a3IlMkYxNDElMkZhcnRjbExpc3QuZG8lM0ZiYnNDbFNlcSUzRCUyNmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZpc1ZpZXclM0R0cnVlJTI2c3JjaENvbHVtbiUzRHNqJTI2c3JjaFdyZCUzRCVFQyU4NSU5NCVFRCU4QiU4MCUyNg%3D%3D",
                        },
                    ],
                },
            ]
        )
    )
