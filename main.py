import re

import uvicorn
import subprocess
from fastapi import FastAPI
from typing import Dict,List,Any,Union
from fastapi.responses import StreamingResponse
from fastapi import WebSocket,WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware


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
        response_string = subprocess.getoutput('yt-dlp --audio-format mp3 --print "title:%(artist)s - %(title)s" --get-url {}'.format(url))
        response_info = response_string.split("\n")
        streaming_link = next((s for s in response_info if "https://rr" in s), None)
        title = next((s for s in response_info if "title:" in s), None) 
        if not title or not streaming_link:
            return {"error":f"streaming_link:{streaming_link},title:{title}"}
        else:
            title = re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-",title.replace("title:","").replace("NA - ",""))
            return {"streaming_url":streaming_link,"title":title}
    except Exception as ex:
        return {"error":f"{type(ex)},{ex}"}




if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
    #uvicorn.run()
    #asyncio.run(main())