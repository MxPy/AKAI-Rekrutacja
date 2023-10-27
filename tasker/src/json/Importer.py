import json


class Importer:

    def __init__(self):
        self.tasks = []

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', "r", encoding='utf8') as f:
            for task in json.load(f):
                self.tasks.append({"content": task['content'], "done": task['done']})


    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.tasks;