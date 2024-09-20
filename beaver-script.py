import json

class Lokalita:
  def __init__(self):
    self.beavers = []

  def __str__(self):
    return "Test"

  def load(self, filePath):
    file = json.loads(open(filePath, "r"))

lokalit = Lokalita()
print(lokalit)
