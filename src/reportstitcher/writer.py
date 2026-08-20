"""Output writers for ReportStitcher."""

import csv
import json
from pathlib import Path


class Writer:
 def __init__(self, path):
 self.path = Path(path)

 def write(self, rows):
 self.path.parent.mkdir(parents=True, exist_ok=True)
 suffix = self.path.suffix.lower()
 if suffix == ".json":
 self._json(rows)
 elif suffix == ".csv":
 self._csv(rows)
 else:
 self._text(rows)

 def _json(self, rows):
 self.path.write_text(json.dumps(rows, indent=2), encoding="utf-8")

 def _csv(self, rows):
 keys = list(rows[0].keys()) if rows else []
 with open(self.path, "w", encoding="utf-8", newline="") as fh:
 writer = csv.DictWriter(fh, fieldnames=keys)
 writer.writeheader()
 writer.writerows(rows)

 def _text(self, rows):
 lines = [str(r) for r in rows]
 self.path.write_text("\n".join(lines), encoding="utf-8")