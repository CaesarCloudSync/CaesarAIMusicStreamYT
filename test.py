import requests

response = requests.get("http://localhost:8080/getytaudio",params={"url":"https://www.youtube.com/watch?v=_7FBQVsT4fk"})
print(response.json())