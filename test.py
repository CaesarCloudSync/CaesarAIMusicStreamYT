import requests

response = requests.get("http://localhost:8080/getytaudio",params={"url":"https://www.youtube.com/watch?v=AHLFNoT64HQ"})
print(response.json())