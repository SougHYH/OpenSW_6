from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import sympy

class CalculatorSkill(Skill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculator_mode = False
        self.expression = ""

    @match_regex(r'!calculator')
    async def calculator_mode_handler(self, message):
        self.calculator_mode = True
        await message.respond('계산기 모드가 활성화되었습니다. 계산할 수식을 입력해주세요.')

    @match_regex(r'!exit calculator')
    async def exit_calculator_handler(self, message):
        self.calculator_mode = False
        self.expression = ""
        await message.respond('계산기 모드가 비활성화되었습니다.')

    @match_regex(r'\d+([+\-*/]\d+)+')
    async def calculate_handler(self, message):
        if self.calculator_mode:
            expression = message.regex.group(0)
            result = sympy.sympify(expression)
            await message.respond(f'결과: {result}')
        else:
            await message.respond('계산기 모드가 활성화 되어 있지 않습니다. 계산기 모드를 활성화해주세요.')

    async def default_handler(self, message):
        if self.calculator_mode:
            self.expression += message.text
            await message.respond(f'Expression: {self.expression}')