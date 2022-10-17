from fastapi import FastAPI
import efeitos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/efeitos')
def main(efeito:str,text:str):
    if efeito == 'AAA':
        return {'status':1,'text':efeitos.AAA(text)}
    elif efeito == 'aaa':
        return {'status':1,'text':efeitos.aaa(text)}
    elif efeito == 'Aaa':
        return {'status':1,'text':efeitos.Aaa(text)}
    elif efeito == 'aAA':
        return {'status':1,'text':efeitos.aAA(text)}
    elif efeito == 'a_b':
        return {'status':1,'text':efeitos.a_b(text)}
    elif efeito == 'abb':
        return {'status':1,'text':efeitos.abb(text)}
    else:
        return {'status':0}