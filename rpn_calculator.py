from enum import Enum


class Operator(Enum):
    PLUS = 0
    MINUS = 0
    MULTIPY = 1
    DEVIDE = 1
    BRACKET = 2


class Calculator(object):


    def readNumber(self, line, index):
        number = 0
        while index < len(line) and line[index].isdigit():
            number = number * 10 + int(line[index])
            index += 1
        if index < len(line) and line[index] == '.':
            index += 1
            keta = 0.1
            while index < len(line) and line[index].isdigit():
                number += int(line[index]) * keta
                keta *= 0.1
                index += 1
        return number, index


    def convert(self, line):
        operators = []
        tokens = []
        index = 0
        while index < len(line):
            if line[index].isdigit():
                token, index = self.readNumber(line, index)
                tokens.append(token)
            else:
                if line[index] == '+' or if line[index] == '-':
                    if '*' in operators or if '/' in operators:
                        # これだと一つのみしか演算子を追加できない
                        tokens.append(operators.pop)
                    operators.append(line[index])
                else:
                    operators.append(line[index])
                index += 1
        tokens.extend(operators)
        return tokens


    def evaluate(self, line):
        tokens = self.convert(line)
        answer = tokens
        return answer


if __name__ == '__main__':
    calc = Calculator()
    print("1.5+2*1")
    print(calc.evaluate("1.5+2*1"))
