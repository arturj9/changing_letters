from fastapi import FastAPI
from . import efeitos

app = FastAPI()

@app.post('/efeitos')
def main(efeito,text):
    if efeito == 'AAA':
        return efeitos.AAA(text)
    elif efeito == 'aaa':
        return efeitos.aaa(text)
    elif efeito == 'Aaa':
        return efeitos.Aaa(text)
    elif efeito == 'aAA':
        return efeitos.aAA(text)
    elif efeito == 'a_b':
        return efeitos.a_b(text)
    elif efeito == 'abb':
        return efeitos.abb(text)
    else:
        return 0