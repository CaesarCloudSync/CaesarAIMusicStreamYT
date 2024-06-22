import uvicorn

from typing import Dict,List,Any,Union
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import WebSocket,WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pytube import YouTube
import re
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get('/')# GET # allow all origins all methods.
async def index():
    return "Welcome to CaesarAIMusicStreamYT Template."
@app.get('/getaudio')# GET # allow all origins all methods.
async def getaudio(url:str):
    try:
        ytobj = YouTube(url)
        ytobj = ytobj.streams.filter(only_audio=True).filter(type="audio").first()
        title = re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-",ytobj.title)
        return {"streaming_url":ytobj.url,"title":title}
    except Exception as ex:
        return {"error":f"{type(ex)},{ex}"}




if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
    #uvicorn.run()
    #asyncio.run(main())