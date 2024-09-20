import json
import random

class Lokalita:
    def __init__(self):
        self.beavers = []
        self.dens = []

    def __str__(self):
        strin = ""
        for i in self.beavers:
            strin += f"Beaver {i['id']}:\n   is {i['age']} years old\n   is {i['sex']}\n"
            if i["den_id"]:
                strin += f"   lives in den {i['den_id']}\n"
            else:
                strin += f"   is homeless\n"
            strin += "\n"
        return strin

    def load(self, filePath, typ):
        if typ == "beaver":
            self.beavers = json.loads(open("beaver-list.json", "r").read())
        elif typ == "den":
            self.dens = json.loads(open(filePath, "r").read())

    def assign(self):
        for beaver in self.beavers:
            beaver["den_id"] = random.choice(self.dens)["id"]

lokalit = Lokalita()
lokalit.load("beaver-list.json", "beaver")
lokalit.load("dens-list.json", "den")
lokalit.assign() # assign random dens to beavers
print(lokalit)
