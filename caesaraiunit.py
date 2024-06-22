import json
import requests
import unittest
import sys

uri = "http://127.0.0.1:8080" #"https://blacktechdivisionreward-hrjw5cc7pa-uc.a.run.app"

class CaesarAIUnittest(unittest.TestCase):
    def test_get_audio(self):
        response = requests.get(f"{uri}/getaudio",params={"url":"https://www.youtube.com/watch?v=sSudJNPsxAc"})
        print(response.json())

if __name__ == "__main__":
    unittest.main()