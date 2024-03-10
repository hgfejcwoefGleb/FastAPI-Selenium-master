from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}


class Request(BaseModel):
    meta: dict
    request: dict
    session: dict
    version: str


class Response(BaseModel):
    response: dict
    session: dict
    version: str


@app.post("/alice_skill")
def alice_skill(request: Request):
    # Получение текста, введенного пользователем
    user_text = request.request["command"]

    # Формирование ответа
    response_text = f"Вы сказали: {user_text}"
    response = {
        "text": response_text,
        "end_session": False
    }

    # Формирование ответа для Яндекс.Алисы
    alice_response = Response(
        response=response,
        session=request.session,
        version=request.version
    )

    return alice_response


