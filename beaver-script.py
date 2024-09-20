import json

class Lokalita:
  def __init__(self):
    self.beavers = []
    self.dens = []

  def __str__(self):
    return f"Beaver {self.beavers[0]['id']} lives in Den {self.beavers[0]['den_id']}"

  def load(self, filePath, typ):
    if typ == "beaver":
      self.beavers = json.loads(open(filePath, "r"))
    elif typ == "den":
      self.dens = json.loads(open(filePath, "r"))

lokalit = Lokalita()
lokalit.load(".\beaver-list.json", "beaver")
lokalit.load(".\dens-list.json", "den")
print(lokalit)
