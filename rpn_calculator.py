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


    def prioritize(self, current, stack):
        if current in '*/' and stack in '*/':
            return True
        elif current in '+-' and stack in '+-*/':
            return True
        else:
            return False


    def tokenize(self, line):
        operators = []
        tokens = []
        index = 0
        while index < len(line):
            if line[index].isdigit():
                token, index = self.readNumber(line, index)
                tokens.append(token)
            else:
                if line[index] == '(':
                    operators.append(line[index])
                elif line[index] == ')':
                    while operators[-1] != '(':
                        tokens.append(operators.pop())
                    operators.pop()
                elif line[index] in "+-*×/÷":
                    while operators:
                        if self.prioritize(line[index], operators[-1]):
                            tokens.append(operators.pop())
                        else:
                            break
                    operators.append(line[index])
                index += 1
        while operators:
            tokens.append(operators.pop())
        return tokens


    def evaluate(self, line):
        tokens = self.tokenize(line)
        answer = tokens
        return answer


if __name__ == '__main__':
    calc = Calculator()
    print("(1+2) * (3+4)")
    print(calc.evaluate("(1+2) * (3+4)"))
    print("1.5+2*1-3")
    print(calc.evaluate("1.5+2*1-3"))
