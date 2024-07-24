import requests

response = requests.get("http://localhost:8080/getytaudio",params={"url":"https://www.youtube.com/watch?v=AHLFNoT64HQ&pp=ygUTZW5kbGVzcyBmcmFuayBvY2Vhbg%3D%3D"})
print(response.json())