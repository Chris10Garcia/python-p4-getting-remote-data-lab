import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_json = json.loads(self.get_response_body()) #json.loads requires a response.content or response.text input
        return data_json


# url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
# test = GetRequester(url)

# print(json.dumps(test.load_json()))

# https://get.geojs.io/v1/ip/geo.json