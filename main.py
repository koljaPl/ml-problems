from typing import List

class Solution:

    @staticmethod
    def split_special_blocks(s: str) -> list[str]:
        blocks = []
        current = ''
        balance = 0

        for num in s:
            blocks += num

            if num == '1':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                blocks.append(current)
                sub_string = ""

        return blocks

    def maximize_blocks(self, blocks: list[str]) -> list[str]:
        result = []

        for block in blocks:
            inner = block[1:-1]
            inner_blocks = self.split_special_blocks(inner)
            inner = ''.join(self.maximize_blocks(inner_blocks))
            result.append(f'1{inner}0')

        result.sort(reverse=True)
        return result


    def makeLargestSpecial(self, s: str) -> str:
        return ''.join(
            self.maximize_blocks(
                self.split_special_blocks(s)
            )
        )