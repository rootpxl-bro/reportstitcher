"""Input readers for ReportStitcher."""

import csv
import json
from pathlib import Path


class Reader:
 def __init__(self, path):
 self.path = Path(path)

 def read(self):
 suffix = self.path.suffix.lower()
 if suffix == ".json":
 return self._json()
 if suffix == ".csv":
 return self._csv()
 if suffix in (".txt", ".log"):
 return self._lines()
 raise ValueError(f"unsupported format: {suffix}")

 def _json(self):
 with open(self.path, "r", encoding="utf-8") as fh:
 return json.load(fh)

 def _csv(self):
 with open(self.path, "r", encoding="utf-8", newline="") as fh:
 return list(csv.DictReader(fh))

 def _lines(self):
 with open(self.path, "r", encoding="utf-8") as fh:
 return [line.rstrip("\n") for line in fh if line.strip()]