def solution(inputString):
    inputString = inputString.replace(' ', '').lower()
    if inputString[::] == inputString[::-1]:
        return True
    else:
        return False