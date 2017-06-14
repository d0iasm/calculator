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


    def readNagativeNumber(self, line, index):
        number, index = self.readNumber(line, index)
        return -number, index


    def isNagativeNumber(self, line, index):
        if line[index] == '-' and index == 0:
            return True
        elif line[index] == '-' and line[index-1] in '+×*÷/' and line[index+1].isdigit():
            return True
        else:
            return False


    def prioritize(self, current, stack):
        if current in '*×/÷' and stack in '*×/÷':
            return True
        elif current in '+-' and stack in '+-*×/÷':
            return True
        else:
            return False


    def tokenize(self, line):
        operators = []
        tokens = []
        index = 0
        while index < len(line):
            if line[index].isdigit():
                number, index = self.readNumber(line, index)
                tokens.append(number)
            elif line[index] == '(':
                operators.append(line[index])
                index += 1
            elif line[index] == ')':
                while operators[-1] != '(':
                    tokens.append(operators.pop())
                operators.pop()
                index += 1
            elif self.isNagativeNumber(line, index):
                number, index = self.readNagativeNumber(line, index+1)
                tokens.append(number)
            elif line[index] in "+-*×/÷":
                while operators:
                    if self.prioritize(line[index], operators[-1]):
                        tokens.append(operators.pop())
                    else: break
                operators.append(line[index])
                index += 1
        
        while operators:
            tokens.append(operators.pop())
        return tokens


    def evaluate(self, line):
        tokens = self.tokenize(line)
        stack = []
        print(tokens)
        operator = {
            '+': (lambda x, y: x + y),
            '-': (lambda x, y: x - y),
            '*': (lambda x, y: x * y),
            '×': (lambda x, y: x * y),
            '/': (lambda x, y: x / y),
            '÷': (lambda x, y: x / y)
        }
        for token in tokens:
            if token not in operator.keys():
                stack.append(token)
                continue
            y = stack.pop()
            x = stack.pop()
            stack.append(operator[token](x, y))
        return stack[0]


