from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import sympy

class CalculatorSkill(Skill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculator_mode = False
        self.expression = ""

    @match_regex(r'calculator')
    async def calculator_mode_handler(self, message):
        self.calculator_mode = True
        await message.respond('Calculator mode activated. Enter a mathematical expression.')

    @match_regex(r'exit calculator')
    async def exit_calculator_handler(self, message):
        self.calculator_mode = False
        self.expression = ""
        await message.respond('Calculator mode deactivated.')

    @match_regex(r'\d+([+\-*/]\d+)+')
    async def calculate_handler(self, message):
        if self.calculator_mode:
            expression = message.regex.group(0)
            result = sympy.sympify(expression)
            await message.respond(f'Result: {result}')
        else:
            await message.respond('Calculator mode not activated. Type "calculator" to activate.')

    async def default_handler(self, message):
        if self.calculator_mode:
            self.expression += message.text
            await message.respond(f'Expression: {self.expression}')