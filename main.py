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
        response_string = subprocess.getoutput('yt-dlp --audio-format mp3 -f bestaudio --print "title:%(artist)s - %(title)s" --get-url {}'.format(url))
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

@app.get("/getytaudio")
async def getytaudio(url:str):
    try:
        response_string = subprocess.getoutput('yt-dlp --audio-format mp3 -f bestaudio --print "title:%(artist)s - %(title)s\n duration:%(duration)s\n thumbnail:%(thumbnail)s\n ytid:%(id)s" --get-url {}'.format(url))
        # duration * 1000
        response_info = response_string.split("\n")
        streaming_link = next((s for s in response_info if "https://rr" in s), None)
        title = next((s for s in response_info if "title:" in s), None) 
        title = re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-",title.replace("title:","").replace("NA - ",""))

        duration= next((s for s in response_info if "duration:" in s), None) 
        duration= int(duration.replace("duration:","")) * 1000 if duration else None

        thumbnail = next((s for s in response_info if "thumbnail:" in s), None)
        thumbnail = thumbnail.replace("thumbnail:","") if thumbnail else None


        ytid = next((s for s in response_info if "ytid:" in s), None)  
        ytid = ytid.replace("ytid:","") if ytid else None
        if not title or not streaming_link or not duration or not thumbnail or not ytid:
            return {"error":f"streaming_link:{streaming_link},title:{title},thumbnail:{thumbnail},duration:{duration},ytid:{ytid},duration:{duration}"}
        else:
            return {"streaming_url":streaming_link,"title":title,"thumbnail":thumbnail,"ytid":ytid,"duration_ms":duration}            
            # {"album_id": "1WVIJaAboRSwJOe4u0n0Q7", "album_name": "GABRIEL", "artist": "keshi", "artist_id": "3pc0bOVB5whxmD50W79wwO", "duration_ms": 128779, "id": "4RfjLV2FwnrxCjhCA3ZHf0", "name": "GABRIEL", "playlist_local": "true", "playlist_name": "New Amari Keshi", "thumbnail": "https://i.scdn.co/image/ab67616d0000b27319aff2da63b211d75341e8eb", "track_number": 12}
    except Exception as ex:
        return {"error":f"{type(ex)},{ex}"}   

if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
    #uvicorn.run()
    #asyncio.run(main())