import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        with open('python/tasker/taski.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)
