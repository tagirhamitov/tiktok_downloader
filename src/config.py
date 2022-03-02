import json

class Config:
    def __init__(self):
        with open("config.json") as config_file:
            data = json.load(config_file)
            self.user_agent = data.get("user_agent")
