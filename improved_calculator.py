class Calculator(object):
    
    def readNumber(line, index):
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
        return token, index

    def evaluate(tokens):
        return answer


if __name__ == '__main__':
    calc = Calculator()
    print(calc.evaluate("1+2+3"))
