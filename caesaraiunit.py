import json
import requests
import unittest
import sys

base_url = "https://hub.caesaraihub.org" 


class CaesarAIUnittest(unittest.TestCase):
    def test_get_audio(self):
        response = requests.get(f"{base_url}/caesaraimusicstreamyt/8080/getaudio",params={"url":"https://www.youtube.com/watch?v=sSudJNPsxAc"})
        print(response.json())

if __name__ == "__main__":
    unittest.main()