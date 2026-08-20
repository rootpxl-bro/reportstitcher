"""Transformation steps for ReportStitcher."""


def normalize(rows):
 """Normalize mixed records into a consistent shape."""
 normalized = []
 for row in rows:
 if isinstance(row, str):
 normalized.append({"value": row})
 elif isinstance(row, dict):
 normalized.append({"value": row.get("value", row.get("name", ""))})
 else:
 normalized.append({"value": str(row)})
 return normalized


def enrich(rows):
 for row in rows:
 row["length"] = len(str(row["value"]))
 row["processed"] = True
 return rows