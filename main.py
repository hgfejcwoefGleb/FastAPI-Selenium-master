from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

"""class Msg(BaseModel):
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
"""

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
    response = {
  "response": {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
    "card": {
      "type": "...",
    },
    "buttons": [
        {
            "title": "Надпись на кнопке",
            "payload": {},
            "url": "https://example.com/",
            "hide": True
        }
    ],
    "end_session": False,
    "directives": {}
  },
  "session_state": {
      "value": 10
  },
  "user_state_update": {
      "value": 42
  },
  "application_state": {
      "value": 37
  },
  "analytics": {
        "events": [
            {
                "name": "custom event"
            },
            {
                "name": "another custom event",
                "value": {
                    "field": "some value",
                    "second field": {
                        "third field": "custom value"
                    }
                }
            }
        ]
    },
  "version": "1.0"
}
    return response


