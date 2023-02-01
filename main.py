def checkBrackets(expression):
    if len(expression) == 0 or len(expression) % 2 != 0 or expression[0] in (')}]'):
        return False
    data = []
    data += expression

    i = 0
    while i < len(data) - 1:
        if i >= 0 and (data[i] == '(' and data[i + 1] == ')'
                       or data[i] == '[' and data[i + 1] == ']' or data[i] == '{' and data[i + 1] == '}'):
            data.pop(i + 1)
            data.pop(i)
            i -= 2
        i += 1

    if len(data) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    data = input()
    print(checkBrackets(data))
