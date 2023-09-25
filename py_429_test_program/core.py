import json

class Core:
    def readFile(self):
        try:
            with open("tests.json", "r", encoding="utf-8") as file:
                data = file.read()
                data = json.loads(data) # stringdan list korinishiga parse qilingan
                return data
        except FileNotFoundError:
            print("Bunday fayl mavjud emas!")
            exit(0)