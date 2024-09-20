import json

class Lokalita:
  def __init__(self):
    self.beavers = []
    self.dens = []

  def __str__(self):
    strin = ""
    for i in self.beavers:
        strin += f"Beaver {i['id']} lives in Den {i['den_id']}. "
    return strin

  def load(self, filePath, typ):
    if typ == "beaver":
      self.beavers = json.loads(open(filePath, "r"))
    elif typ == "den":
      self.dens = json.loads(open(filePath, "r"))

lokalit = Lokalita()
lokalit.load(".\beaver-list.json", "beaver")
lokalit.load(".\dens-list.json", "den")
print(lokalit)
