from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

class ClassroomSkill(Skill):
    BUILDING_NAMES = {
        '': '제1공학관',
        '2': '창조예술관',
        '3': '명진당',
        '5': '제5공학관',
        '6': '예체능관',
        '7': '체육관',
        '8': '제2공학관',
        '9': '함박관',
        '12': '디자인조형관',
        '13': '제4공학관',
        '19': '제3공학과',
        '21': '학생복지관',
        '22': '채플관',
        '23': '차세대과학관'
    }

    @match_regex(r'!room')
    async def request_classroom_info(self, message):
        await message.respond("강의실을 입력해주세요.(입력형식: Y0000)")

    @match_regex(r'Y(\d{0,2})(\d{1})(\d{2})')
    async def provide_classroom_info(self, message):
        match = message.regex.groups()

        if match:
            building_number = match[0]
            floor_number = match[1]
            classroom_number = match[2]

            building_name = self.BUILDING_NAMES.get(building_number)

            if building_name:
                floor_description = f"지하 {max(int(floor_number), 1)}층" if floor_number == '0' else f"{floor_number}층"
                response = f"건물 이름: {building_name}, 건물 층수: {floor_description}, 강의실 번호: {classroom_number}"
            else:
                response = "알 수 없는 강의실입니다."
        else:
            response = "잘못된 입력입니다."

        await message.respond(response)
