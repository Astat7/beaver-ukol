import json

class Lokalita:
  def __init__(self):
    self.beavers = []

  def __str__(self):
    return "Test"

  def load(self, filePath):
    self.beavers = json.loads(open(filePath, "r"))

lokalit = Lokalita()
lokalit.load(".\beaver-list.json")
print(lokalit)
