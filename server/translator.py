import json


class Translator:
    param = None

    def __init__(self, param):
        self.param = param
        
    def returnJSON(self):
        return json.dumps(self.param)
