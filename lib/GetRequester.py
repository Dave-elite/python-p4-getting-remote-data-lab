import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raises an error for bad responses
        return response.content  # Returns bytes object

    def load_json(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return json.loads(response.content)
    
    
    
    
    
    
    
    # def get_response_body(self):
    #     response = requests.get(self.url)
    #     response.raise_for_status()  # Raises an error for bad responses
    #     return response.text  # Ensure this returns a string

    # def load_json(self):
    #     response_body = self.get_response_body()
    #     return json.loads(response_body)
