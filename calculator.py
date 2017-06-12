'''
[sample code]
(https://github.com/xharaken/step2015/blob/master/calculator_modularize_2.py)
'''

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
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readMultipy(line, index):
    token = {'type': 'MULTIPY'}
    return token, index + 1


def readDevide(line, index):
    token = {'type': 'DEVIDE'}
    return token, index + 1


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '×' or line[index] == '*':
            (token, index) = readMultipy(line, index)
        elif line[index] == '÷' or line[index] == '/':
            (token, index) = readDevide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTIPY':
            product = tokens[index - 1]['number'] * tokens[index + 1]['number']
            tokens[index] = {'type': 'NUMBER', 'number': product}
            del tokens[index - 1]
            del tokens[index]
        elif tokens[index]['type'] == 'DEVIDE':
            quotient = tokens[index - 1]['number'] / tokens[index + 1]['number']
            tokens[index] = {'type': 'NUMBER', 'number': quotient}
            del tokens[index - 1]
            del tokens[index]
        index += 1
    
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


def runTest():
    print("==== Test started! ====")
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("0", 0)
    test("-1.5-0.7", -2.2)
    test("2.5×2", 5)
    test("1+2.5*2", 6)
    test("0*5.0", 0)
    test("6÷3", 2)
    test("10-8/2", 6)
    test("-10/2", -5)
    test("0/5", 0)
    test("-2.5*2+10/2", 0)
    # マイナスの数値で掛け算、割り算する場合はカッコが必要になる
    #test("2.5*2/-5", 1)
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ')
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
