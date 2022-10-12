def AAA(text):
    return text.upper()

def aaa(text):
    return text.lower()

def Aaa(text):
    newText = ''
    cont = 1
    for letra in text:
        if cont == 1:
            newText += letra.upper()
            cont = 0
        else:
            newText += letra.lower()

        if letra == ' ':
            cont = 1

    return newText

def aAA(text):
    newText = ''
    cont = 1
    for letra in text:
        if cont == 1:
            newText += letra.lower()
            cont = 0
        else:
            newText += letra.upper()

        if letra == ' ':
            cont = 1

    return newText

def a_b(text):
    newText = ''
    for letra in text:
        if letra == ' ':
            newText += ''
        else:
            newText += f'{letra} '
    
    newText = newText[:-1]

    return newText

def abb(text):
    newText = ''
    for letra in text:
        if letra == ' ':
            continue
        else:
            newText += letra

    return newText
